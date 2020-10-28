class Car:
    def __init__ (self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on")
    def update_odometer(self, milage):
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can't roll back an odometer!")
    def increase_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make,model,year)
        self.battery = Battery()
    def describe_batery(self):
        print(f"This car jas a {self.battery_size} KWh battery")
    def fill_gas_tank(self):
        print("This car doesnt need a gas tank!")


class Battery:
    def __init__(self, battery_size = 75):
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-KWh battery")
    def get_range(self):
        if self.battery_size == 75:
            range = 260
            print(f"This car can go about {range} miles on a full charge") 
        elif self.battery_size == 100:
            range = 315
            print(f"This car can go about {range} miles on a full charge") 


my_used_car = Car("subaru", "outback", "2015")
my_used_car.update_odometer(200)
print(f"{my_used_car.get_descriptive_name()} with {my_used_car.odometer_reading} miles on")

my_tesla = ElectricCar("tesla", "4G", "2019")
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range() 