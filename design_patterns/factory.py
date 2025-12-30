class Notification:
    def send(self, message):
        pass


class EmailNotification(Notification):
    def send(self, message):
        return f"Email sent: {message}"


class SMSNotification(Notification):
    def send(self, message):
        return f"SMS sent: {message}"


def notification_factory(channel):
    if channel == "email":
        return EmailNotification()
    if channel == "sms":
        return SMSNotification()


notifier = notification_factory("email")
print(notifier.send("Welcome"))
