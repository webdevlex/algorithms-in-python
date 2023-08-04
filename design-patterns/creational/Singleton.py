class Singleton:
    _instance = None

    def __new__(self):
        if self._instance is None:
            self._instance = super(Singleton, self).__new__(self)
        return self._instance


# Client code
s1 = Singleton()

s2 = Singleton()

print(s1 is s2)  # Output: True (both s1 and s2 are the same instance)
