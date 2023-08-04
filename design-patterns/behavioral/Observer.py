class Subject:
    def __init__(self):
        self._observers = []
        self._state = None

    def subscribe(self, observer):
        self._observers.append(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def set_state(self, state):
        self._state = state
        self.notify()

    def get_state(self):
        return self._state


class Observer:
    def update(self, subject):
        pass


# Concrete Observer 1
class ConcreteObserver1(Observer):
    def update(self, subject):
        print(f"ConcreteObserver1 received update: {subject.get_state()}")


# Concrete Observer 2
class ConcreteObserver2(Observer):
    def update(self, subject):
        print(f"ConcreteObserver2 received update: {subject.get_state()}")


# Usage
subject = Subject()

observer1 = ConcreteObserver1()
observer2 = ConcreteObserver2()

subject.subscribe(observer1)
subject.subscribe(observer2)

subject.set_state("State 1")
subject.set_state("State 2")

subject.unsubscribe(observer2)

subject.set_state("State 3")
