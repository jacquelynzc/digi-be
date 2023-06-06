# Digi-Backend

# Digi-Backend

This is the backend for the Digi-Backend application, an Instagram-like app with a Digimon theme.

## Technologies Used

- Python 3.10.4
- Django
- PostgreSQL

## Directory Structure

.
├── README.md
├── account
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── migrations
│ ├── models.py
│ ├── tests.py
│ └── views.py
├── digi_be
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── manage.py
├── requirements.txt
└── setup.sql

markdown
Copy code

## Setting Up Your Development Environment

1. Ensure Python 3.10.4 is installed. You can switch to this version using pyenv with the command `pyenv shell 3.10.4`.

2. Install the required Python packages using pip: `pip install -r requirements.txt`.

3. Set up your PostgreSQL database using the commands in `setup.sql`.

## Running the Project

1. Apply the migrations to create the necessary tables in the database: `python manage.py makemigrations` and `python manage.py migrate`.

2. Run the Django development server: `python manage.py runserver`.

3. Open your web browser and navigate to `http://localhost:8000` to see the application in action.

## Features

- User registration and login
- CRUD operations for posts
- Users can like posts and follow other users







