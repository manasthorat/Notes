from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass


class EmailNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"Email sent: {message}")
