# TASK: Vaccines
"""
    Vaccines management system
    Your goal is to create a program to help a city with the vaccination of its citizens.


    Part 1
    You will have to create two classes:
        - Human
        - Queue

    Here is a description of them:
    1. Human
        Represents a citizen of the city, it has the following attributes:
            id_number (str), name (str), age (int), prioritary (bool) and blood_type (str).
            Its blood type can be “A”, “B”, “AB” or “O”.

        It got no methods.

    2. Queue

    Represents a queue of humans waiting for their vaccine.
    It has two attributes, humans, the list containing the humans that are waiting,
    it is initialized empty.
    This class is useful to manage who will get vaccinated in priority. It has the following methods:
        - add_person(self, person) Add a human to the queue, if he is older than 60 years old or a prioritary person,
            put him at the beginning of the list (at index 0) before every other.
        - find_in_queue(self, person) Returns the index of a human in the queue.
        - swap(self, person1, person2) Swaps person1 with person2.
        - get_next(self) return the next human in the queue, meaning the object at index 0 in the list.
        - get_next_blood_type(self, blood_type) Return the first human with this specific blood type.
        - sort_by_age(self) Sort the queue so that the older ones are before the younger ones and all the
            priority persons are before the others.

    Every human returned by get_next and get_next_blood_type is removed from the list,
    those functions return None if there is no one in the list.

    Bonus: Don’t use any of the following built-in methods: list.insert, list.pop, list.index, list.sort, sorted.


    Part 2
    Create an attribute family for the Human class. Initialized as empty,
    family is a list of all the humans that are living in the same house with this human.
    Add a method add_family_member(self, person) that adds the person to this human’s family,
    and this human to the person’s family.

    Add the rearrange_queue(self) method to the Queue class,
    so that there is no two members of the same family one after the other.
"""


class Human:
    def __init__(self, id_number: str, name: str, age: int, priority: bool, blood_type: str, family: list = None):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority

        if blood_type in ["A", "B", "AB", "O"]:
            self.blood_type = blood_type
        else:
            print("Blood type can only be 'A', 'B', 'AB' or 'O', please insert valid blood type\n")

        if family is None:
            self.family = [self]
        else:
            if self in family:
                self.family = family
            else:
                self.family = [self] + family

            for person in family:
                if self not in person.family:
                    person.family.append(self)

                self.family.sort(key=lambda a: a.name)
                person.family.sort(key=lambda a: a.name)


    def __repr__(self):
        return self.name

    def add_family_member(self, person):
        self.family.append(person)
        person.family.append(self)
        # print(self.family)
        # print(person.family)


class Queue:
    def __init__(self, humans: list = None):
        if humans is None:
            self.humans = list()
        else:
            self.humans = humans

    def add_person(self, person: Human):
        if person.age > 60 or person.priority:
            self.humans.insert(0, person)
        else:
            self.humans.append(person)
        print(self.humans)

    def find_in_queue(self, person: Human):
        # print(self.humans.index(person))
        return self.humans.index(person)

    def swap(self, person1: Human, person2: Human):
        index1 = self.find_in_queue(person1)
        index2 = self.find_in_queue(person2)
        self.humans[index1], self.humans[index2] = self.humans[index2], self.humans[index1]
        # print(self.humans)

    def get_next(self):
        return self.humans.pop(0)

    def get_next_blood_type(self, blood_type):
        for human in self.humans:
            if human.blood_type == blood_type:
                return self.humans.pop(self.find_in_queue(human))

    def sort_by_age(self):
        self.humans.sort(key=lambda a: a.age, reverse=True)
        # print(self.humans)
        self.humans.sort(key=lambda a: a.priority, reverse=True)
        print(self.humans)

    def rearrange_queue(self):
        i = 1
        counter = 0
        while i < len(self.humans) and counter <= len(self.humans):
            if self.humans[i-1].family == self.humans[i].family:
                self.humans[i-1], self.humans[i] = self.humans[i], self.humans[i-1]
                i = 1
            else:
                i += 1
            counter += 1

        print(self.humans)


ethan = Human(id_number="123", name="Ethan", age=28, priority=False, blood_type="AB")
adir = Human(id_number="456", name="Adir", age=21, priority=False, blood_type="B", family=[ethan])
asher = Human(id_number="789", name="Asher", age=65, priority=False, blood_type="A", family=[ethan, adir])
ora = Human(id_number="147", name="Ora", age=65, priority=True, blood_type="AB")

ethan.add_family_member(adir)
# print(ethan.family)
# print(adir.family)
# print(asher.family)
# print(ora.family)

queue = Queue([ethan, adir, asher, ora])
print(queue.humans)
queue.add_person(ethan)
print(queue.find_in_queue(asher))
queue.swap(ethan, adir)
print(queue.get_next())
print(queue.humans)
print(queue.get_next_blood_type("A"))
queue.sort_by_age()
queue.rearrange_queue()
