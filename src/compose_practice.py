class Compose(object):

    def __init__(self, operations):
        self.operations = operations

    def __call__(self, x):
        for t in self.operations:
            x = t(x)
        return x


class Add(object):

    def __init__(self, x):
        self.x = x

    def __call__(self, y):
        return self.x + y


class Minus(object):

    def __init__(self, x):
        self.x = x

    def __call__(self, y):
        return y-self.x


if __name__ == '__main__':
    processor = Compose([Add(6), Minus(2)])
    print(processor(7))