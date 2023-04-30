import db
from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
from models.merchant import Merchant

import repositories.user_repository as user_repository
import repositories.merchant_repository as merchant_repository
import repositories.account_repository as account_repository

merchant_blueprint = Blueprint("merchant", __name__)

@merchant_blueprint.route("/merchant")
def merchant():
    merchant = merchant_repository.select_all()
    return render_template("merchant/index.html", merchant = merchant)

# @merchant_blueprint.route('/add_merchant', methods=['POST'])
# def add_merchant_route():
#     name = request.form['name']
#     category = request.form['category']
#     amount = request.form['amount']
#     merchant_repository.add_merchant(name, category, amount)
#     return redirect(url_for('merchant'))



# @merchant_blueprint.route("/add_merchant", methods=["POST"])
# def add_merchant():
#     name = request.form["name"]
#     category = request.form["category"]
#     amount = request.form["amount"]
#     merchant = Merchant(name=name, category=category, amount=amount)
#     db.session.add(merchant)
#     db.session.commit()
#     return redirect(url_for("merchant.merchant"))

# @merchant_blueprint.route("/merchant",  methods=['POST'])
# def add_merchant():
#     name = request.form['name']
#     category = request.form['category']
#     amount = request.form['amount']
#     name = merchant_repository.select(name)
#     category = merchant_repository.select(category)
#     new_merchant = Merchant(name, category, amount)
#     merchant_repository.save(new_merchant)
#     return redirect('/merchant')


# @merchant_blueprint.route("/merchant", methods=["POST"])
# def add_merchant(new_merchant):
#     name = request.form["name"]
#     category = request.form["category"]
#     amount = request.form["amount"]
#     new_merchant = Merchant(name, category, amount)
#     add_merchant(new_merchant)
#     return redirect("/merchant")


# @users_blueprint.route("/users/<id>")
# def show(id):
#     user = user_repository.select(id)
#     locations = location_repository.locations_by_user(user)
#     return render_template("users/show.html", user=user, locations=locations)
