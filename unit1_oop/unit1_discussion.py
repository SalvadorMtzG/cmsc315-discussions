"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class Vehicle:
    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return "This vehicle is a: " + self.make + self.model




# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class GasolineCar(Vehicle):
    transmission_type = "forward"

    def __init__(self, make, model, mpg, fuel_capacity_gal):
        super().__init__(make, model)

        self.mpg = mpg
        self.fuel_capacity_gal = fuel_capacity_gal

    def refuel(self):
        return "This vehicle needs " + str(self.fuel_capacity_gal) + "gallons"

    def get_info(self):
        return "This vehicle is a: " + self.make + " " + self.model + " that does " + str(self.mpg) + "mpg, and has a " + self.transmission_type + " transmission"

# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    print("TODO: Implement namespace demonstration")

    car1 = GasolineCar("Ford", "Explorer", 20, 18.6)
    car2 = GasolineCar("GMC", "Sierra", 14, 34)

    print("Wheels variable through class: ", GasolineCar.wheels)
    print("Wheels variable through object: ", car1.wheels)

    car2.color = "White"

    print(car1.__dict__)
    print(car2.__dict__)

    print(GasolineCar.__dict__)

# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    print("TODO: Implement shallow copy and deep copy demonstration")

    car3 = GasolineCar("Dodge", "Charger", 17, 17.5)
    car3.engines = ["v4", "v6", "v8"]

    shallow_copy = copy(car3)
    deep_copy = deepcopy(car3)

    print("Original list: ", car3.engines)
    car3.engines[0] = "v10"

    print("The element in the shallow copy changes when it is modified in the original object")
    print("Change made: car3.engines[0] = 'v10'")
    print("Original list: ", car3.engines)
    print("Shallow copy: ", shallow_copy.engines)

    print("The deep copy remained unaffected by the change in the original object")
    print("Deep copy: ", deep_copy.engines)

    #Shallow copies still reference the original nested objects while Deep copies create independent copies

# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\nTODO: Create and test your parent object")
    vehicle = Vehicle("Massey Ferguson", "1M.35")
    print(vehicle.get_info())

    print("\nTODO: Create and test your child object")
    car4 = GasolineCar("Mitsubishi", "Eclipse", 23, 16.9)
    print(car4.get_info())

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()