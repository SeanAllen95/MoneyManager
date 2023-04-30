from db.run_sql import run_sql
import psycopg2

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
        merchant = Merchant(row['name'], row['category'], row['amount'], row['id'])
        merchants.append(merchant)
    
    return merchants

# def add_merchant(name, category, amount):
#     conn = psycopg2.connect(database="money_manager")
#     cur = conn.cursor()
#     cur.execute("INSERT INTO merchants (name, category, amount) VALUES (%s, %s, %s)", (name, category, amount))
#     conn.commit()
#     cur.close()
#     conn.close()

def select(id):
    merchant = None
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        merchant = Merchant(result['name'], result['category'], result['amount'] )
    return merchant

def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)

