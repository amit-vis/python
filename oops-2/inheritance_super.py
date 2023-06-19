class Vehicle:
    # polymorphism
    current_year = 2023
    best_price = 1000

    def __init__(self, model, make, fuel):
        self.model = model
        self.make = make
        self.fuel = fuel

    def __private_get_Attribute(self):
        print('This is a private method')
    
    # Default function to get value
    def get_value(self):
        age = Vehicle.current_year - self.model
        print("This is the default method of the parent")
        return Vehicle.best_price * (1 / age)


class Car(Vehicle):
    def __init__(self, model, make, fuel, air_conditioning, sunroof):
        super().__init__(model, make, fuel)
        self.air_conditioning = air_conditioning
        self.sunroof = sunroof

    # Overriding Method - replaces the parent default method
    def get_value(self):
        Vehicle.best_price = 5000
        age = Vehicle.current_year - self.model
        print("This is the child override method")
        return Vehicle.best_price * (1 / age)

# myObj = Car(2019, 'Tesla', 'electric', True, True)
# print(myObj.get_value())

# myObj2 = Car(2018, 'Ford', 'Petrol', False, True)
# print(myObj2.get_value())

# Protected method

class Vehicle:
    # polymorphism
    current_year = 2023
    best_price = 1000

    def __init__(self, model, make, fuel):
        self.model = model

        # protected Attribute
        self._make = make
        self._fuel = fuel

    def __private_get_Attribute(self):
        print('This is a private method')
    
    # Default function to get value
    def _get_value(self):
        age = Vehicle.current_year - self.model
        print("This is the default method of the parent")
        return Vehicle.best_price * (1 / age)


class Car(Vehicle):
    def __init__(self, model, make, fuel, air_conditioning, sunroof):
        super().__init__(model, make, fuel)

        # protected Attribute
        self._air_conditioning = air_conditioning
        self._sunroof = sunroof

    # Overriding Method - replaces the parent default method
    def _get_value(self):
        Vehicle.best_price = 5000
        age = Vehicle.current_year - self.model
        print("This is the child override method")
        return Vehicle.best_price * (1 / age)
    
myObj = Car(2019,'Tesla', 'electric', True, True)

# print(myObj._air_conditioning)
# print(myObj._get_value())


# Object Class

class Circle(object):
    def __init__(self, radius):
        self.__radius = radius

    # def __str__(self):
    #     return "This is a circle class which takes radius as an arguments"
    
# c = Circle(3)
# print(c)

# Multilevel in herintence
# class Vehicle():
#     def __init__(self, model, make, fuel):
#         self.model = model
#         self.make = make
#         self.fuel = fuel

# class Car(Vehicle):
#     def __init__(self, model, make, fuel, air_conditioning, sunroof):
#         super(Car,self).__init__(model, make, fuel)
#         self._air_conditioning =air_conditioning
#         self._sunroof = sunroof

# class ElectricVehicle(Car):
#     def __init__(self, model, make, fuel, air_conditioning, sunroof, distance):
#         super(ElectricVehicle,self).__init__(model, make, fuel, air_conditioning, sunroof)
#         self.distance = distance

# class Vehicle:
#     def __init__(self, model, make, fuel):
#         self.model = model
#         self.make = make
#         self.fuel = fuel

# class Car(Vehicle):
#     def __init__(self, model, make, fuel, suroof, air_conditioning):
#         super(Car, self).__init__(model, make, fuel)
#         self.sunroof = suroof
#         self.air_conditioning = air_conditioning


# myObj = Car(2019,'tesla', 'electric', True, True)
# print(myObj.__dict__)

# MRO
# method resolution order

class Car():
    def __init__(self, make, model, fuel):
        self.make = make
        self.model = model
        self.fuel = fuel
    
    def get_car_details(self):
        return "the make of the car is", self.make, "from car classes"

class ElectricCar():
    def __init__(self, make, model, fuel):
        self.make = make
        self.model = model
        self.fuel = fuel
    
    def get_car_details(self):
        return "the make of the car is", self.make, "from Elecrtric car"
    
class Taxi(ElectricCar,Car):
    def __init__(self, make, model, fuel):
        super().__init__(make, model, fuel)

myObj = Taxi('Tesla', 2019, 'Electric')

# print(myObj.get_car_details())
# print(Taxi.__mro__)
# print(myObj.make)

# overload operator
class Vehicle:
    def __init__(self, make, model, fare):
        self.make = make
        self.model = model
        self.fare = fare

    def __str__(self):
        return "the make of the car is {} and the model is of {} with a fare of {}".format(self.make, self.model, self.fare)
    def __add__(self, other):
        return self.fare + other.fare
    def __sub__(self, other):
        return self.fare - other.fare
    
myObj = Vehicle('Tesla', 2019, 50)
myObj2 = Vehicle('Ford',2018, 80)

print(myObj)
print(myObj+myObj2)
print(myObj-myObj2)