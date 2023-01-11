class SingletonClass(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonClass, cls).__new__(cls)
        return cls._instance


# One more way with class wrapping
class SingletonNewClass(object):
    class _SingletonObject(object):
        pass

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = SingletonNewClass._SingletonObject()
        return cls._instance

    def __getattr__(self, key, value):
        getattr(self._instance, key, value)

    def __setattr__(self, key, value):
        setattr(self._instance, key, value)


if __name__ == '__main__':
    a = SingletonClass()
    a.x = 'Hello'
    print(f'a.x -> {a.x}')
    b = SingletonClass()
    print(f'b.x -> {b.x}')
    b.x = 'Goodbye'
    print(f'a.x -> {a.x}')
    print(f'b.x -> {b.x}')
