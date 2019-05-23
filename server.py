from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL
app = Flask(__name__)

@app.route('/')
def index():
    mysql = connectToMySQL('c+r_pets')
    pets = mysql.query_db('SELECT * FROM pets;')
    return render_template("index.html", allpets=pets)

@app.route('/create', methods=["POST"])
def create():
    mysql = connectToMySQL('c+r_pets')
    query = "INSERT INTO pets (name, type) VALUES (%(na)s, %(ty)s);"
    data = {
        'na': request.form['name'],
        'ty': request.form['type'],
    }
    mysql.query_db(query, data)
    return redirect("/")



if __name__ =="__main__":
    app.run(debug=True)
