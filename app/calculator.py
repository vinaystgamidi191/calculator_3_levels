from typing import Union



class Calculator:
    history = []

    def __init__(self, a: Union[int, float], b: Union[int, float]):
        self.a = a
        self.b = b

    def add(self) -> Union[int, float]:
        result = self.a + self.b
        Calculator.history.append(f"{self.a} + {self.b} = {result}")
        return result

    def subtract(self) -> Union[int, float]:
        result = self.a - self.b
        Calculator.history.append(f"{self.a} - {self.b} = {result}")
        return result

    def multiply(self) -> Union[int, float]:
        result = self.a * self.b
        Calculator.history.append(f"{self.a} * {self.b} = {result}")
        return result

    def divide(self) -> Union[int, float]:
        if self.b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = self.a / self.b
        Calculator.history.append(f"{self.a} / {self.b} = {result}")
        return result
