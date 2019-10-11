from Cat import Cat
from observer import zooAnnouncer
import abc


class Zookeeper:
    # Observer pattern
    @abc.abstractmethod
    def attach(self, zooAnnouncer):
        pass

    @abc.abstractmethod
    def detach(self, zooAnnouncer):
        pass

    @abc.abstractmethod
    def notify(self, arg):
        pass


class concreteZookeeper(Zookeeper):

    # project 1
    # Observer pattern:
    # in every method I called notify to update zoo announcer about changes
    def __init__(self, name):
        self.observers = []
        self.name = name

        # new attribute for observer pattern
        # self.observers = []

    def wakeup(self, a):
        # a = Cat(a.name)
        print("<my name is {}. My type is a {}.>".format(a.name, type(a).__name__))
        if isinstance(a, Cat):
            a.random()
        else:
            a.wakeup()
        self.notify("wakeup")

    def rollcall(self, a):
        # a = Cat(a.name)
        print("<my name is {}. My type is a {}.>".format(a.name, type(a).__name__))
        if isinstance(a, Cat):
            a.random()
        else:
            a.noise()
        self.notify("rollcall")

    def feed(self, a):
        # a = Cat(a.name)
        print("<my name is {}. My type is a {}.>".format(a.name, type(a).__name__))
        if isinstance(a, Cat):
            a.random()
        else:
            a.eat()
        self.notify("feed")

    def exercise(self, a):
        # a = Cat(a.name)
        print("<my name is {}. My type is a {}.>".format(a.name, type(a).__name__))
        if isinstance(a, Cat):
            a.random()
        else:
            a.sleep()
        self.notify("exercise")

    def shut_down(self):
        print("I am shutting down the zoo now.")
        self.notify("shut_down")

    # Observer pattern

    def attach(self, zooAnnouncer):
        print("attached the observer")
        self.observers.append(zooAnnouncer)

    def detach(self, zooAnnouncer):
        print("detached the observer")
        self.observers.remove(zooAnnouncer)

    def notify(self, arg):
        for i in self.observers:
            i.update(arg)
