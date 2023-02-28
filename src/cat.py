from typing import Optional, List, Sequence
from collections.abc import Sequence

"""Module docstring"""
class Dog:
    name = 'fido'


class Animal:
    def make_sound(self):
        print(f"{self.name}<Opens Mouth>")


class Cat(Animal):
    species = 'Felis Catus'
    """This class defines a cat"""
    def __init__(self, names: Sequence[str]) -> None:
        self.name = names
        self.eat: Optional[bool] = None
        self.my_species = Cat.species
        self.species = 'Felis Catus1'+ Cat.species

    @staticmethod
    def make_generic_sound():
        print("SOUND")

    @classmethod
    def make_generic_blink(cls):
        ...

    def make_sound(self) -> str:
        super().make_sound()
        """method docstring"""
        return f"{self.name} Meows Prrrs Meows"

    # def __repr__(self):
    #     return f"Cat()"
    #
    # def __str__(self):
    #     return 'meow'


if __name__ == '__main__':

    from pprint import pprint
    best_cat = Cat(123)
    best_cat.make_sound()
    doggy = Dog()
    Cat.make_generic_sound()
    # pprint(dir(lenny))
    print(Cat.species)
    print(best_cat.species)
