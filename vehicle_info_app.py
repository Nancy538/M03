#Author: Nancy
#File Name: vehicle_info_app.py
#This program prompts the user for car details, stores them in an Automobile object,and then displays the information in a readable format.

#Variables:year (str): The manufacturing year of the car.
#make (str): The brand of the car.
#model (str): The specific model of the car.
#doors (str): The number of doors (2 or 4).
#roof (str): The type of roof (solid or sun roof).

class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__("car")  # Vehicle type is always "car"
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")

# User input
year = input("Enter the year of the car: ")
make = input("Enter the make of the car: ")
model = input("Enter the model of the car: ")
doors = input("Enter the number of doors (2 or 4): ")
roof = input("Enter the type of roof (solid or sun roof): ")

# Create an Automobile instance
car = Automobile(year, make, model, doors, roof)

# Display the car information
print("\nCar Details:")
car.display_info()