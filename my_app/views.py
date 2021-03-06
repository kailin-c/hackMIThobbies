from my_app import app, db
from flask import render_template, request, redirect
from my_app.models import Fact, Post, PostRecipe, PostKnitting, PostHandletter

import requests

name = ""
facts = {"Hobbies": "running, biking, handlettering", "Favourite drink": "smoothies"}
posts = [{"title": "this is my title", "description": "this is my description", "username": "this is my username"}]

@app.route("/")
def index():
    # fact query (from the tables we made)
    db_facts = Fact.query.all()
    fact_dict = {fact.name: fact.value for fact in db_facts}

    # post query (from the tables we made)
    db_posts = Post.query.all()
    post_list = [{"title": post.title, "description": post.description, "username": post.username} for post in db_posts]
    return render_template("index.html", name=name, facts=fact_dict, posts=post_list)

@app.route("/change_name")
def change_name():
    global name
    new_name=request.args.get("name")
    name = new_name
    return redirect("/")

# updating posts from postmaster here
@app.route("/post", methods=["POST"])
def post():
    if request.method == "POST":
        post_info = request.get_json()
        new_post = Post(title = post_info['title'], description=post_info['description'], username=post_info['username'])
        db.session.add(new_post)
        db.session.commit()
    return redirect("/")

# updating facts from postmaster here
@app.route("/change_facts", methods=["POST"])
def change_facts():
    if request.method == "POST":
        change_facts = request.get_json()
        for key, value in change_facts.items():
            if Fact.query.filter(Fact.name == key).first() is None:
                new_fact = Fact(name=key, value=value)
                db.session.add(new_fact)
        db.session.commit()
    return redirect("/")

# go to wheel page
@app.route("/wheel")
def wheel():
    return render_template("wheel.html")

# go to boardgames page
@app.route("/boardgames")
def boardgames():
    # fact query (from the tables we made)
    db_facts = Fact.query.all()
    fact_dict = {fact.name: fact.value for fact in db_facts}

    # post query (from the tables we made)
    db_posts = Post.query.all()
    post_list = [{"title": post.title, "description": post.description, "username": post.username} for post in db_posts]
    return render_template("boardgames.html", name=name, facts=fact_dict, posts=post_list)
    
@app.route("/recipes")
def recipes():
    # fact query (from the tables we made)
    db_facts = Fact.query.all()
    fact_dict = {fact.name: fact.value for fact in db_facts}

    # post query (from the tables we made)
    db_posts = PostRecipe.query.all()
    post_list = [{"title": post.title, "description": post.description, "username": post.username} for post in db_posts]
    return render_template("recipes.html", name=name, facts=fact_dict, posts=post_list)

@app.route("/knitting")
def knitting():
    # fact query (from the tables we made)
    db_facts = Fact.query.all()
    fact_dict = {fact.name: fact.value for fact in db_facts}
    
    # post query (from the tables we made)
    db_posts = PostKnitting.query.all()
    post_list = [{"title": post.title, "description": post.description, "username": post.username} for post in db_posts]
    return render_template("knitting.html", name=name, facts=fact_dict, posts=post_list)
    

@app.route("/handletter")
def handletter():
    # fact query (from the tables we made)
    db_facts = Fact.query.all()
    fact_dict = {fact.name: fact.value for fact in db_facts}
    
    # post query (from the tables we made)
    db_posts = PostHandletter.query.all()
    post_list = [{"title": post.title, "description": post.description, "username": post.username} for post in db_posts]
    return render_template("handletter.html", name=name, facts=fact_dict, posts=post_list)
    
