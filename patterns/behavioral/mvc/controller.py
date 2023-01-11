from patterns.behavioral.mvc.model import NameModel
from patterns.behavioral.mvc.view import GreetingView


class GreetingController:
    def __init__(self):
        self.model = NameModel()
        self.view = GreetingView()

    def handle(self, request):
        if request in self.model.get_name_list():
            greeting = self.view.generate_greeting(request, True)
        else:
            self.model.save_name(request)
            greeting = self.view.generate_greeting(request, False)
        print(greeting)


def main(name):
    request_handler = GreetingController()
    request_handler.handle(name)


if __name__ == '__main__':
    main('TEST NAME')
