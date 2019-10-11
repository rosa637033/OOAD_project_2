from interface import move
class Animal:
    #Constructor
    def __init__(self, name, move:move):
        self.name = name
        self._move = move

    # any move method that is in class move
    def setMove(self, move) -> move:
        self._move = move

    # This is where strategy pattern is implemented.
    def move(self):
        self._move.run()

    def wake(self):
        print("I am awake")

    def noise(self):
        print("aw")

    def eat(self):
        print("I am eating")

    def roam(self):
        print("aw")

    def sleep(self):
        print("I am going to sleep")
