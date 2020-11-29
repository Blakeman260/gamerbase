import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_reviews)")
def get_reviews():
    reviews = list(mongo.db.reviews.find())
    return render_template("reviews.html", reviews=reviews)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # To check if the username already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("The Username you chose, already exists! :O ")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # This is to put new user into the 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Player registered! ☺")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # This checks if username actually exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # This checks password matches user input for username
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Player {}, Online".format(
                        request.form.get("username")))  
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else: 
                #Password doesn't match
                flash("Incorrect Username and/or Password")
                return redirect(url_for('login'))

        else:
            # Username doesn't exists
            flash("Incorrect Username and/or Password")
            return redirect(url_for('login'))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Grab sessions username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username) 
        
    return render_template(url_for("login"))


@app.route("/logout")
def logout():
    #This is to remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        review = {
            "game_title": request.form.get("game_title"),
            "game_review": request.form.get("game_review"),
            "console_name": request.form.get("console_name"),
            "would_recommend": request.form.get("would_recommend"),
            "review_author": session["user"]
        }
        mongo.db.reviews.insert_one(review)
        flash("Your Review was successfully added!")
        return redirect(url_for("get_reviews"))

    consoles = mongo.db.consoles.find().sort("console_name", 1)
    recommend = mongo.db.recommend.find().sort("would_recommend", 1)
    return render_template("add_review.html", consoles=consoles, recommend=recommend)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    if request.method == "POST":
        submit = {
            "game_title": request.form.get("game_title"),
            "game_review": request.form.get("game_review"),
            "console_name": request.form.get("console_name"),
            "would_recommend": request.form.get("would_recommend"),
            "review_author": session["user"]
        }
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, submit)
        flash("Your Review was successfully Edited!")

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    consoles = mongo.db.consoles.find().sort("console_name", 1)
    recommend = mongo.db.recommend.find().sort("would_recommend", 1)
    return render_template(
        "edit_review.html", review=review, consoles=consoles, recommend=recommend)


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Your Review was Sucessfully Removed")
    return redirect(url_for("get_reviews"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)