class AddCommand:
    def __init__(self, receiver, value):
        self.receiver = receiver
        self.value = value

    def execute(self):
        self.receiver.add(self.value)

    def undo(self):
        self.receiver.subtract(self.value)


class SubtractCommand:
    def __init__(self, receiver, value):
        self.receiver = receiver
        self.value = value

    def execute(self):
        self.receiver.subtract(self.value)

    def undo(self):
        self.receiver.add(self.value)


class MultiplyCommand:
    def __init__(self, receiver, value):
        self.receiver = receiver
        self.value = value

    def execute(self):
        self.receiver.multiply(self.value)

    def undo(self):
        self.receiver.divide(self.value)


class DivideCommand:
    def __init__(self, receiver, value):
        self.receiver = receiver
        self.value = value

    def execute(self):
        self.receiver.divide(self.value)

    def undo(self):
        self.receiver.multiply(self.value)


class CalculationInvoker:
    def __init__(self):
        self.commands = []
        self.undo_stack = []

    def add_new_command(self, command):
        self.commands.append(command)

    def run(self):
        for command in self.commands:
            command.execute()
            self.undo_stack.append(command)

    def undo(self):
        undo_command = self.undo_stack.pop()
        undo_command.undo()


class Accumulator:
    def __init__(self, value):
        self._value = value

    def add(self, value):
        self._value += value

    def subtract(self, value):
        self._value -= value

    def multiply(self, value):
        self._value *= value

    def divide(self, value):
        self._value /= value

    def __str__(self):
        return f"Current Value: {self._value}"


if __name__ == '__main__':
    acc = Accumulator(10)

    invoker = CalculationInvoker()
    for command, value in [(AddCommand, 11), (SubtractCommand, 12),
                           (MultiplyCommand, 13), (DivideCommand, 14)]:
        invoker.add_new_command(command(acc, value))

    invoker.run()

    print(acc)

    for i in range(4):
        invoker.undo()

    print(acc)