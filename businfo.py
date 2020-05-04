class busInfo:

    def __init__(self, bRegNumber: str, bType: str, bMaker: str):
        self.regNumber = bRegNumber
        self.type = bType
        self.maker = bMaker

    def getBusRegNumber(self):
        return self.regNumber

    def getBusType(self):
        return self.type

    def getBusMaker(self):
        return self.maker

    def setBusRegNumber(self, bRegNumber):
        self.regNumber = bRegNumber

    def setBusType(self, bType):
        self.type = bType

    def setBusMaker(self, bMaker):
        self.maker = bMaker
