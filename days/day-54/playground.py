class UppercaseDecoratorWithState:
    def __init__(self, function):
        self.function = function
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.counter += 1
        print(f"This is the #{self.counter} time the decorator is used")
        result = self.function(*args, **kwargs)
        return result.upper()

@UppercaseDecoratorWithState
def greet(name):
    return f"hello there {name}"  

print(greet("Ciccio"))
print(greet("Pasticcio"))