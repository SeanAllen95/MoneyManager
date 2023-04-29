from db.run_sql import run_sql

from models.user import User
from models.account import Account
from models.merchant import Merchant


def save(account):
    sql = "INSERT INTO accounts (user_id, type, balance) VALUES (%s, %s, %s) RETURNING id"
    values = [account.user_id.id, account.type, account.balance]
    results = run_sql(sql, values)
    account.id = results[0]['id']
    return account

def select_all():
    accounts = []
    sql = "SELECT * FROM accounts"
    results = run_sql(sql)
    for row in results:
        account = Account(row['user_id'], row['type'], row['balance'], row['id'])
        accounts.append(account)
    
    return accounts

def delete_all():
    sql = "DELETE FROM accounts"
    run_sql(sql)