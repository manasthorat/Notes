from src.core.payment import UPIPayment


def test_upi_payment_limit():
    payment = UPIPayment()

    assert payment.pay(50000) is True
    assert payment.pay(150000) is False
