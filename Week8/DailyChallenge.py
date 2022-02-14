# TASK: Old MacDonald’s Farm

class Farm:
    """
        Take a look at the following code and output!

        File: market.py

        macdonald = Farm("McDonald")
        macdonald.add_animal('cow',5)
        macdonald.add_animal('sheep')
        macdonald.add_animal('sheep')
        macdonald.add_animal('goat', 12)
        print(macdonald.get_info())

        Output

        McDonald's farm

        cow: 5
        sheep: 2
        goat: 12

        E-I-E-I-0!


        Create the code that is needed to recreate the code provided above.
        Below are a few questions to assist you with your code:
            1. Create a class called Farm. How should this be implemented?


            2. Does the Farm class need an __init__ method? If so, what parameters should it take?


            3. How many methods does the Farm class need?


            4. Do you notice anything interesting about the way we are calling the add_animal method?
                What parameters should this function have? How many…?


            5. Test your code and make sure you get the same results as the example above.


            6. Bonus: nicely line the text in columns as seen in the example above. Use string formatting.


            Expand The Farm:

                Add a method called get_animal_types to the Farm class.
                This method should return a sorted list of all the animal types (names) in the farm.
                With the example above, the list should be: ['cow', 'goat', 'sheep'].

                Add another method to the Farm class called get_short_info.
                This method should return the following string: “McDonald’s farm has cows, goats and sheep.”.
                The method should call the get_animal_types function to get a list of the animals.
    """

    def __init__(self, name):
        self.name = name
        self.farm_dict = {}
        self.info = f"{self.name}'s Farm\n"

    def add_animal(self, animal, amount=1):
        try:
            self.farm_dict[animal] = self.farm_dict[animal] + amount
        except KeyError:
            self.farm_dict[animal] = amount

    def get_info(self):
        self.info += "\n".join(key+": " + str(value) for key, value in self.farm_dict.items())
        self.info += "\nE-I-E-I-0!"
        return self.info

    def get_animal_types(self):
        return sorted(list(self.farm_dict.keys()))

    def get_short_info(self):
        animal_list = self.get_animal_types()
        return f"{self.name}'s farm has {','.join(animal_list[0:-2])} and {animal_list[-1]}"


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_short_info())
