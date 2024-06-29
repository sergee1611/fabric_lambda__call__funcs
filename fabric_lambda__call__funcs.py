def create_operation(operation):
    if operation == '*':
        def multiply(x, y):
            return x * y
        return multiply
    elif operation == '/':
        def divide(x, y):
            return x / y
        return divide


try:
    my_func_1 = create_operation('*')
    my_func_2 = create_operation('/')
    print(my_func_1(2, 3))
    print(my_func_2(8, 4))
    print(my_func_2(8, 0))
except ZeroDivisionError as zer_div:
    print(f'Error: {zer_div}')

square = lambda x: x ** 2
print(square(4))


def square_def(x):
    return x ** 2


print(square_def(4))


class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b


rectangle = Rect(2, 4)
print(rectangle())
