class Flyable:
    def fly(self):
        pass


class Walkable:
    def walk(self):
        pass


class Bird(Flyable, Walkable):
    def fly(self):
        return "flying"

    def walk(self):
        return "walking"


class Dog(Walkable):
    def walk(self):
        return "walking"


print(Bird().fly())
print(Dog().walk())
