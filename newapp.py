from flask import Flask,render_template,request,jsonify
import mysql.connector

# 1. create flask app
app=Flask(__name__)

#2.connect to database
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "testdb"
)

cursor = conn.cursor()

#3.home route (show form)
@app.route("/")
def home():
    return render_template("index.html")

#4.insert DAta into database
@app.route("/add", methods=["GET","POST"])
def adduser():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        query = "insert into users (name,age) values (%s,%s)"
        values = (name,age)

        cursor.execute(query,values)
        conn.commit()

        return "User added successfully"
    return "use POST method"

#5.show data from database
@app.route("/users")
def users():
    cursor.execute("select * from users")
    data = cursor.fetchall()
    return jsonify(data)

#6.run server

if __name__ == "__main__":
    app.run(debug=True)