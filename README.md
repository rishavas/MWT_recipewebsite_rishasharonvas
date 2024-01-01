# Backend
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



CRUD:
``````

GET /  :(get all recipes)

GET /recipes/{recipe_id}  :(gets recipe by id)

POST /add :(adds new recipes)

PUT /update/{recipe_id}  : (updates recipe by id)

DELETE /delete/{recipe_id}  : (deletes receipe id)

``````


