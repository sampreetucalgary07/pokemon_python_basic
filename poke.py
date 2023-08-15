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
        return f"Pokemon: {self.name}, Type: {self.primary_type}"

    # feed them to increase the health
    def feed(self):
        self.hp += 1

    # make them battle and decide the winner


# take a look into it

if __name__ == "__main__":
    print(Pokemon(name="bulbasaur", primary_type="grass", max_hp=100))
    print(Pokemon(name="charmander", primary_type="fire", max_hp=100))
