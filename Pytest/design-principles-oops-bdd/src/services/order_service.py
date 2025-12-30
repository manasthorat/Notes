class OrderService:
    def __init__(self, payment_processor, notifier, repository):
        self.payment_processor = payment_processor
        self.notifier = notifier
        self.repository = repository

    def place_order(self, order) -> bool:
        if not self.payment_processor.pay(order.amount):
            return False

        self.repository.save(order)
        self.notifier.send("Order placed successfully")
        return True
