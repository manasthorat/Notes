class Coffee:
    def cost(self):
        return 5
    def description(self):
        return "Coffee"

class Milk:
    def __init__(self, coffee):
        self.coffee = coffee
    
    def cost(self):
        return self.coffee.cost() + 2
    
    def description(self):
        return self.coffee.description() + " + Milk"

class Sugar:
    def __init__(self, coffee):
        self.coffee = coffee
    
    def cost(self):
        return self.coffee.cost() + 1
    
    def description(self):
        return self.coffee.description() + " + Sugar"

# Test
drink = Coffee()
drink = Milk(drink)
drink = Sugar(drink)
print(f"{drink.description()}: ${drink.cost()}")