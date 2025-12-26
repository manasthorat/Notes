class Invoice:
    def __init__(self, amount):
        self.amount = amount


class InvoiceCalculator:
    def total(self, invoice):
        return invoice.amount


class InvoicePrinter:
    def print_invoice(self, invoice):
        return f"Invoice amount: {invoice.amount}"


invoice = Invoice(1000)
calculator = InvoiceCalculator()
printer = InvoicePrinter()

print(calculator.total(invoice))
print(printer.print_invoice(invoice))
