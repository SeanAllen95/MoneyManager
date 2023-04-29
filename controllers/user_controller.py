from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.user import User
import repositories.user_repository as user_repository
# import repositories.location_repository as location_repository

users_blueprint = Blueprint("user", __name__)

@users_blueprint.route("/user")
def user():
    user = user_repository.select_all() # NEW
    return render_template("user/index.html", user = user)

# @users_blueprint.route("/users/<id>")
# def show(id):
#     user = user_repository.select(id)
#     locations = location_repository.locations_by_user(user)
#     return render_template("users/show.html", user=user, locations=locations)
