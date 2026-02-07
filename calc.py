#                   Main file


def plus(*numbers):
    numbers:list[int] = []
    result:int = numbers[0]
    for i in numbers:
        result += numbers[i]
    return result

def minus(firstNumber, secondNumber):
    result:int = firstNumber - secondNumber
    return result

def wcminus(firstNumber, secondNumber):
    result:int = firstNumber - secondNumber
    error:str = "Error: answer is negative."
    if secondNumber > firstNumber:
        return error
    else:
        return result

def multiply(firstNumber, secondNumber):
    result:int = firstNumber * secondNumber
    return result

#TODO
def divide(firstNumber, secondNumber): 
    result:int = firstNumber // secondNumber
    return result
