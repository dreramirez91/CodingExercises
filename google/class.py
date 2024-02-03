import random


class RandomSet:
    def __init__(self):
        self.values = set()

    def insert(self, value):
        self.values.add(value)

    def remove(self, value):
        self.values.discard(value)

    def get_random(self):
        return
        try:
            return random.choice(list(self.values))
        except IndexError:
            return "Your set is empty!"


my_set = RandomSet()
print(my_set.values)
my_set.insert(7)
my_set.insert(9)
my_set.insert(12)
print(my_set.get_random())
print(my_set.get_random())
print(my_set.get_random())
print(my_set.get_random())
