class OldPrinter:
    def print_old(self, text):
        return f"[Old] {text}"

class NewPrinter:
    def print_new(self, text):
        return f"[New] {text}"

class PrinterAdapter:
    def __init__(self, old_printer):
        self.old_printer = old_printer
    
    def print_new(self, text):
        return self.old_printer.print_old(text)

# Test
old = OldPrinter()
adapter = PrinterAdapter(old)
print(adapter.print_new("Hello"))  # [Old] Hello