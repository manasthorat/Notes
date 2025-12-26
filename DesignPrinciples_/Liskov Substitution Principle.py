class Vehicle:
    def speed(self):
        return 0


class Car(Vehicle):
    def speed(self):
        return 120


class Bike(Vehicle):
    def speed(self):
        return 80


def show_speed(vehicle: Vehicle):
    return vehicle.speed()


print(show_speed(Car()))
print(show_speed(Bike()))
