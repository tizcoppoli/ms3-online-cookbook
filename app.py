import os
import random
from datetime import datetime
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_paginate import Pagination, get_page_args
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


def pagination_recipes(offset=0, per_page=10):
    recipes = list(mongo.db.recipes.find())
    recipes.reverse()
    return recipes[offset: offset + per_page]


def pagination_recipes_profile(offset=0, per_page=10):
    user = mongo.db.users.find_one({"username": session["user"]})
    recipes = list(mongo.db.recipes.find({"created_by": str(user["_id"])}))
    recipes.reverse()
    return recipes[offset: offset + per_page]


def pagination_recipes_category(category, offset=0, per_page=10):
    recipes = list(mongo.db.recipes.find({"category": category}))
    return recipes[offset: offset + per_page]


@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        existing_contact = mongo.db.contacts.find_one(
            {"email_address": request.form.get("email-address").lower()})
        if existing_contact:
            flash("already in newsletter")
            return redirect(url_for("home"))

        register = {"email_address": request.form.get("email-address").lower()}
        mongo.db.contacts.insert_one(register)
        flash("Added to newsletter")
        return redirect(url_for("home"))

    recipes_admin = list(mongo.db.recipes.find(
        {"created_by": "605b52c31a93cdb5624e75ba"}))
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    random.shuffle(recipes_admin)
    return render_template(
        "home.html",
        recipes=recipes_admin,
        categories=categories,
        recipes_admin=recipes_admin)


@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    per_page = 6
    total = len(recipes)
    pag_recipes = pagination_recipes(
        offset=page*per_page-per_page, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total)
    return render_template(
        "recipes.html",
        categories=categories,
        recipes=pag_recipes,
        page=page,
        per_page=per_page,
        pagination=pagination)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    flash("You searched: " + query)
    return render_template("search.html", recipes=recipes)


@app.route("/category/<category>", methods=["GET", "POST"])
def category(category):
    recipes = list(mongo.db.recipes.find({"category": category}))
    category_obj = mongo.db.categories.find_one({"_id": ObjectId(category)})
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    per_page = 6
    total = len(recipes)
    pag_recipes = pagination_recipes_category(
        category, offset=page*per_page-per_page, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total)
    return render_template(
        "category.html",
        recipes=pag_recipes,
        category=category,
        category_obj=category_obj,
        page=page, per_page=per_page,
        pagination=pagination)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        if request.form.get("newsletter-checkbox"):
            existing_contact = mongo.db.contacts.find_one(
                {"email_address": request.form.get("email").lower()})
            if not existing_contact:
                contact = {"email_address": request.form.get("email").lower()}
                mongo.db.contacts.insert_one(contact)

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "email": request.form.get("email").lower(),
            "user_img": "https://i.imgur.com/3XizFU1.png"
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                existing_user["password"],
                    request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    user = mongo.db.users.find_one({"username": session["user"]})
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        if request.method == "POST":
            if request.form.get("user_email"):
                contact = {"email_address": request.form.get(
                    "user_email").lower()}
                if request.form.get("newsletter-checkbox"):
                    mongo.db.contacts.insert_one(contact)
                else:
                    mongo.db.contacts.remove(
                        {"email_address": request.form.get(
                            "user_email").lower()})

                user_img = request.form.get(
                    "user_img") if request.form.get(
                        "user_img") else "https://i.imgur.com/3XizFU1.png"
                submit = {"$set": {
                    "email": request.form.get("user_email"),
                    "user_img": user_img
                    }}
                mongo.db.users.update(user, submit)
                flash("User Successfully Updated")
                return redirect(url_for("profile", username=username))

            else:
                recipe_img = request.form.get(
                    "recipe_img") if request.form.get(
                        "recipe_img") else "https://i.imgur.com/3XizFU1.png"
                is_spicy = "on" if request.form.get("is_spicy") else "off"
                is_vegan = "on" if request.form.get("is_vegan") else "off"
                ingredient_list = request.form.getlist("ingredient_list[]")
                recipe_steps = request.form.getlist("recipe_steps[]")
                recipe = {
                    "category": request.form.get("category_name"),
                    "recipe_name": request.form.get("recipe_name"),
                    "is_spicy": is_spicy,
                    "is_vegan": is_vegan,
                    "created_by": str(user["_id"]),
                    "ingredient_list": ingredient_list,
                    "recipe_steps": recipe_steps,
                    "recipe_img": recipe_img,
                    "preparation_time": request.form.get("preparation_time"),
                    "servings": request.form.get("servings"),
                    "difficulty": request.form.get("difficulty"),
                    "likes": 0,
                    "like_array": [],
                    "comment_array": []
                }
                mongo.db.recipes.insert_one(recipe)
                flash("Recipe Successfully Added")
                return redirect(url_for("profile", username=username))

        recipes_complete = list(mongo.db.recipes.find(
            {"created_by": str(user["_id"])}))
        categories = mongo.db.categories.find().sort(
            "category_name", 1)
        is_subscribed = mongo.db.contacts.find_one(
            {"email_address": user["email"]})
        page, per_page, offset = get_page_args(
            page_parameter='page', per_page_parameter='per_page')
        per_page = 6
        total = len(recipes_complete)
        pag_recipes = pagination_recipes_profile(
            offset=page*per_page-per_page, per_page=per_page)
        pagination = Pagination(page=page, per_page=per_page, total=total)
        return render_template(
            "profile.html",
            user=user,
            username=username,
            categories=categories,
            recipes=pag_recipes,
            recipes_complete=recipes_complete,
            page=page,
            per_page=per_page,
            pagination=pagination,
            is_subscribed=is_subscribed)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        is_spicy = "on" if request.form.get("is_spicy") else "off"
        is_vegan = "on" if request.form.get("is_vegan") else "off"
        ingredient_list = request.form.getlist("ingredient_list[]")
        recipe_steps = request.form.getlist("recipe_steps[]")
        recipe_img = request.form.get(
            "recipe_img") if request.form.get(
                "recipe_img") else "https://i.imgur.com/3XizFU1.png"
        submit = {"$set": {
            "category": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "is_spicy": is_spicy,
            "is_vegan": is_vegan,
            "ingredient_list": ingredient_list,
            "recipe_steps": recipe_steps,
            "recipe_img": recipe_img,
            "preparation_time": request.form.get("preparation_time"),
            "servings": request.form.get("servings"),
            "difficulty": request.form.get("difficulty")
            }}
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Updated")
        return redirect(url_for("view_recipe", recipe_id=recipe_id))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_recipe.html",
        recipe=recipe,
        categories=categories)


