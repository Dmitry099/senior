from base64 import b64decode, b64encode


class User:
    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    @classmethod
    def get_verified_user(cls, username, password):
        return User(username, password, username, f"{username}@demo.com")


class EndHandler:

    def __init__(self):
        pass

    def handle_request(self, request, response=None):
        return response.encode('utf-8')


class AuthorizationHandler:

    def __init__(self, next_handler=EndHandler):
        self.next_handler = next_handler()

    def handle_request(self, request, response=None):
        authorization_header = request["HTTP_AUTHORIZATION"]
        decoded_string = b64decode(authorization_header).decode('utf-8')
        username, password = decoded_string.split(":")
        request['username'] = username
        request['password'] = password
        return self.next_handler.handle_request(request, response)


class UserHandler:

    def __init__(self, next_handler=EndHandler):
        self.next_handler = next_handler()

    def handle_request(self, request, response=None):
        user = User.get_verified_user(request['username'], request['password'])
        request['user'] = user
        return self.next_handler.handle_request(request, response)


class PathHandler:

    def __init__(self, next_handler=EndHandler):
        self.next_handler = next_handler()

    def handle_request(self, request, response=None):
        path = request["PATH_INFO"].split("/")
        if 'goodbye' in path:
            response = f"Goodbye {request['user'].name}!"
        else:
            response = f"Hello {request['user'].name}!"
        return self.next_handler.handle_request(request, response)


def application(env, start_response):

    head = AuthorizationHandler()
    previous_handler = head
    for handler in (UserHandler, PathHandler):
        previous_handler.next_handler = handler()
        previous_handler = previous_handler.next_handler
    print(head.handle_request(env).decode())


if __name__ == '__main__':
    env = {
        "PATH_INFO": "hello",
        "HTTP_AUTHORIZATION": b64encode(b'TESTNAME:TESTPASSW')
    }
    application(env, None)
