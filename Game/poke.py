from pathlib import Path


class Pokemon:
    def __init__(self, name, primary_type, max_hp):
        self.name = name
        self.primary_type = primary_type
        self.hp = max_hp
        self.max_hp = max_hp

    def __str__(self):
        return f"{self.name} ({self.primary_type}): {self.hp}/{self.hp}"

    def feed(self):
        if self.hp < self.max_hp:
            self.hp += 1
            print(f"{self.name} has now {self.hp} HP.")
        else:
            print(f"{self.name} is full")

    def battle(self, other):
        result = self.typewheel(self.primary_type,other.primary_type)
        print(f"{self.name} fought {other.name} and the result is a {result}")
        # call type wheel

    @staticmethod
    def typewheel(type1, type2):
        result = {0: "loose", 1: "win", -1: "tie"}
        # mapping between types and result conditions
        game_map = {"water": 0, "fire": 1, "grass": 2}
        # implement win-lose matrix
        wl_matrix = [
            [-1, 1, 0],  # water
            [0, -1, 1],  # fire
            [1, 0, -1]  # grass
        ]
        # declare a winner
        wl_result = wl_matrix[game_map[type1]][game_map[type2]]
        # declare a winner
        return result[wl_result]


test1 = Pokemon(name='Test1', primary_type="grass", max_hp=150)
test2 = Pokemon(name='Test2', primary_type="water", max_hp=100)

test1.battle(test2)
