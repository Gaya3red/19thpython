class car:
    engineType = "Strongest Engine"
    numberOfTyres = 4
    numberOfWindow = 6
    isFridgeAvailable = True
    def getNumberOfWindows(self):
        return self.numberOfWindow
    def getNumberOfTyres(self):
        return self.numberOfTyres
car1 = car()
print(car1.getNumberOfWindows())
print(car1.getNumberOfTyres()) 