@app.route("/view_recipe/<recipe_id>", methods=["GET", "POST"])
def view_recipe(recipe_id):
    if request.method == "POST":
        if request.form.get("textarea-comment"):
            date = datetime.now().strftime("%d/%m/%y")
            submit = {"$push": {
                "comment_array": [session["user"], request.form.get(
                    "textarea-comment"), date]}}
            mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
            flash("commento")
            return redirect(url_for("view_recipe", recipe_id=recipe_id))
        else:
            recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
            user = mongo.db.users.find_one({"username": session["user"]})
            if str(user["_id"]) in recipe["like_array"]:
                submit = {"$inc": {"likes": -1}}
                pull = {"$pull": {"like_array": {"$in": [str(user["_id"])]}}}
                mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
                mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, pull)
                flash("Like removed")
                return redirect(url_for("view_recipe", recipe_id=recipe_id))
            else:
                submit = {"$inc": {"likes": 1}}
                push = {"$push": {"like_array": str(user["_id"])}}
                mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
                mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, push)
                flash("Like added")
                return redirect(url_for("view_recipe", recipe_id=recipe_id))

    recipes = list(mongo.db.recipes.find())
    random.shuffle(recipes)
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    category = mongo.db.categories.find_one(
        {"_id": ObjectId(recipe["category"])})
    author = mongo.db.users.find_one({"_id": ObjectId(recipe["created_by"])})
    categories = mongo.db.categories.find().sort("category_name", 1)

    user = mongo.db.users.find_one(
        {"username": session["user"]}) if session else ""
    return render_template(
        "view_recipe.html",
        recipe=recipe,
        categories=categories,
        recipes=recipes,
        category=category,
        user=user,
        author=author)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("profile", username=session["user"]))


@app.route("/get_categories", methods=["GET", "POST"])
def get_categories():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name"),
            "category_description": request.form.get("category_description")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "category_description": request.form.get("category_description")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
