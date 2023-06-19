# Parent Class
class Vehicle:
    def __init__(self, model, make, fuel):
        self.model = model
        self.make = make
        self.fuel = fuel

# child class
class car(Vehicle):
    def __init__(self, model, make, fuel, sunroof, air_conditioning):
        # parent Attribute
        Vehicle.model = model
        Vehicle.make = make
        Vehicle.fuel = fuel

        self.sunroof = sunroof
        self.air_conditioning = air_conditioning
    
    def get_Attribute(self):
        print(Vehicle.model, ' ', Vehicle.make, ' ', Vehicle.fuel)

myObj = car("Tesla", 2019, 'Electric', True, True)

# print(myObj.__dict__)
# myObj.get_Attribute()
# print(myObj.model)

# child class
class Vehicle:
    def __init__(self, model, make, fuel):
        self.model = model
        self.__make = make
        self.__fuel = fuel

    def __private_method_parent(self):
        print('This is a Private')

# child class
class car(Vehicle):
    def __init__(self, model, make, fuel, sunroof, air_conditioning):
        # parent Attribute
        Vehicle.model = model
        Vehicle.__make = make
        Vehicle.__fuel = fuel

        self.sunroof = sunroof
        self.air_conditioning = air_conditioning

    def get_Attribute(self):
        print(Vehicle.model, ' ', Vehicle.make, ' ', Vehicle.fuel)

    def get_privatemethod_from_parent(self):
        self._Vehicle__private_method_parent()

myObj = car("Tesla", 2019, 'Electric', True, True)
# myObj.get_Attribute()
print(myObj.__make)
myObj.get_privatemethod_from_parent()