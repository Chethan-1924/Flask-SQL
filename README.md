This is a small implementation to test the connection of frontend with sql using flask.
Created a table in sql with 3 columns having id,name and age.
Created a HTML document that consist of form which takes name and age as inputs.
#newapp.py :
This is where I have built the connection using flask.
Used mysql.connector to connect sql.
Used render_template to find and load HTML document.
Returned the output in JSON using jsonify().
