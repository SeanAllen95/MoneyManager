from db.run_sql import run_sql

from models.user import User
from models.account import Account
from models.merchant import Merchant

def save(merchant):
    sql = "INSERT INTO merchants (name, category, amount) VALUES (%s, %s, %s) RETURNING id"
    values = [merchant.name, merchant.category, merchant.amount]
    results = run_sql(sql, values)
    merchant.id = results[0]['id']
    return merchant

def select_all():
    merchants = []
    sql = "SELECT * FROM merchants"
    results = run_sql(sql)
    for row in results:
        merchant = Merchant(row['name'], row['category'], row['amoount'], row['id'])
        merchants.append(merchant)
    
    return merchants

def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)