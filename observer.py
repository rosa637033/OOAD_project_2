import abc
class zooAnnouncer(abc.ABC):
    @abc.abstractmethod
    def update(self):
        pass

class concreteZooAnnouncer(zooAnnouncer):
    def __init__(self, arg):
        self.arg = arg

    def update(self, arg) -> None:
        if arg == "wakeup":
            print("Hi this is the {}, zookeeper is about to wake the animals".format(self.arg))
        elif arg == "rollcall":
            print("Hi this is the {}, zookeeper is about to roll call the animals".format(self.arg))
        elif arg == "feed":
            print("Hi this is the {}, zookeeper is about to feed the animals".format(self.arg))
        elif arg == "exercise":
            print("Hi this is the {}, zookeeper is about to exercise the animals".format(self.arg))
        else:
            print("Hi this is the {}, zookeeper is about to shut down the animals".format(self.arg))
