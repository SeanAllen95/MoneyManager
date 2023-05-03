from db.run_sql import run_sql

from models.user import User
from models.account import Account
from models.merchant import Merchant


def save(account):
    sql = "INSERT INTO accounts (type, balance, user_id) VALUES (%s, %s, %s) RETURNING id"
    values = [account.user_id.id, account.type, account.balance, account.id]
    results = run_sql(sql, values)
    account.id = results[0]['id']
    return account

def select_all():
    accounts = []
    sql = "SELECT * FROM accounts"
    results = run_sql(sql)
    for row in results:
        account = Account( row['id'], row['type'], row['balance'], row['user_id'])
        accounts.append(account)
    
    return accounts

def select(id):
    account = None
    sql = "SELECT * FROM accounts WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        account = Account(result['user_id'], result['type'], result['balance'], result['id'])
    return account

def delete_all():
    sql = "DELETE FROM accounts"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM accounts WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(account):
    sql = "UPDATE accounts SET (user_id, type, balance) = (%s, %s, %s) WHERE id = %s"
    values = [account.user_id, account.type, account.balance, account.id]
    run_sql(sql, values)