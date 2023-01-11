class GreetingView:
    def generate_greeting(self, name, known):
        if known:
            message = f"Welcome back {name}!"
        else:
            message = f"Hi {name}, it is good to meet you!"
        return message
