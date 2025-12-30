from src.services.order_service import OrderService
from src.core.payment import CardPayment
from src.core.notifier import EmailNotifier
from src.core.repository import OrderRepository
from src.models.order import Order


def test_place_order_success():
    payment = CardPayment()
    notifier = EmailNotifier()
    repo = OrderRepository()
    service = OrderService(payment, notifier, repo)

    order = Order(1, 500)

    result = service.place_order(order)

    assert result is True
