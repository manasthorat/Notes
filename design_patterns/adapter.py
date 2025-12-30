class PaymentGateway:
    def pay(self, amount):
        pass


class OldPaymentSystem:
    def make_payment(self, value):
        return f"Paid {value}"


class PaymentAdapter(PaymentGateway):
    def __init__(self, old_system):
        self.old_system = old_system

    def pay(self, amount):
        return self.old_system.make_payment(amount)


gateway = PaymentAdapter(OldPaymentSystem())
print(gateway.pay(500))
