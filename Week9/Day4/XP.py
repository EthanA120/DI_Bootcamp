# TASK:
class Human:
    """
        Create a class Human, it has the following attributes:
            - name (str)
            - age (int)
            - living_place (Building - Default is None)

        Create another class Building, it has the following attributes:
            - address (str)
            - inhabitants (List of Human objs - Default is empty)

        Create a class City, it has the following attributes:
            - name (str)
            - buildings (List of Building objs - Default is empty)

        Add the move(self, building) method to the Human class,
        it sets the living place of this human to the building and add this human to the building inhabitants.
        Add the construct(self, address) method to the City class, it adds a building at the referenced address.
        Add the info(self, address) method to the City class,
        it displays the number of buildings and the mean age of the citizens.
    """

    def __init__(self, name, age, living_place=None):
        self.name = name
        self.age = age
        self.living_place = living_place

    def __repr__(self):
        return self.name

    def move(self, building):
        self.living_place = building.address
        building.inhabitants.append(self)
        print(f"{self} is now live in {building}\n")


class Building:
    def __init__(self, address, inhabitants=None):
        self.address = address
        if inhabitants is None:
            self.inhabitants = []
        else:
            self.inhabitants = inhabitants

    def __repr__(self):
        return self.address


class City:
    def __init__(self, name, buildings=None):
        self.name = name
        if buildings is None:
            self.buildings = []
        else:
            self.buildings = buildings

    def __repr__(self):
        return self.name

    def construct(self, address):
        self.buildings.append(address)
        print(f"{address} is now built in {self}")

    def info(self, address):
        print(f"Amount of buildings in the city: {len(self.buildings)}\n"
              f"Mean age of the citizens: "
              f"{sum([inhabitant.age for inhabitant in address.inhabitants]) / len(address.inhabitants)}")


ethan = Human("Ethan", 28, "Netivot")
adir = Human("Adir", 26, "Netivot")

sderot = City("Sderot")
hyg = Building("Yahalom")
sderot.construct(hyg)

ethan.move(hyg)
adir.move(hyg)
sderot.info(hyg)
