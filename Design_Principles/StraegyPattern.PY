class PaymentStrategy:
    def pay(self, amount):
        pass

class CreditCard(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount} with Credit Card"

class PayPal(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount} with PayPal"

class Cart:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def checkout(self, amount):
        return self.strategy.pay(amount)

# Test
cart = Cart(PayPal())
print(cart.checkout(100))