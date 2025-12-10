class Book:
    def __init__(self, price):
        self.price = price
    
    def accept(self, visitor):
        return visitor.visit_book(self)

class Fruit:
    def __init__(self, weight, price_per_kg):
        self.weight = weight
        self.price_per_kg = price_per_kg
    
    def accept(self, visitor):
        return visitor.visit_fruit(self)

class PriceCalculator:
    def visit_book(self, book):
        return book.price
    
    def visit_fruit(self, fruit):
        return fruit.weight * fruit.price_per_kg

# Test
items = [Book(20), Fruit(2, 5), Book(15)]
calc = PriceCalculator()
total = sum(item.accept(calc) for item in items)
print(f"Total: ${total}")  # 45