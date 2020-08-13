class transactionInfo:

    def __init__(self, tRegNumb: str, tDate, tSchStart, tSchEnd, tMechanic: mechanicInfo, tHelper: mechanicInfo, tNeededSparePartes: list):
        self.regNumb = tRegNumb
        self.date = tDate
        self.schStart = tSchStart
        self.schEnd = tSchEnd
        self.mechanic = tMechanic
        self.helper = tHelper
        self.neededSpareParts = tNeededSparePartes

    def getRegNum(self):
        return self.regNumb

    def getDate(self):
        return self.date

    def getSchStart(self):
        return self.schStart

    def getSchEnd(self):
        return self.schEnd

    def getMechanic(self):
        return self.mechanic

    def getHelper(self):
        return self.helper

    def getNeededSpareParts(self):
        return self.neededSpareParts

    def setRegNum(self, tRegNumb):
        self.regNumb = tRegNumb

    def setDate(self, tDate):
        self.date = tDate

    def setSchStart(self, tSchStart):
        self.schStart = tSchStart

    def setSchEnd(self, tSchEnd):
        self.schEnd = tSchEnd

    def setMechanic(self, tMechanic: mechanicInfoI):
        self.mechanic = tMechanic

    def setHelper(self, tHelper: mechanicInfo):
        self.helper = tHelper

    def setNeededSpareParts(self, tNeededSparePartes: list):
        self.neededSpareParts = tNeededSparePartes
