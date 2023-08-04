class Employee:
    def __init__(self, rank, handler):
        self.currentCall = None
        self.rank = rank
        self.handler = handler

    def recieveCall(self, call):
        self.currentCall = call

    def completeCall(self):
        if not self.handler.assignCall(self):
            self.currentCall = None

    def escalateCall(self):
        self.call.incrementRank()
        self.handler.dispatchCall(self.call)
        if not self.handler.assignCall(self):
            self.currentCall = None

    def isFree(self):
        return not self.currentCall

    def getRank(self):
        return self.rank


class Director(Employee):
    def __init__(self, handler):
        super().__init__("director", handler)


class Manager(Employee):
    def __init__(self, handler):
        super().__init__("manager", handler)


class Respondent(Employee):
    def __init__(self, handler):
        super().__init__("respondent", handler)
