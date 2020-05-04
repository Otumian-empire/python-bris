class driverInfo:

    def __init__(self, dDriverName: str, dGender: str, dBillAddr: str, dConatactNumber: str):
        self.driverName = dDriverName
        self.gender = dGender
        self.billAddress = dBillAddr
        self.contactNumber = dConatactNumber

    def getDriverName(self):
        return self.driverName

    def getGender(self):
        return self.gender

    def getBillAddress(self):
        return self.billAddress

    def getContactNumber(self):
        return self.contactNumber

    def setDriverName(self, dDriverName):
        self.driverName = dDriverName

    def setGender(self, dGender):
        self.gender = dGender

    def setBillAddress(self, dBillAddr):
        self.billAddress = dBillAddr

    def setContactNumber(self, dConatactNumber):
        self.contactNumber = dConatactNumber
