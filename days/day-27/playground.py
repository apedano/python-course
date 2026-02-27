def add(*args):
    return sum(args)
print(add(1,2,3,4,5,6,7,8,9)) #45


def calculate(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}->{value}")

calculate(add=1, multiply=2) #{'add': 1, 'multiply': 2}


def calculate(op, **kwargs):
    print(op)
    for key, value in kwargs.items():
        print(f"{key}->{value}")

calculate("add", a=3, b=4, c=5)