from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def get_value(self):
        pass

class Car(Vehicle):
    def __init__(self, make, model, fare):
        self.make = make
        self.model = model
        self.fare = fare

    def get_value(self):
        return 1000*self.fare

# myObj = Car("Tesla", 2019, 40)
# print(myObj.get_value())

class TextReaderAbstract(ABC):
    def __init__(self, path, filename):
        self.path = path
        self.filename = filename

    @abstractmethod
    def get_path(self):
        pass

    @abstractmethod
    def get_filename(self):
        pass

class TextReader(TextReaderAbstract):
    def get_path(self):
        return self.path
    
    def get_filename(self):
        return self.filename
    
myObj = TextReader("/user/download", "sample.txt")

# print(myObj.get_path())

class Bank(ABC):

    @abstractmethod
    def get_interest(self):
        pass

class HDFC(Bank):

    def get_interest(self):
        return 8.9
    
myObj = HDFC()
print(myObj.get_interest())