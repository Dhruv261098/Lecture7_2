# how to call function from function

def multiplication(x:float, y:float):
    """
    Multipling two numbers
    :param x:  first number
    :param y:  second number
    :return: first * second number
    """
    c = x * y
    return c

def substraction(x,y):
    c = x - y
    return c

def my_calculator(a,b):
    print('multiplication result: ', multiplication(x=a, y=b)) # called function inside function
    print('substraction result: ', substraction(x=a,y=b))

my_calculator(3,2)


