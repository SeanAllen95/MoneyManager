from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
import repositories.user_repository as user_repository
import repositories.merchant_repository as merchant_repository
# import repositories.location_repository as location_repository

merchant_blueprint = Blueprint("merchant", __name__)

@merchant_blueprint.route("/merchant")
def merchant():
    merchant = merchant_repository.select_all() # NEW
    return render_template("merchant/index.html", merchant = merchant)



# @users_blueprint.route("/users/<id>")
# def show(id):
#     user = user_repository.select(id)
#     locations = location_repository.locations_by_user(user)
#     return render_template("users/show.html", user=user, locations=locations)
