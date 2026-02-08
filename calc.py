#                   Main file


def plus(*numbers):
    result:int = numbers[0]
    for i in range(1, len(numbers)):
        result += numbers[i]
    return result

def minus(*numbers):
    result:int = numbers[0]
    for i in range(1, len(numbers)):
        result -= numbers[i]
    return result

def multiply(*numbers):
    result:int = numbers[0]
    for i in range(1, len(numbers)):
        result *= numbers[i]
    return result

def divide(*numbers): 
    result:int = numbers[0]
    for i in range(1, len(numbers)):
        result //= numbers[i]
    return result

def dividef(*numbers): 
    result:int = numbers[0]
    for i in range(1, len(numbers)):
        result /= numbers[i]
    return result

def divreminder(*numbers):
    result:int = numbers[0]
    for i in range(1, len(numbers)):
        result %= numbers[i]
    return result

def degree(*numbers):
    result:int = numbers[0]
    for i in range(1, len(numbers)):
        result **= numbers[i]
    return result

