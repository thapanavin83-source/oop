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

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"\nRace: {self.name}")
        print(f"{'License Plate':<15}{'Max Speed':<12}{'Current Speed':<15}{'Distance (km)':<15}")
        print("-" * 57)
        for car in self.cars:
            print(f"{car.license_plate:<15}{car.maximum_speed:<12}{car.current_speed:<15}{car.travelled_distance:<15.1f}")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False