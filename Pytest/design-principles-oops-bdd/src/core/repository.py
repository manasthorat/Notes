class OrderRepository:
    def save(self, order) -> None:
        print(f"Order {order.order_id} saved")
