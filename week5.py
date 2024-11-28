# **Assignment 1: Design Your Own Class (Smartphone and Smartwatch)**

class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Battery Life: {self.battery_life} hours")

    def charge(self):
        print(f"Charging the {self.model}...")

# Inheritance: Smartwatch class that extends Smartphone
class Smartwatch(Smartphone):
    def __init__(self, brand, model, battery_life, strap_material):
        super().__init__(brand, model, battery_life)
        self.strap_material = strap_material  # Additional attribute

    def display_info(self):
        super().display_info()  # Call the parent class method
        print(f"Strap Material: {self.strap_material}")

    def charge(self):
        print(f"Charging the {self.model} smartwatch...")

# Create an instance of Smartphone
phone = Smartphone("Apple", "iPhone 14", 20)
print("\nSmartphone Info:")
phone.display_info()
phone.charge()

# Create an instance of Smartwatch
watch = Smartwatch("Apple", "Apple Watch Series 8", 18, "Silicone")
print("\nSmartwatch Info:")
watch.display_info()
watch.charge()


# **Activity 2: Polymorphism Challenge (Vehicles with Different move() Methods)**

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method!")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Creating instances of each vehicle
car = Car()
plane = Plane()
boat = Boat()

# Calling the move method for each class
print("\nVehicle Movement Actions:")
