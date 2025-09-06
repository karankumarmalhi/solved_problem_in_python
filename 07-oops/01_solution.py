class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


my_car = Car("KIA", "Stonic")
my_new_car = Car("Suzuki", "Caltus")

print(my_car.brand, my_car.model)
print(my_new_car.model, my_new_car.brand)