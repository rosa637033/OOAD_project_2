from Cat import Cat
from Lion import Lion
from interface import fastMove, slowMove
from observer import concreteZooAnnouncer
from Zookeeper import concreteZookeeper

zookeeper = concreteZookeeper("zookeeper")
zooann1 = concreteZooAnnouncer("zooann1")
zookeeper.attach(zooann1)
zooann2 = concreteZooAnnouncer("zooann2")
zookeeper.attach(zooann2)

# Instantiate cats
chi = Cat("Chi", slowMove())
chi.move()
chi.setMove(fastMove())
chi.move()
zookeeper.feed(chi)

# Instantiate lions
lin = Lion("Lin", fastMove())
zookeeper.feed(lin)


zookeeper.detach(zooann1)
zookeeper.detach(zooann2)
