class Merchant:

    def __init__(self, name, category, amount, id = None):
        self.name = name
        self.category = category
        self.amount = amount
        self.id = id

    def increase_amount(self, amount):
        self.amount += amount
    
    def decrease_amount(self, amount):
        self.amount -= amount
        
        
