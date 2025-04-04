# Periodic_Table_App

Periodic Table Web App is an interactive educational platform that allows users to explore chemical elements with detailed information. It features a clickable periodic table, a multiple-choice quiz, and a jumbled words quiz to test users' knowledge. The app includes user authentication with admin and regular user roles, ensuring a secure and personalized experience. Users can edit element descriptions and upload images to enhance the learning experience.
------------------------------------------------------------------------------------------------------------------------------------------------------------

To open the Periodic Table Web App:

Step 1
Download the the zip folder from Github and extract it.

------------------------------------------------------------------------------------------------------------------------------------------------------------
Step 2
In Visual Studio Code open the folder named " periodic_table_MainApp "

Make sure DJANGO and PILLOW is installed, if not yet installed run this two command in your Visual Studio Code terminal:

TO INSTALL DJANGO:

" pip install django "
to check if it is properly installed run this:
" django-admin --version "

TO INSTALL PILLOW:

" pip install pillow "

------------------------------------------------------------------------------------------------------------------------------------------------------------
Step 3
After you installed DJANGO and PILLOW you can now use the command " python manage.py runserver ", after that you will see a message like this:

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 21, 2025 - 22:49:42
Django version 5.1.6, using settings 'periodic_table.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

This means that you successfully run the web app,
the last thing to do is Ctrl+Click the "http://127.0.0.1:8000/" or copy and paste it on a browser to access it.

------------------------------------------------------------------------------------------------------------------------------------------------------------

BEFORE I FORGOT YOU NEED TO REGISTER FIRST


------------------------------------------------------------------------------------------------------------------------------------------------------------




Features and Functionalities
1. User Authentication & Authorization
> Signup & Login – Users can create an account and log in.

> User Roles - The admin can add, edit, and delete elements and regular users can only view elements and take quizzes. Logout button allows users to log out securely.


2. Periodic Table Page
> Interactive Periodic Table – Users can click on an element symbol to view its details.

> CRUD Functionality for Elements (Admin Only) –
      
  >>Create: Add new elements.
      
  >>Read: View detailed information about each element.
      
  >>Update: Edit element details (name, atomic number, symbol, description, image).
    
  >>Delete: Remove an element.


> Add Images & Descriptions – Users can upload images and update element descriptions.

3. Quiz Section
> Two Quiz Types:
> >>Multiple Choice Quiz
> >>Jumbled Words Quiz

>  >>Randomized Questions – Questions appear in a random order for each quiz attempt.
>  >
>  >>Quiz Progress Indicator – Shows which question number the user is on.
>  >
>  >>Instant Feedback – Displays correct or incorrect responses.
>  >
>  >>Final Score Summary – Users can see their total score at the end of the quiz.
>  >
>  >>"Go Back" Button – Redirects users back to the quiz selection page after finishing.

------------------------------------------------------------------------------------------------------------------------------------------------------------

Group Members:

Bautista, Kenneth

Magapi, Daniel

Veneracion, Kurt

Guevarra, Ma. Paula


