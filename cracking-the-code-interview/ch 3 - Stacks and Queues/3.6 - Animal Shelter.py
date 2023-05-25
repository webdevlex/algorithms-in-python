from LinkedList import LinkedList


class Animal:
    def __init__(self, name):
        self.name = name
        self.order = -1

    def setOrder(self, order):
        self.order = order

    def getOrder(self):
        return self.order

    def getName(self):
        return self.name


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)


class AnimalQueue:
    def __init__(self):
        self.dogList = LinkedList()
        self.catList = LinkedList()
        self.order = 0

    def enqueue(self, animal):
        animal.setOrder(self.order)
        self.order += 1
        if isinstance(animal, Dog):
            self.dogList.insert(animal)
        else:
            self.catList.insert(animal)

    def dequeueAny(self):
        oldestDog = self.getOldestDogOrder()
        oldestCat = self.getOldestCatOrder()
        if oldestCat == oldestCat:
            ValueError("No animals remaining")
        if oldestDog < oldestCat:
            return self.dequeueDog()
        else:
            return self.dequeueCat()

    def getOldestDogOrder(self):
        order = float("inf")
        if self.dogList.getSize() != 0:
            order = self.dogList.getHead().getItem().getOrder()
        return order

    def getOldestCatOrder(self):
        order = float("inf")
        if self.catList.getSize() != 0:
            order = self.catList.getHead().getItem().getOrder()
        return order

    def dequeueDog(self):
        if self.dogList.getHead() == None:
            raise ValueError("You tried to dequeue an empty dog list")
        return self.dogList.dequeue()

    def dequeueCat(self):
        if self.catList.getHead() == None:
            raise ValueError("You tried to dequeue an empty cat list")
        return self.catList.dequeue()


teet = Dog("Teet")
tabby = Cat("Tabby")
rosie = Dog("Rosie")
toby = Cat("Toby")
animals = AnimalQueue()
animals.enqueue(teet)
animals.enqueue(tabby)
animals.enqueue(rosie)
animals.enqueue(toby)
print(animals.dequeueCat().getItem().getName())
print(animals.dequeueAny().getItem().getName())
print(animals.dequeueCat().getItem().getName())
print(animals.dequeueAny().getItem().getName())
