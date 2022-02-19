# TASK: Pets
"""
    Using this code:

    class Pets():
        def __init__(self, animals):
            self.animals = animals

        def walk(self):
            for animal in self.animals:
                print(animal.walk())

    class Cat():
        is_lazy = True

        def __init__(self, name, age):
            self.name = name
            self.age = age

        def walk(self):
            return f'{self.name} is just walking around'

    class Bengal(Cat):
        def sing(self, sounds):
            return f'{sounds}'

    class Chartreux(Cat):
        def sing(self, sounds):
            return f'{sounds}'


        1. Create another cat breed. In order to do so, create a class which inherits from the Cat class.
        2. Create a few cat instances.
        3. Create a list called my_cats, which will hold all the created cat instances.
        4. Create a variable called my_pets. Its value is an instance of the Pet class.
            Hint : Use the my_cats variable to create the instance.
        5. Take all the cats for a walk, use the walk method.
"""


class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Tabby(Cat):
    pass


simba = Bengal("Simba", 2)
mufasa = Tabby("Mufasa", 7)
sarabi = Chartreux("Sarabi", 6)
my_cats = [simba, mufasa, sarabi]

[print(cat.walk()) for cat in my_cats]
print()


# TASK: Dogs
class Dog:
    """

        1. Create a class called Dog with the following attributes name, age, weight.
        2. Implement the following methods in the Dog class:
            - bark: returns a string which states: “<dog_name> is barking”.
            - run_speed: returns the dogs running speed (weight/age*10).
            - fight: takes a parameter which value should be another dog called other_dog,
                returns a string stating which dog won the fight.
                The winner should be the dog with the higher run_speed x weight.

        3. Create 3 dogs and run them through your class.
    """

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            print(f"{self.name} won the fight")
        else:
            print(f"{other_dog.name} won the fight")


tramp = Dog("Tramp", 5, 18)
jock = Dog("Jock", 4, 15)
trusty = Dog("Trusty", 5, 14)

print(tramp.bark())
print(jock.run_speed())
trusty.fight(jock)
print()


# TASK: Dogs Domesticated
# from XP import Dog
from random import choice


class PetDog(Dog):
    """
        1. Create a new python file and import your Dog class from the previous exercise.
        2. In the new python file, create a class named PetDog that inherits from Dog.
        3. Add an attribute called trained to the __init__ method,
            this attribute is a boolean and the value should be False by default.
        4. Add the following methods:
            - train: prints the output of bark and switches the trained boolean to True

            - play: takes a parameter which value is a few names of other dogs (use *args).
                The method should print the following string: “dog_names all play together”.

            - do_a_trick: If the dog is trained the method should print one of the following sentences at random:
                + “dog_name does a barrel roll”.
                + “dog_name stands on his back legs”.
                + “dog_name shakes your hand”.
                + “dog_name plays dead”.
    """

    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dog_names = ", ".join(dog.name for dog in args)
        print(f"{dog_names}, all play together")

    def do_a_trick(self):
        some_list = [
            "does a barrel roll",
            "stands on his back legs",
            "shakes your hand",
            "plays dead"
        ]

        if self.trained:
            print(f"{self.name} {choice(some_list)}")


# tramp = Dog("Tramp", 5, 18)
# jock = Dog("Jock", 4, 15)
# trusty = Dog("Trusty", 5, 14)

lady = PetDog("Lady", 4, 12)

lady.train()
lady.play(tramp, jock, trusty)
lady.do_a_trick()
