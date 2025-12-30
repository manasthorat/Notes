class PaymentStrategy:
    def pay(self, amount):
        pass


class CardPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid {amount} via card"


class UpiPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Paid {amount} via UPI"


class Checkout:
    def __init__(self, strategy):
        self.strategy = strategy

    def process(self, amount):
        return self.strategy.pay(amount)


checkout = Checkout(UpiPayment())
print(checkout.process(1000))
