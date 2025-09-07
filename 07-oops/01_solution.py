class Car:

    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

        Car.total_car  += 1

    def get_brand(self):
        return self.__brand   
    
    def full_name(self):
        return f"{self.__brand},{self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def generale_description():
        return "Cars are means to move you!"
    
    @property
    def model(self):
        return self.__model


class Electric_cars(Car):
    def __init__(self, brand, model,bettery_size):
        super().__init__(brand, model)
        self.bettery_size = bettery_size


    def fuel_type(self):
        return "Electric charge"


my_electric_car = Electric_cars("MG", 'PHev', "90kWh")
print(my_electric_car.full_name())
print(my_electric_car.bettery_size)

my_car = Car("KIA", "Stonic")
my_new_car = Car("Suzuki", "Caltus")

# print(isinstance(my_car, Electric_cars))
# print(isinstance(my_car, Car))
# print(isinstance(my_electric_car, Car))
# print(isinstance(my_new_car, Car))


# print(my_car.get_brand())
# print(my_electric_car.fuel_type())
# print(my_car.fuel_type())

# print(Car.total_car)
# print(Car.generale_description())
# # my_car.model = "City"
# print(my_car.model)



# print(my_car.brand, my_car.model)
# print(my_car.full_name())
# print(my_new_car.model, my_new_car.brand)


class Bettery:
    def bettery_info(self):
        return "This is bettery"
        

class Engin:
    def engin_info(self):
        return "This is engin"

class NewElectricCar(Bettery, Engin, Car):
    pass


my_new_tesla = NewElectricCar("Tesla", "Model R")
print(my_new_tesla.bettery_info())
print(my_new_tesla.engin_info())