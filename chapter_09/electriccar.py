# filepath: /c:/Users/rouss/OneDrive/Desktop/code-college/python/my-code/chapter_09/electriccar.py
from car import Car as ParentClass
from battery import Battery as SmallerVariable

class ElectricCar(ParentClass):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = SmallerVariable()

    def fill_gas_tank(self):
        print("This car does not take gas.")

# Create an instance of ElectricCar
my_tesla = ElectricCar('tesla', 'model s', 2020)

# Call methods on the instance
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()