from db.run_sql import run_sql

from models.user import User
from models.account import Account
from models.merchant import Merchant

def save(user):
    sql = "INSERT INTO users (name, cash) VALUES (%s, %s) RETURNING id"
    values = [user.name, user.cash]
    results = run_sql(sql, values)
    user.id = results[0]['id']
    return user

def select_all():
    users = []
    sql = "SELECT * FROM users"
    results = run_sql(sql)
    for row in results:
        user = User(row['name'], row['id'])
        users.append(user)
    
    return users

# def delete_all():
#     sql = "DELETE FROM users"
#     run_sql(sql)