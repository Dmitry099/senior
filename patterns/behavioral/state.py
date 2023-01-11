import time


class State:
    def __init__(self, state_machine):
        self.state_machine = state_machine

    def switch(self, in_key):
        self.state_machine.state = self.state_machine.mapping.get(
            in_key, self.state_machine.standing
        )


class Standing(State):
    def __str__(self):
        return "Standing"


class RunningLeft(State):
    def __str__(self):
        return "Running Left"


class RunningRight(State):
    def __str__(self):
        return "Running Right"


class Jumping(State):
    def __str__(self):
        return "Jumping"


class Crouching(State):
    def __str__(self):
        return "Crouching"


class StateMachine:

    def __init__(self):
        self.standing = Standing(self)
        self.running_left = RunningLeft(self)
        self.running_right = RunningRight(self)
        self.jumping = Jumping(self)
        self.crouching = Crouching(self)

        self.mapping = {
            "a": self.running_left,
            "d": self.running_right,
            "s": self.crouching,
            "w": self.jumping
        }

        self.state = self.standing

    def action(self, in_key):
        self.state.switch(in_key)

    def __str__(self):
        return str(self.state)


def main():
    player = StateMachine()

    while True:
        command = input('Please provide command: ')
        if command:
            player.action(command)
            print(player.state)
            time.sleep(0.5)
        else:
            break


if __name__ == '__main__':
    main()
