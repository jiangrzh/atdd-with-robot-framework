import os
import unittest
from datetime import date, datetime

from vacalc.employeestore import EmployeeStore, VacalcError
from vacalc.dateprovider import CurrentDate


class TestEmployeeStore(unittest.TestCase):

    def test_adding_employee(self):
        store = EmployeeStore(None)
        employee = store.add_employee('Test Employee Store', '2000-12-24')
        self._assert_employee(employee, 'Test Employee Store',
                              date(2000, 12, 24))
        self.assertEquals(store.get_all_employees(), [employee])

    def test_adding_duplicate_employee(self):
        store = EmployeeStore(None)
        store.add_employee('test', '2000-12-24')
        self.assertRaises(VacalcError, store.add_employee,
                          'test', '2001-01-24')

    def test_getting_employee(self):
        store = EmployeeStore(None)
        employee = store.add_employee('Mr Foo Bar', '1990-02-03')
        self.assertEquals(store.get_employee('Mr Foo Bar'), employee)

    def test_get_missing_employee(self):
        store = EmployeeStore(None)
        self.assertRaises(VacalcError, store.get_employee, 'I am not here')

    def test_sorting(self):
        store = EmployeeStore(None)
        names = ('Urkki', 'Manu', 'Mara', 'JK')
        for name in names:
            store.add_employee(name, '2009-12-12')
        self.assertEquals([e.name for e in store.get_all_employees()], sorted(names))

    def _assert_employee(self, employee, name, date):
        self.assertEquals(employee.name, name)
        self.assertEquals(employee.startdate, date)


class TestDateProvider(unittest.TestCase):

    def test_in_normal_usage(self):
        self.assertEquals(CurrentDate().year, datetime.now().year)

    def test_mocked_date_time(self):
        os.environ['VACALC_DATE'] = '2009-03-01'
        self.assertEquals(CurrentDate().year, 2009)
        self.assertEquals(CurrentDate().month, 3)
        self.assertEquals(CurrentDate().day, 1)


if __name__ == '__main__':
    unittest.main()
