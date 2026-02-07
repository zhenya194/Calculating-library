#                   Main file


def plus(firstNumber, secondNumber):
    result:int = firstNumber + secondNumber
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
    result = firstNumber * secondNumber
    return result

def divide(firstNumber, secondNumber):
    pass
