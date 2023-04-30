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

@merchant_blueprint.route("/merchant/new")
def new_merchant():
    merchant = merchant_repository.select_all()
    return render_template("merchant/new.html")

@merchant_blueprint.route("/merchant",  methods=['POST'])
def create_merchant():
    name = request.form['name']
    category = request.form['category']
    amount = request.form['amount']
    merchant = Merchant(name, category, amount)
    merchant_repository.save(merchant)
    return redirect('/merchant')
