import copy


# Prototype interface/abstract class
class Prototype:
    def clone(self):
        pass


# Concrete Prototype class
class ConcretePrototype(Prototype):
    def __init__(self, field):
        self.field = field

    def clone(self):
        return copy.deepcopy(self)


# Client code
class Registery:
    def __init__(self):
        self.prototypes = {}
        self.prototypes["prototypeA"] = ConcretePrototype(1)
        self.prototypes["prototypeB"] = ConcretePrototype(2)

    def create_object(self, prototype_name):
        prototype = self.prototypes.get(prototype_name)
        if prototype:
            return prototype.clone()
        else:
            return None


# Usage
registery = Registery()
obj_a = registery.create_object("prototypeA")
obj_b = registery.create_object("prototypeB")

print(obj_a.field)  # Output: 1
print(obj_b.field)  # Output: 2
