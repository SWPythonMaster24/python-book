from car import Car

class Battery:

    def __init__(self, battery_size = 40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")
        

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print("This car doesn't have a gas tank!")

#my_leaf = ElectricCar('nissan', 'leaf', 2024)
#print(my_leaf.get_descriptive_name()) # 2024 Nissan Leaf
#my_leaf.battery.describe_battery() # This car has a 40-kWh battery.
#my_leaf.fill_gas_tank() # This car doesn't have a gas tank!
#my_leaf.battery.get_range() # This car can go about 150 miles on a full charge.