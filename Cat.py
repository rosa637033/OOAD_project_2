from Feline import Feline
import random

class Cat(Feline):
    # def __init__(self,name, move):
    #     self.name = name
    #     self.move = move

    def noise(self):
        print("Meow")

    def roam(self):
        print("Meow meow meow")

    def random(self):
        rand = random.randint(1,10)
        if rand%5 == 0:
            self.wake()

        elif rand%5 == 1:
            self.noise()

        elif rand%5 == 2:
            self.eat()

        elif rand%5 == 3:
            self.roam()

        else:
            self.sleep()
