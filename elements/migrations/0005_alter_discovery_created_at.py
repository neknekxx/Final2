# Generated by Django 5.1.6 on 2025-03-23 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elements', '0004_discovery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discovery',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
