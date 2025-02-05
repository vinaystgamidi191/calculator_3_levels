from typing import Union

class Calculator:
    history = []
    def __init__(self, a: Union[int, float], b: Union[int, float]):
        self.a = a
        self.b = b
    def add(self) -> Union[int, float]:
        return self.a + self.b
    def subtract(self) -> Union[int, float]:
        return self.a - self.b
    def multiply(cls, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        return a * b
    def divide(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = a / b
        Calculator.history.append(f"{a} / {b} = {result}")
        return result
