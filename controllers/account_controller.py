from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.user import User
import repositories.user_repository as user_repository
import repositories.account_repository as account_repository

account_blueprint = Blueprint("account", __name__)

@account_blueprint.route("/account")
def account(id):
    account = account_repository.select_all()
    return render_template("account/index.html", account = account)
