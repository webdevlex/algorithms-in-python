# Question: Design a parking lot using object-oriented principles.

from enum import Enum


class VehicleSize(Enum):
    MOTORCYCLE = 1
    COMPACT = 2
    LARGE = 3


class Vehicle:
    def __init__(self, licencePlate, spotsNeeded, size):
        self.parkingSpotsTaken = []
        self.licencePlate = licencePlate
        self.spotsNeeded = spotsNeeded
        self.size = size

    def getSpotsNeeded(self):
        return self.spotsNeeded

    def getSize(self):
        return self.size

    def parkInSpot(self, parkingSpot):
        self.parkingSpotsTaken.push(parkingSpot)

    def clearSpots(self):
        for parkingSpot in self.parkingSpotsTaken:
            parkingSpot.leaveSpot()
            self.parkingSpotsTaken.remove(parkingSpot)

    def canFitInSpot(self, parkingSpot):
        return parkingSpot.canFitVehicle(self)


class ParkingSpot:
    def __init__(self, spotSize, level, row, spotNumber):
        self.spotSize = spotSize
        self.level = level
        self.row = row
        self.spotNumber = spotNumber
        self.isAvailable = True

    def isAvailable(self):
        return self.isAvailable

    def canFitVehicle(self, vehicle):
        vehicleIsMotorCycle = vehicle.getSize() == VehicleSize.MOTORCYCLE
        vehicleIsCompact = vehicle.getSize() == VehicleSize.COMPACT
        vehicleIsLarge = vehicle.getSize() == VehicleSize.LARGE

        spotIsCompact = self.spotSize == VehicleSize.COMPACT
        spotIsLarge = self.spotSize == VehicleSize.LARGE

        if vehicleIsMotorCycle:
            return True
        elif vehicleIsCompact and (spotIsCompact or spotIsLarge):
            return True
        elif vehicleIsLarge and spotIsLarge:
            return True
        return False

    def parkInSpot(self):
        self.isAvailable = False

    def leaveSpot(self):
        self.isAvailable = True

    def getRow(self):
        return self.row

    def getSpotNumber(self):
        return self.spotNumber


class Car(Vehicle):
    def __init__(self, licencePlate):
        super.__init__(licencePlate, 1, VehicleSize.COMPACT)
