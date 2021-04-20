import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from calculator import Calculator


class TomsRetailCalc(QMainWindow):
    """ Main UI class
    """

    def __init__(self):
        super().__init__()
        self.calculator = Calculator()
        self.states = self.calculator.get_states()
        self.current_state = None
        self.__init_ui()

    def __init_ui(self):
        """ create UI elements
        """
        self.setWindowTitle("Tom's retail calculator")

        self.quantity_label = QLabel(self)
        self.quantity_label.setText('Quantity:')
        self.price_label = QLabel(self)
        self.price_label.setText('Price ($):')
        self.state_label = QLabel(self)
        self.state_label.setText('State:')
        self.total_label = QLabel(self)
        self.total_label.setText('Total ($):')
        self.tax_label = QLabel(self)
        self.tax_label.setText('With Tax ($):')

        price_validator = QDoubleValidator()
        price_validator.setDecimals(2)
        price_validator.setBottom(0.0)
        qty_validator = QIntValidator()
        qty_validator.setBottom(0)
        self.price_line = QLineEdit(self)
        self.quantity_line = QLineEdit(self)
        self.price_line.setValidator(price_validator)
        self.quantity_line.setValidator(qty_validator)
        self.state_box = QComboBox(self)
        self.state_box.addItems(list(self.states.keys()))
        self.current_state = self.state_box.currentText()
        self.state_box.currentIndexChanged.connect(self.state_changed)
        self.total_line = QLineEdit(self)
        self.total_line.setReadOnly(True)
        self.tax_line = QLineEdit(self)
        self.tax_line.setReadOnly(True)
        self.calculate_button = QPushButton(self)
        self.calculate_button.setText("Calculate")
        self.calculate_button.clicked.connect(self.calculate_total)

        # move elements
        self.price_label.move(20, 20)
        self.quantity_label.move(20, 60)
        self.state_label.move(20, 100)
        self.total_label.move(20, 140)
        self.tax_label.move(20, 180)

        self.price_line.resize(200, 32)
        self.price_line.move(90, 20)
        self.quantity_line.resize(40, 32)
        self.quantity_line.move(90, 60)
        self.state_box.resize(40, 32)
        self.state_box.move(90, 100)
        self.total_line.resize(200, 32)
        self.total_line.move(90, 140)
        self.tax_line.resize(200, 32)
        self.tax_line.move(90, 180)
        self.calculate_button.resize(100, 32)
        self.calculate_button.move(190, 100)

        # show main window
        self.setGeometry(400, 250, 310, 230)
        self.setFixedSize(self.size())
        self.show()

    def state_changed(self, _):
        """ process change of state
        """
        self.current_state = self.state_box.currentText()

    def calculate_total(self):
        """ process calculate button
        """
        price = self.price_line.text()
        qty = self.quantity_line.text()
        qty = int(qty) if qty else 0
        price = price.replace(',', '.')
        price = float(price) if price else 0.0
        total = self.calculator.apply_discount(self.calculator.full_price(price, qty))
        tax = self.calculator.apply_tax(total, self.states[self.current_state].get_tax())
        self.total_line.setText(str(total))
        self.tax_line.setText(str(tax))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TomsRetailCalc()
    sys.exit(app.exec_())
