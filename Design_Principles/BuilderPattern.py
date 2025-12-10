class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
    
    def __str__(self):
        return f"Computer: CPU={self.cpu}, RAM={self.ram}GB, Storage={self.storage}GB"

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()
    
    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self
    
    def set_ram(self, ram):
        self.computer.ram = ram
        return self
    
    def set_storage(self, storage):
        self.computer.storage = storage
        return self
    
    def build(self):
        return self.computer

# Test
pc = ComputerBuilder().set_cpu("Intel i7").set_ram(16).set_storage(512).build()
print(pc)