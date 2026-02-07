#                   Main file


def plus(*numbers):
    result:int = numbers[0]
    i:int = 1
    for i in range(len(numbers)):
        result += numbers[i]
    return result

def minus(*numbers):
    result:int = numbers[0]
    i:int = 1
    for i in range(len(numbers)):
        result -= numbers[i]
    return result

def multiply(*numbers):
    result:int = numbers[0]
    i:int = 1
    for i in range(len(numbers)):
        result *= numbers[i]
    return result

def divide(*numbers): 
    result:int = numbers[0]
    i:int = 1
    for i in range(len(numbers)):
        result //= numbers[i]
    return result

