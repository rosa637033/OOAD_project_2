# abstract base classes is similar to interface in python
import abc
class move(abc.ABC):

    @abc.abstractmethod
    def run(self):
        pass

# Concrete strategy pattern
class slowMove(move):
    def run(self):
        print("I am moving slow")

class fastMove(move):
    def run(self):
        print("I am moving fast")
