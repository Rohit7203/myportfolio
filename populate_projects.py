import os
import django

# Tell Django which settings to use
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myportfolio.settings")

# Start Django
django.setup()

# Import your Project model
from portfolio.models import Project


# Delete existing projects to avoid duplicates
Project.objects.all().delete()


# Project 1
Project.objects.create(
    title="Student Management System",
    description="Django-based web application for managing student records with CRUD functionality.",
    technologies="Python, Django, HTML, CSS, SQLite",
    github_url="https://github.com/Rohit7203/django-project",
    live_url=""
)


# Project 2
Project.objects.create(
    title="Django Portfolio",
    description="Personal portfolio website built using Django with a dynamic project section.",
    technologies="Python, Django, HTML, CSS, JavaScript",
    github_url="https://github.com/Rohit7203/myportfolio",
    live_url="https://myportfolio-opl4.onrender.com/"
)


# Project 3
Project.objects.create(
    title="Data Analytics Dashboard",
    description="Interactive dashboard for analyzing business data and generating useful insights.",
    technologies="SQL, Power BI, PostgreSQL",
    github_url="",
    live_url=""
)


print("Projects added successfully!")

# Display projects
for project in Project.objects.all():
    print(project.title)