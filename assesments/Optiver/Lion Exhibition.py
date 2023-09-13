from dataclasses import dataclass


@dataclass
class LionDescription:
    name: str
    height: int


@dataclass
class LionSchedule:
    name: str
    enter_time: int
    exit_time: int


class LionCompetition:
    def __init__(self, lions: list[LionDescription], schedule: list[LionSchedule]):
        self.myLions = lions
        self.myLionHeights = self._initLionHeights(lions)
        self.mySchedule = self._initSchedule(schedule)
        self.heightsOfLionsInRoom = []

    def _initLionHeights(self, lions):
        myLionHeights = {}
        for myLion in lions:
            myLionHeights[myLion.height] = myLion.name
        return myLionHeights

    def _initSchedule(self, schedule):
        mySchedule = {}
        for lionEnteredEvent in schedule:
            mySchedule[lionEnteredEvent.name] = [
                lionEnteredEvent.enter_time,
                lionEnteredEvent.exit_time,
                False,
            ]
        return mySchedule

    def lion_entered(self, current_time: int, height: int):
        isMyLion = False
        for mylionEnteredEvent in self.mySchedule.values():
            if mylionEnteredEvent[0] == current_time and height in self.myLionHeights:
                mylionEnteredEvent[2] = True
                isMyLion = True

        if not isMyLion:
            self.heightsOfLionsInRoom.append(height)

    def lion_left(self, current_time: int, height: int):
        isMyLion = False
        for mylionLeftEvent in self.mySchedule.values():
            if mylionLeftEvent[1] == current_time and height in self.myLionHeights:
                mylionLeftEvent[2] = False
                isMyLion = True

        if not isMyLion:
            self.heightsOfLionsInRoom.remove(height)

    def get_biggest_lions(self) -> list[str]:
        competitionMaxHeight = 0
        for lionHeight in self.heightsOfLionsInRoom:
            if lionHeight > competitionMaxHeight:
                competitionMaxHeight = lionHeight

        result = []
        for myLion in self.myLions:
            if myLion.height >= competitionMaxHeight and self._myLionInRoom(
                myLion.name
            ):
                result.append(myLion.name)

        return result

    def _myLionInRoom(self, lionName):
        return self.mySchedule[lionName][2]


# Intalize marry
rob = LionDescription(name="rob", height=250)
robSchedule = LionSchedule(name="rob", enter_time=13, exit_time=20)


# Intalize rob
marry = LionDescription(name="marry", height=300)
marrySchedule = LionSchedule(name="marry", enter_time=10, exit_time=15)


# Intalize competition
competition = LionCompetition([rob, marry], [marrySchedule, robSchedule])

# Competition Begins
competition.lion_entered(8, 200)
competition.lion_entered(10, 310)
competition.lion_entered(10, 300)

results = competition.get_biggest_lions()
print(results)

competition.lion_entered(13, 250)
competition.lion_left(13, 310)

results = competition.get_biggest_lions()
print(results)

competition.lion_left(15, 300)

results = competition.get_biggest_lions()
print(results)

competition.lion_left(16, 200)
competition.lion_left(20, 250)
