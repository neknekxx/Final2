import os
import openai
import json
import random
import requests
from django.utils.timezone import now
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Element
from .models import Discovery
from django.conf import settings



# Home page view
@login_required
def home(request):
    return render(request, 'home.html')

# Log in view
def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error_message': "Invalid login details."})
    return render(request, 'login.html')

# Sign up view
def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')

# About view
def about(request):
    return render(request, 'about.html')

# Periodic Table view
@login_required
def element_list(request):
    elements = Element.objects.all().order_by('atomic_number')
    return render(request, 'elements/periodic_table.html', {'elements': elements})

# Element detail view
@login_required
def element_detail(request, symbol):
    element = get_object_or_404(Element, symbol=symbol)
    return render(request, 'elements/element_detail.html', {'element': element})

# Update Element Description
@login_required
def update_element(request, symbol):
    element = get_object_or_404(Element, symbol=symbol)

    if request.method == "POST":
        new_description = request.POST.get('description')
        if new_description:
            element.description = new_description
            element.save()
        return redirect('element_detail', symbol=element.symbol)

    return render(request, 'elements/element_detail.html', {'element': element})

# Upload Element Image
@login_required
def upload_image(request, symbol):
    element = get_object_or_404(Element, symbol=symbol)

    if request.method == "POST" and request.FILES.get('image'):
        image = request.FILES['image']
        filename, file_extension = os.path.splitext(image.name)
        new_filename = f"{element.symbol}_{now().strftime('%Y%m%d%H%M%S')}{file_extension}"

        # Delete old image if it exists
        if element.image and default_storage.exists(element.image.name):
            default_storage.delete(element.image.name)

        # Save the new image
        element.image.save(new_filename, image, save=True)

        return redirect('element_detail', symbol=element.symbol)

    return render(request, 'elements/element_detail.html', {'element': element})

# Main Quiz Page
@login_required
def quiz(request):
    return render(request, 'quiz.html')

# Multiple Choice Quiz Page
@login_required
def multiple_choice_quiz(request):
    return render(request, 'mcq_quiz.html')

# Jumbled Words Quiz Page
@login_required
def jumbled_words_quiz(request):
    return render(request, 'jumbled_quiz.html')


# Load API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Chatbot API View
@csrf_exempt
@login_required  # Ensure only logged-in users access the chatbot
def chatbot_response(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "")

            # Create an OpenAI client with the API key
            client = openai.OpenAI(api_key=OPENAI_API_KEY)

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_message}]
            )

            bot_reply = response.choices[0].message.content

            return JsonResponse({"reply": bot_reply})

        except Exception as e:
            return JsonResponse({"reply": f"Error: {str(e)}"}, status=500)

    return JsonResponse({"reply": "Invalid request"}, status=400)

def discover_view(request):
    discoveries = list(Discovery.objects.all())
    random.shuffle(discoveries)
    
    for d in discoveries:
        d.image_filename = f"{d.element_name.lower().replace(' ', '_')}.webp"  # ✅ Ensure filename matches saved images

    context = {"discoveries": discoveries[:5]}  # Send only 5 random discoveries
    return render(request, "discover.html", context)

def discovery_list(request):
    """Fetch all discovery data from the database"""
    discoveries = Discovery.objects.all()
    data = [
        {
            "element_name": d.element_name,
            "discovered_by": d.discovered_by,
            "discovery_year": d.discovery_year,
            "trivia": d.trivia,
            "image_filename": f"/static/images/elements/{d.image_filename}"  # ✅ Provide full image path
        }
        for d in discoveries
    ]
    return JsonResponse(data, safe=False)

def discover_page(request):
    return render(request, "discover.html")


# NASA API
def nasa_page(request):
    return render(request, "nasa.html")