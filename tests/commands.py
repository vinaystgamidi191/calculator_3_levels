from typing import Union
from app.calculator import Calculator

class Command:
    def __init__(self, calculator):
        self.calculator = calculator

    def execute(self):
        pass
class AddCommand(Command):
    def execute(self):
        return self.calculator.add()

class SubtractCommand(Command):
    def execute(self):
        return self.calculator.subtract()

class MultiplyCommand(Command):
    def execute(self):
        return self.calculator.multiply()

class DivideCommand(Command):
    def execute(self):
        return self.calculator.divide()

class MenuCommand(Command):
    def execute(self):
        print("Available commands:")
        print("add, subtract, multiply, divide, menu")

class TestCommands:
    def setUp(self):
        self.calculator = Calculator(10, 5)

    def test_add_command(self):
        add_command = AddCommand(self.calculator)
        result = add_command.execute()
        assert result == 15

    def test_subtract_command(self):
        subtract_command = SubtractCommand(self.calculator)
        result = subtract_command.execute()
        assert result == 5

    def test_multiply_command(self):
        multiply_command = MultiplyCommand(self.calculator)
        result = multiply_command.execute()
        assert result == 50

    def test_divide_command(self):
        divide_command = DivideCommand(self.calculator)
        result = divide_command.execute()
        assert result == 2

    def test_menu_command(self):
        menu_command = MenuCommand(self.calculator)
        # Redirect stdout to StringIO to capture printed output
        with captured_output() as (out, err):
            menu_command.execute()
        output = out.getvalue().strip()
        expected_output = "Available commands:\nadd, subtract, multiply, divide, menu"
        assert output == expected_output
