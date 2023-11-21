# Poliformism

class Man:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(f"This is {self.name}, he's {self.age}, now he sleepin'")

max = Man("Max", 26)


class Woman:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(f"This is {self.name}, he's {self.age}, now she sleepin'")

anna = Woman("Anna", 25)


peoples = (anna, max)

for people in peoples:
    print(people.sleep())


# Incapsulation

class EncapExamples:

    def __init__(self):
        self.pub_atr = "Public atribute"
        self._prot_atr = "Protected atribute"
        self.__priv_atr = "Private atribute"

    def public_method(self):
        print("This is public method")

    def protect_method(self):
        print("This is protect method")

    def private_method(self):
        print("This is private method")

    def access_private_attribute(self):
        return self.__private_attribute

example = EncapExamples()

print(example.pub_atr, example.public_method())
print(example._prot_atr, example.protect_method())
print(example.access_priv_atr, example.private_method())