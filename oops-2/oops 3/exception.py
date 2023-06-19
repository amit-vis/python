# class Vehicle():
#     def __init__(self, make, model, fuel):
#         self.make = make
#         self.model = model
#         self.fuel = fuel

#     def get_value(self):
#         try:
#             age = 2021-self.model
#             return 1000*(1/age)
#         except:
#             try:
#                 age = 2021-int(self.model)
#                 return 1000*(1/age)
#             except ZeroDivisionError:
#                 age = 2021 - int(self.model)
#                 return 1000*(1)
#             except:
#                 return "Kindly mentioned the model in correct format"
        


# # print(myObj.get_value())

# class NegativeCarValue(Exception):
#     def __init__(self, value, message = "Car value not be negative"):
#         self.value = value
#         self.message = message
#         super().__init__(self.message)

#     def __str__(self):
#         return f'{self.message} ------> {self.value}'
    
# # a = -1
# # if (a<0):
# #     raise NegativeCarValue(a)

# class Vehicle():
#     def __init__(self,make,model,fuel):
#         self.make = make
#         self.model = model
#         self.fuel = fuel
#         self.current_year = 2021

#     def get_value(self):
#         age = self.current_year - self.model
#         try:
#             if(age<0):
#                 return NegativeCarValue(age)
#             else:
#                 return 1000*(1/age)
#         except NegativeCarValue as e:
#             print('Error****',e)
        

# myObj = Vehicle('Tesla', 2023, 'electric')

# myObj.get_value()
class NegativeZeroModelYear(Exception):
    def __init__(self, value, message = "Model Year can not be equal or greater then 2021"):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message} -----> {self.value}'
    
class CarModelYearAnString(Exception):
    def __init__(self, value, message="Car Value is in not an string"):
        self.value = value
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f'{self.message} -------> {self.value}'
    
class Vehicle():
    def __init__(self, make, model,fuel):
        self.make = make
        self.model = model
        self.fuel = fuel
        self.current_year = 2021
        self.value = None

    def get_value(self):
        try:
            if self.model == str:
                status = "custom"
                raise CarModelYearAnString(self.model)
            elif self.model >= self.current_year:
                status = "custom"
                raise NegativeZeroModelYear(self.model)
            else:
                self.age = self.current_year - self.model
                self.value = 1000 * (1/self.age)
                status = "success"
        except TypeError:
            self.age = self.current_year - int(self.model)
            self.value = 1000*(1/self.age)
            status = "inbuilt"
        else:
            print("code ran without any exception")
        finally:
            if status == "custom":
                print("code has custom exception please rectify this")
            elif status == "inbuilt":
                print("code has inbuilt exception, please rectify this")

            else:
                print("print the value without any exception - ", self.value)

myObj = Vehicle('Tesla', 2023, 'electric')

print(myObj.get_value())
        
