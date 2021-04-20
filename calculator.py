
class State:
    """ class to hold data about state
    """
    def __init__(self, name, tax):
        self._name = name
        self._tax = tax

    def get_tax(self):
        return self._tax

    def get_name(self):
        return self._name

    def __eq__(self, other):
        return self._name == other.get_name() and self._tax == other.get_tax()


class Calculator:
    """ class for calculations
    """

    @staticmethod
    def full_price(price, qty):
        """ Calculate full price, for USD take 2 digits after point
        Args:
            price - digit
            qty - int
        Returns:
            total - full price with 2 digits after point
        """
        if not isinstance(price, (int, float)) or not isinstance(qty, int):
            raise TypeError()
        if price < 0 or qty < 0:
            raise ValueError('Value must be positive')
        return round(price, 2) * qty

    @staticmethod
    def apply_discount(price):
        """ Calculate price with discount, for USD take 2 digits after point
        Args:
            price - digit
        Returns:
            total - discount price with 2 digits after point
        """
        if not isinstance(price, (int, float)):
            raise TypeError()
        price = round(price, 2)
        if price < 0:
            raise ValueError('Value must be positive')
        discount = 0
        if price >= 50000:
            discount = 15
        elif price >= 10000:
            discount = 10
        elif price >= 7000:
            discount = 7
        elif price >= 5000:
            discount = 5
        elif price >= 1000:
            discount = 3
        return round(price / 100 * (100 - discount), 2)

    @staticmethod
    def apply_tax(price, tax):
        """ Calculate price with tax, for USD take 2 digits after point
        Args:
            price - digit
            tax - digit
        Returns:
            total - tax price with 2 digits after point
        """
        if not isinstance(price, (int, float)) or not isinstance(tax, (int, float)):
            raise TypeError()
        if price < 0 or tax < 0:
            raise ValueError('Value must be positive')
        return round(price + (price * tax / 100), 2)

    @staticmethod
    def get_states():
        """ return data about all states
        Returns:
            dict - {name:state}
        """
        return {
            'UT': State('UT', 6.85),
            'NV': State('NV', 8),
            'TX': State('TX', 6.25),
            'AL': State('AL', 4),
            'CA': State('CA', 8.25)
        }
