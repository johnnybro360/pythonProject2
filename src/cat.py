"""Module docstring"""
class Dog:
    name = 'fido'

class Animal:
    def make_sound(self):
        print(f"{self.name}<Opens Mouth>")


class Cat(Animal):
    """This class defines a cat"""
    def __init__(self, name):
        self.name = name


    def make_sound(self):
        super().make_sound()
        """method docstring"""
        print(f"{self.name} Meows Prrrs Meows")

    # def __repr__(self):
    #     return f"Cat()"
    #
    # def __str__(self):
    #     return 'meow'


if __name__ == '__main__':
    from pprint import pprint
    best_cat = Cat('Lenny')
    best_cat.make_sound()
    doggy = Dog()
    # pprint(dir(lenny))

