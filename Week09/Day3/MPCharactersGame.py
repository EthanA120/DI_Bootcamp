# TASK: Characters game (Gleb Omarov's code)
"""
    Description:
    Create a class called Character with the following attributes and methods:
    - name
    - life – starts with a default value of 20
    - attack – the base attack of a character (integer) will be a default of 10
    - basic_attack() - accepts another character as a parameter and will <attack> the character,
        and the characters <life> points should drop.

    Instructions:
    1. Now create 3 different classes that inherit from Character:
        Every character type should say (ie. print) something when they are created, get creative :)
            1. Druid:
                - meditate() - increase life by 10, decrease attack by 2
                - animal_help()- increase attack by 5
                - fight() - accepts another character as a parameter and subtracts (0.75*life + 0.75*attack)
                    from the other characters life.
                - Example:
                - druid.fight(other_char): other_char.life - (0.75*self.life + 0.75*self.attack)

            2. Warrior:
                - brawl() - accepts another character as a parameter,
                    subtacts (2*attack) to the other characters life and adds (0.5*attack) to his own life.
                - train() - increase both your attack and life points by 2.
                - roar() - accepts another character as a parameter and subtracts their attack points by 3.

            3. Mage:
                - curse() – accepts another character as a parameter and subtracts their attack points by 2.
                - summon() - increases attack attribute by 3 points.
                - cast_spell() - accepts another character as a parameter and subtracts attack/life to the other
                    characters' life points (eg if your attack is 20 and life is 5 you will subtract 4 life points).

    2. Once all your classes are created start testing them, create one of each character and use each of their methods.
"""


class Character:
    def __init__(self, name, life=20, attack=10):
        self.name = name
        self.life = life
        self.attack = attack

    def basic_attack(self, other):
        other.life -= self.attack

    @staticmethod
    def turn_results(char1, char2):
        print(f"Result:\n\t{char1.name}'s life - {char1.life}\n\t{char2.name}'s life - {char2.life}")


class Druid(Character):
    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print(f"Wood whispers: Druid {self.name} has been created.")

    def meditate(self):
        self.attack -= 2
        self.life += 5
        print(f"{self.name} meditates. His life rises to {self.life} and attack power goes {self.attack}.")

    def animal_help(self):
        self.attack += 5
        print(f"{self.name} calls out to the animals. His attack power goes {self.attack}.")

    def fight(self, other_character):
        other_character.life -= 0.75 * (self.attack + self.life)
        print(f"{self.name} attacks to {other_character.name}")
        Character.turn_results(self, other_character)


class Warrior(Character):
    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print(f"Mountains yell: Warrior {self.name} was born!")

    def brawl(self, other_character):
        other_character.life -= 2 * self.attack
        self.life += 0.5 * self.attack
        print(f"{self.name} brawls with {other_character.name}")
        Character.turn_results(self, other_character)

    def train(self):
        self.attack += 2
        self.life += 2
        print(f"{self.name} trains. His life rises to {self.life} and attack power goes to {self.attack}.")

    def roar(self, other_character):
        other_character.attack -= 3
        print(
            f"{self.name} roars on {other_character.name}. {other_character.name}'s attack now {other_character.attack}")


class Mage(Character):
    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print(f"Sky sings: Mage {self.name} comes in this world!")

    def curse(self, other_character):
        other_character.attack -= 2
        print(
            f"{self.name} curses at {other_character.name}. {other_character.name}'s attack now {other_character.attack}")

    def summon(self):
        self.attack += 3
        print(f"{self.name} summons the power of the spirit. His attack power rises to {self.attack}.")

    def cast_spell(self, other_character):
        other_character.life -= self.attack / self.life
        print(f"{self.name} casts spell on {other_character.name}")
        Character.turn_results(self, other_character)
