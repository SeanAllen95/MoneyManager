class Account:

    def __init__(self, user_id, type, balance, id = None):
        self.user_id = user_id
        self.type = type
        self.balance = balance
        self.id = id

    def increase_balance(self, amount):
        self.balance += amount
    
    def decrease_balance(self, amount):
        self.balance -= amount
        
