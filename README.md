## MiddleWare Architecture Project on Recipe Website.

The Recipe Management Application is a web-based platform designed to help users manage their recipes. It consists of:

- A Frontend application built with HTML, CSS, and JavaScript, and a Flask backend that serves as the API. 
- A Backend communicates with a PostgreSQL database to store and retrieve recipe data.
- A Postgres Database for storing information.

## Steps to run the application 

- First, build the application with
  > docker-compose build && docker-compose down && docker-compose up
- You can access the frontend at
  > http://localhost:8080/


## My Website contains following:

### Frontend:
The frontend application is a user interface that interacts with a Flask backend to manage recipes. It allows users to view, add, update, and delete recipes. The frontend is built using HTML for structure, CSS for styling, and JavaScript for dynamic behavior.

I have used environment variable to pass the Backend Url in `docker-compose.yaml`


The frontend application provides a user interface to interact with the recipes. Here are the main features:
- View a list of recipes.
- Add a new recipe.
- Update an existing recipe.
- Delete a recipe.

### Backend:
The Flask backend application is a RESTful API that handles requests from the frontend application. It manages recipe data, handles CRUD operations, and communicates with a PostgreSQL database.

The backend can be accesses at:
>   http://localhost:5000

The backend serves as the API for the frontend, handling CRUD operations on recipe data. Key API endpoints include:

- GET /: Get a list of all recipes.
- GET /recipe/<id>: Get details of a specific recipe.
- POST /add: Add a new recipe.
- PUT /update/<id>: Update an existing recipe.
- DELETE /delete/<id>: Delete a recipe.

## My development environment:
I first created a virtual environment and installed dependencies with following:

create  a virtual environment
> py -3 -m venv .venv

activate the environment (made sure you use below command in cmd)
> .venv\Scripts\activate

install flask using pip command
> pip install Flask

to store packages to install
> python -m pip freeze > requirements.txt

to install the list of packages from requirements
> python -m pip install -r requirements.txt








