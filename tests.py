import unittest
from decimal import *
from calculator import Calculator, State


class CalculatorTestCase(unittest.TestCase):
    def test_full_price(self):
        """ Cover full price calculations
        """
        cases = [
            (100, 0, 0.0),
            (1000.45, 2, 2000.9),
            (1000.45222222, 2, 2000.9)
        ]
        for case in cases:
            self.assertEqual(Calculator.full_price(case[0], case[1]), case[2])

        type_errors = [
            ('100', 0),
            (1000.45, 2.6),
            (Decimal(1000.45), 2)  # no decimals for now
        ]
        for error in type_errors:
            try:
                Calculator.full_price(error[0], error[1])
            except TypeError:
                continue
            self.assertFalse(True)

        value_errors = [
            (-100.0, 1),
            (100, -1),
        ]
        for error in value_errors:
            try:
                Calculator.full_price(error[0], error[1])
            except ValueError:
                continue
            self.assertFalse(True)

    def test_discounts(self):
        """ Cover discounts calculations
        """
        cases = [
            (0, 0.0),
            (0.0, 0.0),
            (100, 100.0),
            (1000, 970.0),
            (12000, 10800.0),
            (50000, 42500.0),
            (55000.04, 46750.03)
        ]
        for case in cases:
            self.assertEqual(Calculator.apply_discount(case[0]), case[1])

        type_errors = [
            '100',
            Decimal(1000.45)  # no decimals for now
        ]
        for error in type_errors:
            try:
                Calculator.apply_discount(error)
            except TypeError:
                continue
            self.assertFalse(True)

        value_errors = [
            -100,
        ]
        for error in value_errors:
            try:
                Calculator.apply_discount(error)
            except ValueError:
                continue
            self.assertFalse(True)

    def test_taxes(self):
        """ Cover tax calculations
        """
        cases = [
            (0, 10, 0),
            (1.0, 20, 1.2),
            (10800, 6.5, 11502.0)
        ]
        for case in cases:
            self.assertEqual(Calculator.apply_tax(case[0], case[1]), case[2])
        type_errors = [
            ('100', 1),
            (1, '100'),
            (1, Decimal(1000.45)),  # no decimals for now
            (Decimal(1000.45), 1),
        ]
        for error in type_errors:
            try:
                Calculator.apply_tax(error[0], error[1])
            except TypeError:
                continue
            self.assertFalse(True)

        value_errors = [
            (-100.0, 5.5),
            (100, -5.5),
        ]
        for error in value_errors:
            try:
                Calculator.apply_tax(error[0], error[1])
            except ValueError:
                continue
            self.assertFalse(True)

    def test_states(self):
        """ Change this if states data changed
        """
        states = {
            'CA': State('CA', 8.25),
            'AL': State('AL', 4),
            'UT': State('UT', 6.85),
            'NV': State('NV', 8),
            'TX': State('TX', 6.25)
        }
        self.assertDictEqual(Calculator.get_states(), states)


if __name__ == '__main__':
    unittest.main()
