class Order:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, user):
        self.subscribers.append(user)

    def place_order(self):
        for user in self.subscribers:
            user.notify()


class User:
    def notify(self):
        print("Order placed notification received")


order = Order()
order.subscribe(User())
order.subscribe(User())

order.place_order()
