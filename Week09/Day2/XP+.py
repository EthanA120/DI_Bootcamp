# TASK: Family
class Family:
    """
        1. Create a class called Family and implement the following attributes:
            - members: list of dictionaries with the following keys: name, age, gender and is_child (boolean).
            - last_name : (string)

        Initial members' data:
            [
                {'name':'Michael','age':35,'gender':'Male','is_child':False},
                {'name':'Sarah','age':32,'gender':'Female','is_child':False}
            ]

        2. Implement the following methods:
            - born: adds a child to the members list (use **kwargs),
                don’t forget to print a message congratulating the family.
            - is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
            - a method that prints all the members of the family.
    """

    def __init__(self):
        self.members = {
            'Michael': {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
            'Sarah': {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
        }

    def born(self, **kwargs):
        self.members[kwargs["name"]] = kwargs

    def is_18(self, member_name):
        if member_name in self.members:
            if self.members[member_name]['age'] >= 18:
                return True
            elif self.members[member_name]['age'] < 18:
                return False
        else:
            print("Not such name in this family")


family = Family()
family.born(name="Rony", age=10, gender="Male")
family.members["Rony"].update({"is_child": family.is_18("Rony")})


# TASK: The Incredibles Family
class TheIncredibles(Family):
    """
        1. Create a class called TheIncredibles. This class should inherit from the Family class:
            - This is no random family they are an incredible family,
            therefore we need to add the following keys to our dictionaries: power and incredible_name.

            - Add a method called use_power, this method should print the power of a member if they are over 18 years old.
                If not raise an exception (look up exceptions) which stated they are not over 18 years old.

            - Add a method called incredible_presentation which presents the family members with their incredible names and powers.

        Look up the names of The Incredibles characters on Google and build the family
            (if you can’t find the correct information just improvise).
        Print their normal presentation and their incredible presentation.
        Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.
        Print both presentations again.
        Check that Baby Jack is born and that his power is showing when using the incredible representation.
    """
    def __init__(self):
        super(TheIncredibles, self).__init__()

    def use_power(self, member_name):
        try:
            if self.is_18(member_name):
                print(f"{member_name} use {self.members[member_name]['power']}")
            else:
                raise ValueError()
        except ValueError:
            print("this member is not over 18 years old yet")

    def incredible_presentation(self):
        for member in self.members.keys():
            if "power" in self.members[member].keys():
                print(f"{self.members[member]['presentation']} have {self.members[member]['power']} power")


incredible_family = TheIncredibles()
incredible_family.born(name="Bob", age=40, gender="Male", is_child=False,
                       power="Superhuman strength and invulnerability", presentation="Mr. Incredible")
incredible_family.born(name="Helen", age=38, gender="Female", is_child=False,
                       power="Elasticity, Shapeshifting and Picnokinesis (Density manipulation)", presentation="Elastigirl")
incredible_family.born(name="Violet", age=14, gender="Female", is_child=True,
                       power="Invisibility and force-field projection", presentation="Vi")
incredible_family.born(name="Dashiell", age=10, gender="Male", is_child=True,
                       power="Superhuman speed and reflexes", presentation="Dash")
incredible_family.born(name="John", age=1, gender="Male", is_child=True,
                       power="Polymorphing, Enhanced Strength and Dexterity, Laser Vision,"
                             "Telekinesis, Levitation, Teleportation, Mégethoskinesis,"
                             "Self-Duplication, Intangibility and Wall-crawling", presentation="Jack-Jack")

incredible_family.use_power("Bob")
incredible_family.use_power("Helen")
incredible_family.use_power("Violet")
incredible_family.use_power("Dashiell")
incredible_family.use_power("John")
print()

incredible_family.incredible_presentation()
