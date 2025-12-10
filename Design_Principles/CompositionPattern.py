class Component:
    def show(self, indent=0):
        pass

class File(Component):
    def __init__(self, name):
        self.name = name
    
    def show(self, indent=0):
        print("  " * indent + f"- File: {self.name}")

class Folder(Component):
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def add(self, component):
        self.children.append(component)
    
    def show(self, indent=0):
        print("  " * indent + f"+ Folder: {self.name}")
        for child in self.children:
            child.show(indent + 1)

# Test
root = Folder("root")
file1 = File("file1.txt")
sub = Folder("subfolder")
file2 = File("file2.txt")

root.add(file1)
root.add(sub)
sub.add(file2)
root.show()