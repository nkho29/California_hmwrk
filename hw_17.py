class Animal:

    def __init__(self, eat, name, color):
        self.eat = eat
        self.name = name
        self.color = color

    def animal_info(self):
        print(f"This is {self.color} {self.name}")

    def eatin_food(self):
        print(f"{self.color} {self.name} eatin {self.eat}")


animal1 = Animal(name="car", color="orange", eat="fish")

print(animal1.animal_info())
print(animal1.eatin_food())


class Lil_Animal(Animal):

    def __init__(self, eat, name, color, legs):
        self.legs = legs
        Animal.__init__(self, name, eat, color)


    def other_animal_info(self):
        print(f"this is {self.color} {self.name} he has {self.legs} legs, and loves eat {self.eat}")


animal2 = Lil_Animal("fish", "cat", "orange", 4)
print(animal2.other_animal_info())


print(Lil_Animal.__base__)


class Another_animal(Lil_Animal):

    def __init__(self, eat, name, color, legs, act):
        self.act = act
        Lil_Animal.__init__(self,  eat, name, color, legs)

    def another_animal_act(self):
        print(f"This is {self.color} {self.name}, he has {self.legs} legs, he loves eatin {self.eat} fish n he loves {self.act}")


animal3 = Another_animal( "fish", "cat", "orange", 4, "runin")
print(animal3.another_animal_act())

print(type(animal3))
