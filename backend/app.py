import os,time
from flask import Flask, jsonify,request
from flask_sqlalchemy import SQLAlchemy
from waitforit import wait_for_postgres
from flask_cors import CORS

wait_for_postgres(
    host='postgresdb',
    port=5432,
    user='vas',
    password='password',
    database='mydb',
    max_attempts=30,
    delay=2
)

# Continue with the rest of your application logic
print("PostgreSQL is ready. Continue with the application.")



app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://vas:password@postgresdb/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy instance
db = SQLAlchemy(app)

# Define a simple model
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), nullable=False)
    ingredients=db.Column(db.String(200),nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()  # Create database tables

def insert_recipe(db,title,ingredients):
    new_recipe = Recipe(title=title,ingredients=ingredients)
    db.session.add(new_recipe)
    db.session.commit()

def read_recipes(db):
    recipes = Recipe.query.all()
    recipe_list = []
    for recipe in recipes:
        recipe_list.append({'id': recipe.id, 'title': recipe.title, 'ingredients': recipe.ingredients})
    return jsonify({'recipes': recipe_list})

def read_recipes_by_id(db, id):
    recipe=Recipe.query.get(id)
    return jsonify({'id': recipe.id, 'title': recipe.title, 'ingredients': recipe.ingredients})

def update_recipes(db,id,title,ingredients):
    recipe=Recipe.query.get(id)
    # Update user information based on the request data
    recipe.title=title
    recipe.ingredients=ingredients
    db.session.commit()
    return jsonify({'message': 'recipe updated successfully'})

def delete_recipes(db,id):
    recipe=Recipe.query.get(id)
    # Update user information based on the request data
    db.session.delete(recipe)
    db.session.commit()
    return jsonify({'message': 'recipe deleted successfully'})


@app.route("/",methods=['GET'])
def get_all_recipes():
    # recipe=insert_recipe(db,"Maggi","pwofjuerhfuqvyrf")
    return read_recipes(db)

@app.route('/recipe/<int:id>',methods=['GET'])
def get_recipe(id):
    return read_recipes_by_id(db, id)
    

@app.route('/add',methods=['POST'])
def add_new_recipe():
    title = request.form.get('title')
    ingredients = request.form.get('ingredients')
    insert_recipe(db,title,ingredients)
    return jsonify({'message': 'inserted recipes succesfully'})

@app.route('/update/<int:id>',methods=['PUT'])
def updates_recipe(id):
    recipe = Recipe.query.get(id)
    title = request.form.get('title')
    ingredients = request.form.get('ingredients')
    return update_recipes(db,id,title,ingredients)
    
@app.route("/delete/<int:id>",methods=['DELETE'])
def delete_recipe(id):
    return delete_recipes(db,id)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
