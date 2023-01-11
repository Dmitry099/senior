import time


class RawCalculator:

    def fibbonacci(self, n):
        if n < 2:
            return 1
        return self.fibbonacci(n-2) + self.fibbonacci(n-1)


def memoize(fn):
    _cache = {}

    def memoized(*args):
        key = (fn.__name__, args)
        if key in _cache:
            return _cache[key]
        _cache[key] = fn(*args)
        return _cache[key]

    return memoized


class CalculatorProxy:

    def __init__(self, target):
        self.target = target
        fib = getattr(self.target, 'fibbonacci')
        setattr(self.target, 'fibbonacci', memoize(fib))

    def __getattr__(self, item):
        return getattr(self.target, item)


if __name__ == "__main__":
    raw_calculator = RawCalculator()
    start_time_1 = time.time()
    [raw_calculator.fibbonacci(x) for x in range(0, 40)]
    end_time_1 = time.time()
    print(f'Raw calculation tooks {end_time_1 - start_time_1}')
    calculator = CalculatorProxy(RawCalculator())
    start_time_2 = time.time()
    [calculator.fibbonacci(x) for x in range(0, 40)]
    end_time_2 = time.time()
    print(f'Proxy calculation tooks {end_time_2 - start_time_2}')
