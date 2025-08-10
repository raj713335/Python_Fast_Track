# Addition of numbers using a Decorator

def sumx(func):
    def wrapper(*args, **kwargs):
        result = sum(args)
        return func(result, **kwargs)
    return wrapper

@sumx
def sum_numbers(result):
    return "Sum of numbers is {0}".format(result)

print(sum_numbers(1,2,3,4))