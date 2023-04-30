from models.account import Account
from models.user import User
from models.merchant import Merchant

import repositories.account_repository as account_repository
import repositories.merchant_repository as merchant_repository
import repositories.user_repository as user_repository

user_repository.delete_all()
merchant_repository.delete_all()
account_repository.delete_all()

user1 = User("Brian")
user_repository.save(user1)

account1 = Account(user1, "Personal", 100)
account_repository.save(account1)

merchant1 = Merchant("Tesco", "Food", 50)
merchant_repository.save(merchant1)

merchant2 = Merchant("Primark", "Clothing", 20)
merchant_repository.save(merchant2)

merchant3 = Merchant("Scottish Power", "Bills", 100)
merchant_repository.save(merchant3)

merchant4 = Merchant("Winchester", "Pub", 15)
merchant_repository.save(merchant4)

