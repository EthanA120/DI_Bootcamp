# TASK: Geometry
import math
from random import randint


class Circle:
    """
        1. Write a class called circle that receives a radius as an argument (default is 1.0).
        2. Write two instance methods to compute perimeter and area.
        3. Write a method that prints the geometrical definition of a circle.
    """

    def __init__(self, radius=1.0):
        self.radius = radius

    def perimeter(self):
        return math.pi * 2 * self.radius

    def area(self):
        return math.pi * self.radius ** 2

    def geometry(self):
        print(f"Radius: {self.radius}\n"
              f"Perimeter: {round(self.perimeter(), 2)}\n"
              f"area: {round(self.area(), 2)}"
              )


circ = Circle(5)
circ.geometry()


# TASK: Custom List Class
class MyList:
    """
        1. Create a class called MyList, the class should receive a list of letters.
        2. Add a method that returns the reversed list.
        3. Add a method that returns the sorted List.
        4. Bonus: Create a method that generates a second list with the same length as my list.
        The list should be constructed with random numbers. (use list Comprehension).
    """

    def __init__(self, letters):
        self.letters = letters
        self.new_list = []

    def reverse(self):
        list_reverse = self.letters.copy()
        list_reverse.reverse()
        return list_reverse

    def sort(self):
        return sorted(self.letters)

    def rand_list(self):
        self.new_list = [randint(0, 9) for letter in self.letters]
        return self.new_list


letter_list = MyList(["a", "p", "c", "g", "t", "x"])
print(letter_list.reverse())
print(letter_list.sort())
print(letter_list.rand_list())


# TASK: Restaurant Menu Manager
class MenuManager:
    """
        The purpose of this exercise is to create a restaurant menu.
        The code will allow a manager to add and delete dishes.
    
        1. Create a python file called menu_manager.py.
    
        2. Create a class called MenuManager.
    
        3. Create a method __init__ that instantiates an attribute called menu.
            The menu attributes value will be all the current dishes (list of dictionaries).
            Each dish will be stored in a dictionary where the keys are name, price,
            spice level and gluten index (boolean).
    
        Here is a list of the dishes currently on the menu:
            Soup – 10 – B - False
            Hamburger – 15 - A - True
            Salad – 18 - A - False
            French Fries – 5 - C - False
            Beef bourguignon– 25 - B - True
    
            Meaning: For the spice level:
               • A = not spicy,
               • B = a little spicy,
               • C = very spicy
               
        The dishes provided above should be the value of the menu attribute.
            1. Create a method called add_item(name, price, spice, gluten).
                This method will add new dishes to the menu.
            2. Create a method called update_item(name , price, spice, gluten).
                This method checks whether a dish is in the menu, if the dish exists then update it.
                    If not notify the manager that the dish is not in the menu.
            3. Create a method called remove_item(name).
                This method should check if the dish is in the menu,
                    if the dish exists then delete it and print the updated dictionary.
                    If not notify the manager that the dish is not in the menu.
    """

    def __init__(self, menu):
        self.menu = menu

    def add_item(self, name, price, spice, gluten):
        self.menu.append({"name": name, "price": price, "spice": spice, "gluten": gluten})
        print(self.menu)

    def update_item(self, name, price, spice, gluten):
        flag = False
        for i, dish in enumerate(self.menu):
            if name == dish["name"]:
                self.menu[i] = {"name": name, "price": price, "spice": spice, "gluten": gluten}
                flag = True

            if flag:
                print("Dear manager, the dish is not in the menu!")

        print(self.menu)

    def remove_item(self, name):
        for i, dish in enumerate(self.menu):
            if name == dish["name"]:
                self.menu.remove(dish)
            else:
                print("Dear manager, the dish is not in the menu!")
        print(self.menu)


my_menu = MenuManager([
    {"name": "Soup", "price": 10, "spice": "B", "gluten": False},
    {"name": "Hamburger", "price": 15, "spice": "A", "gluten": True},
    {"name": "Salad", "price": 18, "spice": "A", "gluten": False},
    {"name": "French Fries", "price": 5, "spice": "C", "gluten": False},
    {"name": "Beef bourguignon Fries", "price": 25, "spice": "B", "gluten": True}
])

my_menu.add_item("dish", 11, "C", True)
my_menu.update_item("dish", 12, "B", False)
my_menu.remove_item("dish")
