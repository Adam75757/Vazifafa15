from flask import Flask
from flask import render_template,redirect,request
from mysql.connector import connect

app = Flask(__name__)

db = connect(
    user = 'root',
    host = 'localhost',
    password = '11201111',
    database = 'takomillashish'
)

dbc = db.cursor()

@app.route('/')
def home():

    dbc.execute("select * from odam")
    add = dbc.fetchall()

    return render_template("index.html", odam = add)


@app.route('/sign_up/',methods =["GET","POST"])
def sign_up():
    if request.method =="POST":
    
        return redirect("/sign_in/")
    return render_template("sign_up.html")

@app.route("/sign_in/", methods = ["GET","POST"])
def sign_in():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        repeat_password = request.form.get("repeat_password")
        email = request.form.get("email")

        dbc.execute(" insert into odam (username,password,Repait,email) values(%s,%s,%s,%s)", params=(username,password,repeat_password,email))
        db.commit()
        return redirect("/")
    return render_template("sign_in.html")


if __name__ == "__main__":
    app.run(debug = True,port= 2011)

