from flask import Flask, render_template

from controllers.user_controller import user_blueprint
from controllers.merchant_controller import merchant_blueprint
from controllers.account_controller import account_blueprint

from repositories import account_repository

app = Flask(__name__)

app.register_blueprint(user_blueprint)
app.register_blueprint(merchant_blueprint)
app.register_blueprint(account_blueprint)

@app.route('/')
def home():
    # account = account_repository.select_all()
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)