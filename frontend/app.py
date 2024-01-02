import os,time
from flask import Flask, jsonify,request,render_template
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route("/",methods=['GET'])
def home_page():
    # recipe=insert_recipe(db,"Maggi","pwofjuerhfuqvyrf")
   
    return render_template('index.html',backend_url=os.getenv('BACKEND_URL'))

@app.route('/add',methods=['GET'])
def add_new_recipe():
    return render_template('add.html',backend_url=os.getenv('BACKEND_URL'))

@app.route('/update/<int:id>',methods=['GET'])
def updates_recipe(id):
    return render_template('update.html',backend_url=os.getenv('BACKEND_URL'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
