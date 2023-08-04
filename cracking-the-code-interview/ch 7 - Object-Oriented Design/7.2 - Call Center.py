from enum import Enum


class Rank(Enum):
    RESPONDENT = 0
    MANAGER = 1
    DIRECTOR = 2


class CallHandler:
    def __init__(self):
        self.employeeLevels = [[], [], []]
        self.callQueue = [[], [], []]

    def addEmployee(self, employee):
        self.employeeLevels[employee.getRank().value].append(employee)

    def call(self, caller):
        call = Call(caller)
        self.dispatchCall(call)

    def dispatchCall(self, call):
        employee = self.getHandlerForCall(call)
        if employee:
            self.assignCall(call, employee)
        else:
            self.addCallToQueue(call)

    def getHandlerForCall(self, call):
        for employee in self.employeeLevels[call.getRank().value]:
            if employee.isFree():
                return employee
        return None

    def assignCall(self, call, employee):
        call.setHandler(employee)
        employee.recieveCall(call)

    def addCallToQueue(self, call):
        print(f"{call.getCaller().getName()} was added to the waiting queue")
        self.callQueue[call.getRank().value].append(call)


class Caller:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


class Call:
    def __init__(self, caller, rank=Rank.RESPONDENT, handler=None):
        self.caller = caller
        self.rank = rank
        self.handler = handler

    def setHandler(self, employee):
        self.handler = employee

    def getCaller(self):
        return self.caller

    def getRank(self):
        return self.rank

    def setRank(self, rank):
        self.rank = rank

    def incrementRank(self):
        self.rank = self.rank + 1


class Employee:
    def __init__(self, name, rank, handler):
        self.name = name
        self.currentCall = None
        self.rank = rank
        self.handler = handler

    def recieveCall(self, call):
        print(f"{self.name} answered the call")
        self.currentCall = call

    def completeCall(self):
        self.currentCall = None

    def escalateCall(self):
        self.currentCall.incrementRank()
        self.handler.dispatchCall(self.currentCall)

    def isFree(self):
        return not self.currentCall

    def getRank(self):
        return self.rank


class Director(Employee):
    def __init__(self, name, handler):
        super().__init__(name, Rank.DIRECTOR, handler)


class Manager(Employee):
    def __init__(self, name, handler):
        super().__init__(name, Rank.MANAGER, handler)


class Respondent(Employee):
    def __init__(self, name, handler):
        super().__init__(name, Rank.RESPONDENT, handler)


def addEmployees(callCenter):
    callCenter.addEmployee(Respondent("Pam", callCenter))
    callCenter.addEmployee(Respondent("Dwight", callCenter))
    callCenter.addEmployee(Respondent("Jim", callCenter))

    callCenter.addEmployee(Manager("Michael", callCenter))
    callCenter.addEmployee(Manager("Jan", callCenter))

    callCenter.addEmployee(Director("David", callCenter))


def main():
    # Add employees to call center
    callCenter = CallHandler()
    addEmployees(callCenter)

    # Create a new caller and call the call center
    newCaller = Caller("Caller 1")
    callCenter.call(newCaller)

    newCaller = Caller("Caller 2")
    callCenter.call(newCaller)

    newCaller = Caller("Caller 3")
    callCenter.call(newCaller)

    newCaller = Caller("Caller 4")
    callCenter.call(newCaller)


main()
