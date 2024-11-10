import random

class MathOperation:
    def __init__(self, *args):
        self.numbers = args
        self.result = None

    def __hide_numbers(self):
        # випадкова математична операція
        operation = random.choice(['+', '-', '*', '/'])
        if operation == '+':
           self.result = sum(self.numbers)
        elif operation == '-':
            self.result = self.numbers[0]
            for num in self.numbers[1:]:
                self.result -= num
        elif operation == '*':
            self.result = 1
            for num in self.numbers:
                self.result *= num
        elif operation == '/':
            self.result = self.numbers[0]
            for num in self.numbers[1:]:
                self.result /= num

    def calculate(self):
        self.__hide_numbers()

    def __str__(self):
        if self.result is None:
            self.calculate()
        return f"Результат обчислень: {self.result}"

# Приклад використання
operation = MathOperation(12, 6, 2)
print(operation)
