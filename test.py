# test.py

from unittest import TestCase, main as unittest_main
from businfo import busInfo
from driverinfo import driverInfo
from sparepartinfo import sparePartInfo


class busInfoTest(TestCase):
    some_bus = busInfo("DW 123 X", "Double-Decker", "BMW")

    def test_regNum(self):
        self.assertEqual(self.some_bus.getBusRegNumber(), "DW 123 X")

    def test_type(self):
        self.assertEqual(self.some_bus.getBusType(), "Double-Decker")

    def test_maker(self):
        self.assertEqual(self.some_bus.getBusMaker(), "BMW")


class driverinfoTest(TestCase):
    some_driver = driverInfo("Anderson Silver", "M",
                             "Accra, Mantseman - 123", "+233267330353")

    def test_driverName(self):
        self.assertEqual(self.some_driver.getDriverName(), "Anderson Silver")

    def test_gender(self):
        self.assertEqual(self.some_driver.getGender(), "M")

    def test_billAddress(self):
        self.assertEqual(self.some_driver.getBillAddress(),
                         "Accra, Mantseman - 123")

    def test_contactNumber(self):
        self.assertEqual(self.some_driver.getContactNumber(), "+233267330353")


class sparePartInfoTest(TestCase):
    pass


if __name__ == '__main__':
    unittest_main()  # called it this for scopinng issue
