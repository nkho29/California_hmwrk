class Car:

    vin_code = "WS12D312GJKO44WFG2341"
    def __init__(self, colour):
        self.colour = colour

    def colour_method(self):
        return f"{self.colour}"

    @classmethod
    def classmethod(cls):
        return f"this is {classmethod}"

    @staticmethod
    def static_method():
        return "this is static method"


car1 = Car("Red car")

print(car1.colour_method())
print(Car.classmethod())
print(Car.static_method())