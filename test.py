# test.py

from unittest import TestCase, main as unittest_main
from businfo import busInfo
from driverinfo import driverInfo
from sparepartinfo import sparePartInfo
from mechanicinfo import mechanicInfo


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
    some_spare_part = sparePartInfo(
        "Tube", "shapes the tyre when inflated", 12.00)

    def test_name(self):
        self.assertEqual(self.some_spare_part.getName(), "Tube")

    def test_desciption(self):
        self.assertEqual(self.some_spare_part.getDescription(),
                         "shapes the tyre when inflated")

    def test_price(self):
        self.assertEqual(self.some_spare_part.getPrice(), 12.00)


class mechanicInfoTest(TestCase):
    some_mechanic = mechanicInfo("Daniel Hanni", 23.00)

    def test_name(self):
        self.assertEqual(self.some_mechanic.getName(), "Daniel Hanni")

    def test_salary(self):
        self.assertEqual(self.some_mechanic.getSalary(), 23.00)


if __name__ == '__main__':
    unittest_main()  # called it this for scopinng issue
