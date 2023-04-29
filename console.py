from models.account import Account
from models.user import User
from models.merchant import Merchant

import repositories.account_repository as account_repository
import repositories.merchant_repository as merchant_repository
import repositories.user_repository as user_repository

# user_repository.delete_all()

user1 = User("Brian", 100)
user_repository.save(user1)

