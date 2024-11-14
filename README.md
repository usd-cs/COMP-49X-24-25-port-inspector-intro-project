# COMP-49X-24-25-port-inspector-intro-project
Web Forum Project

This project is a web forum application built with Django that allows users to share posts, comment on discussions, and administrators to manage content. The forum implements essential functionality to foster user interaction while giving admins control to maintain a healthy environment.

User Stories
The application satisfies the following user stories:

Post Creation: As a user, I want to be able to create a new post so that I can express my original thoughts and feelings.

Commenting: As a user, I want to be able to comment on a post so I can add to an existing discussion.

Content Moderation: As an admin, I want to be able to delete posts and comments so I can remove problematic content.

Technologies Used
Backend & Frontend Framework: Django
Database: Django’s default SQLite (or update this if another database is used)

Setup and Installation

Clone the Repository:
git clone https://github.com/yourusername/your-repo-name.git

Navigate to the Project Directory:
cd your-repo-name/intro_project

Install Dependencies: Ensure you have Django installed or install it via pip:
pip install django

Run Migrations: Set up the database tables by running:
python3 manage.py migrate

Running the Server

Start the Server:
python3 manage.py runserver

Access the Forum: Open a web browser and go to the following link:
http://127.0.0.1:8000/

