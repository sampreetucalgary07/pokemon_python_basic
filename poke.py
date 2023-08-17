# from pathlib import Path

# print(Path().home())


# create a pokemon
class Pokemon:
    def __init__(self, name, primary_type, max_hp):
        self.name = name
        self.primary_type = primary_type
        self.max_hp = max_hp
        self.hp = max_hp

    def __str__(self) -> str:
        return f"Pokemon: {self.name}, Type: {self.primary_type}, HP: {self.hp}/{self.max_hp}"

    def __repr__(self) -> str:
        return f"trying representation method"

    # feed them to increase the health
    def feed(self):
        if self.hp < self.max_hp:
            self.hp += 1
            print(f"{self.name} has health {self.hp} HP")
        else:
            print(f"Health is full")

    # make them battle and decide the winner
    def battle(self, other):
        print(f"Battle : {self.name} V/S {other.name}")
        # call typewheel()
        result = self.typewheel(self.primary_type, other.primary_type)
        # depending on the result, have effects
        if result == "lose":
            self.hp -= 10
            print(f"{self.name} lose and now has {self.hp} HP.")
        print(f"Battle result : {result}")

    @staticmethod
    def typewheel(type1, type2):
        result = {0: "lose", 1: "win", -1: "tie"}
        # mapping between types and result conditions
        game_map = {"water": 0, "fire": 1, "grass": 2}
        # implement win-loose matrix
        wl_matrix = [
            [-1, 1, 0],  # water
            [0, -1, 1],  # fire
            [1, 0, -1],  # grass
        ]
        # declare a winner
        wl_result = wl_matrix[game_map[type1]][game_map[type2]]
        return wl_result


# take a look into it
if __name__ == "__main__":
    print(Pokemon(name="bulbasaur", primary_type="grass", max_hp=100))
    print(Pokemon(name="charmander", primary_type="fire", max_hp=100))
