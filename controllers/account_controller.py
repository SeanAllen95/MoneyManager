from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.user import User
from models.account import Account
import repositories.user_repository as user_repository
import repositories.account_repository as account_repository
import repositories.merchant_repository as merchant_repository

account_blueprint = Blueprint("account", __name__)

@account_blueprint.route("/account")
def account():
    account = account_repository.select_all()
    return render_template("account/index.html", account = account)

@account_blueprint.route("/account/transactions")
def transactions():
    account = account_repository.select_all()
    merchants = merchant_repository.select_all()
    return render_template("account/transactions.html", account = account, merchants = merchants)

@account_blueprint.route("/account/new")
def new_account():
    account = account_repository.select_all()
    return render_template("account/new_account.html", account = account)

@account_blueprint.route("/account/new_transaction")
def new_transaction():
    account = account_repository.select_all()
    return render_template("account/new_transaction.html", account = account)

@account_blueprint.route("/account",  methods=['POST'])
def create_account():
    user_id = request.form['user_id']
    type = request.form['type']
    balance = request.form['balance']
    account = Account(user_id, type, balance)
    account_repository.save(account)
    return redirect('/account')

@account_blueprint.route("/account/<id>/edit", methods=['GET'])
def edit_account(id):
    account = account_repository.select(id)
    return render_template('account/edit.html', account = account)

@account_blueprint.route("/account", methods=['POST'])
def update_account(id):
    user_id = request.form['user_id']
    type = request.form['type']
    balance = request.form['balance']
    account = Account(user_id, type, balance, id)
    account_repository.update(account)
    return redirect('/merchant')

@account_blueprint.route("/account/<id>/view", methods=['GET'])
def view_account(id):
    account = account_repository.select(id)
    return render_template("account/view.html", account = account)




# # @merchant_blueprint.route("/merchant/<id>/delete", methods=['POST'])
# # def delete_merchant(id):
# #     merchant_repository.delete(id)
# #     return redirect('/merchant')