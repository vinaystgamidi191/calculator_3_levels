from typing import Union
from multiprocessing import Process, Queue
from app.calculator import Calculator
from tests.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand, MenuCommand

def calculate_and_enqueue(queue, calculator, command_name):
    command_map = {
        "add": AddCommand(calculator),
        "subtract": SubtractCommand(calculator),
        "multiply": MultiplyCommand(calculator),
        "divide": DivideCommand(calculator)
    }
    result = command_map[command_name].execute()
    queue.put((command_name, result))

def main():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    calculator = Calculator(a, b)
    commands = ["add", "subtract", "multiply", "divide"]
    results = {}
    queue = Queue()
    processes = []
    for command in commands:
        process = Process(target=calculate_and_enqueue, args=(queue, calculator, command))
        process.start()
        processes.append(process)
    for process in processes:
        process.join()
    while not queue.empty():
        command_name, result = queue.get()
        results[command_name] = result
    print("Results:")
    for command_name, result in results.items():
        print(f"{command_name.capitalize()} result: {result}")
    menu_command = MenuCommand(calculator)
    menu_command.execute()

if __name__ == "__main__":
    main()
