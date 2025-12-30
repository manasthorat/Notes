from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass


class CardPayment(PaymentProcessor):
    def pay(self, amount: float) -> bool:
        return amount > 0


class UPIPayment(PaymentProcessor):
    def pay(self, amount: float) -> bool:
        return amount <= 100000
