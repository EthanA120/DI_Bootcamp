# TASK: Cats
class Cat:
    """
        class Cat:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        1. Instantiate three cat objects using the code provided above.

        2. Outside the class, create a function that finds the oldest cat and returns the cat.

        3. Print the following string: "The oldest cat is <cat_name>, and is <cat_age> years old".
            Use the function previously created.
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age


def oldest_cat(cat_list):
    oldest = Cat("oldest", 0)
    for cat in cat_list:
        if oldest.age < cat.age:
            oldest = cat

    return oldest.name, oldest.age


fury = Cat("Fury", 5)
fuzzy = Cat("Fuzzy", 2)
hazy = Cat("Hazy", 3)
cat_name, cat_age = oldest_cat([fury, fuzzy, hazy])

print(f"The oldest cat is {cat_name}, and is {cat_age} years old")


# TASK: Dogs
class Dog:
    """
        1. Create a class called Dog.

        2. In this class, create an __init__ method that takes two parameters: name and height.
            This function instantiates two attributes, which values are the parameters.

        3. Create a method called bark that prints the following string "{dog_name} goes woof!".

        4. Create a method called jump that prints the following string "{dog_name} jumps x> cm high!".
            x is the height *2.

        5. Outside the class, create an object called davids_dog. His dog's name is davids_dog and his height is 50cm.

        6. Print the details of his dog (i.e. name and height) and call the methods bark and jump.

        7. Create an object called sarahs_dog. Her dog's name is "Teacup" and his height is 20cm.

        8. Print details of her dog (i.e. name and height) and call the methods bark and jump.

        9. Create an if statement outside the class to check which dog is bigger. Print the name of the bigger dog.
    """

    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

    def get_info(self):
        print(f"Name: {self.name}\nHeight: {self.height}cm")


davids_dog = Dog("Rex", 50)
davids_dog.get_info()
davids_dog.bark()
davids_dog.jump()
print()

sarahs_dog = Dog("Teacup", 20)
sarahs_dog.get_info()
sarahs_dog.bark()
sarahs_dog.jump()
print()

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger than {sarahs_dog.name}\n")
else:
    print(f"{sarahs_dog.name} is bigger than {davids_dog.name}\n")


# TASK: Who’s the song producer?
class Song:
    """
        1. Define a class called Song, it will show the lyrics of a song.
            Its __init__ method should have two arguments: self and lyrics (a list).

        2. Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.

        3. Create an object, for example:
            stairway = Song([
                "There’s a lady whose sure",
                "all that glitters is gold",
                "and she’s buying a stairway to heaven"
                ])

        4. Then, call the sing_me_a_song method. The output should be:
            There’s a lady who's sure
            all that glitters is gold
            and she’s buying a stairway to heaven
    """

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        [print(line) for line in self.lyrics]


stairway = Song([
    "There’s a lady whose sure",
    "all that glitters is gold",
    "and she’s buying a stairway to heaven"
])
stairway.sing_me_a_song()
print()


# TASK: Afternoon at the Zoo
class Zoo:
    """
        1. Create a class called Zoo.

        2. In this class create a method_init_ that takes one parameter: zoo_name.
            It instantiates two attributes: animals (an empty list) and name (name of the zoo).

        3. Create a method called add_animal that takes one parameter new_animal.
            This method adds the new_animal to the animals list as long as it isn't already in the list.

        4. Create a method called get_animals that prints all the animals of the zoo.

        5. Create a method called sell_animal that takes one parameter animal_sold.
            This method removes the animal from the list and of course the animal needs to exist in the list.

        6. Create a method called sort_animals that sorts the animals and groups them together based on their first letter.
            Example:
            {
                1: "Ape",
                2: ["Baboon", "Bear"],
                3: ['Cat', 'Cougar'],
                4: ['Eel', 'Emu']
            }

        7. Create a method called get_groups that prints the animal/animals inside each group.

        8. Create an object called ramat_gan_safari and call all the methods.
            Tip: The zookeeper is the one who will use this class.
            Example:
                Which animal should we add to the zoo --> Giraffe
                x.add_animal(Giraffe)
    """

    def __init__(self, zoo_name, animals=[]):
        self.zoo_name = zoo_name
        self.animals = ["Cougar", "Cat", "Bear", "Eel", "Baboon", "Ape", "Emu"]
        self.groups = {}

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        [print(animal) for animal in self.animals]

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print()

    def sort_animals(self):
        alpha = sorted(list({animal[0] for animal in self.animals}))
        for letter in alpha:
            self.groups[letter] = []
            for animal in self.animals:
                if animal[0] == letter:
                    self.groups[letter].append(animal)

    def get_groups(self):
        [print(key+": ", group) for key, group in self.groups.items()]


ramat_gan_safari = Zoo("ramat_gan_safari")
ramat_gan_safari.add_animal("Lama")
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal("Cat")
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()
