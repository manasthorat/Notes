class MessageService:
    def send(self, msg):
        pass


class EmailService(MessageService):
    def send(self, msg):
        return f"Email sent: {msg}"


class SMSService(MessageService):
    def send(self, msg):
        return f"SMS sent: {msg}"


class Notification:
    def __init__(self, service: MessageService):
        self.service = service

    def notify(self, msg):
        return self.service.send(msg)


email_notification = Notification(EmailService())
sms_notification = Notification(SMSService())

print(email_notification.notify("Hello"))
print(sms_notification.notify("Hi"))
