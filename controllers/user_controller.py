from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.user import User
import repositories.user_repository as user_repository
import repositories.account_repository as account_repository

user_blueprint = Blueprint("user", __name__)

@user_blueprint.route("/user")
def user():
    user = user_repository.select_all()
    account = account_repository.select_all()
    return render_template("user/index.html", user = user, account = account)



# @users_blueprint.route("/users/<id>")
# def show(id):
#     user = user_repository.select(id)
#     locations = location_repository.locations_by_user(user)
#     return render_template("users/show.html", user=user, locations=locations)
