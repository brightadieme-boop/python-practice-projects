class Car:
    """A simple attempt to represent a car"""
    def __init__(self,make,model,year):
        """Initialize attribute to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 23
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        car_details = f"{self.year} {self.model} {self.make}"
        return car_details.title()
    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} mile on it")

my_new_car = Car('2024','a4','toyota')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()