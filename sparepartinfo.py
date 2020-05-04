class sparePartInfo:

    def __init__(self, sName, sDescription, sPrice):
        self.name = sName
        self.description = sDescription
        self.price = sPrice

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getPrice(self):
        return self.price

    def setName(self, sName):
        self.name = sName

    def setDescription(self, sDescription):
        self.description = sDescription

    def setPrice(self, sPrice):
        self.price = sPrice