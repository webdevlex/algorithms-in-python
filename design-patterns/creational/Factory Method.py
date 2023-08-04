from abc import ABC, abstractmethod


# Abstract Product
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


# Concrete Products
class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


# Factory Method
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass


# Concrete Factories
class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()


class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()


# Client code
def get_animal_sound(factory):
    animal = factory.create_animal()
    return animal.speak()


# Usage
dog_sound = get_animal_sound(DogFactory())  # Output: "Woof!"
cat_sound = get_animal_sound(CatFactory())  # Output: "Meow!"
