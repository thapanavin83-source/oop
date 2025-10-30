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
class ElectricCar(Car):
    def __init__(self,license_plate, maximum_speed,battery_capacity):
        super().__init__(license_plate, maximum_speed)
        self.battery_capacity = battery_capacity
class GasolineCar(Car):
    def __init__(self,license_plate, maximum_speed,tank_volume):
        super().__init__(license_plate, maximum_speed)
        self.battery_capacity = battery_capacity
