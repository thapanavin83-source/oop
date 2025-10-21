class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

def race(sort_results=True):
    import random

    cars = [Car(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]

    while True:
        for car in cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)
            if car.travelled_distance >= 10000:
                if sort_results:
                    return sorted(cars, key=lambda c: c.travelled_distance, reverse=True)
                else:
                    return cars