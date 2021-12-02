from pizza_maker.dough import Dough
from pizza_maker.topping import Topping


class Pizza:
    def __init__(self, name, dough: Dough, toppings_capacity: int, toppings=None):
        if toppings is None:
            toppings = {}
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = toppings

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    def add_topping(self, topping: Topping):
        if len(self.toppings) == self.toppings_capacity:
            raise ValueError("Not enough space for another topping")
        if topping.topping_type in self.toppings:
            self.toppings[topping.topping_type] += topping.weight
        else:
            self.toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        topping_weight = sum(self.toppings.values())
        return topping_weight + self.dough.weight

