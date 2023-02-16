
def greet_user(first_name: str, last_name: str=None): # specified the type of input we want, we get warning if we not give coorect input
    """
    A function to print first and last name
    :param first_name: the first name of the person (str)
    :param last_name: the last name of the person (str)
    :return: None
    """
    print("Hello, ", first_name, last_name)


def f(x):
    y = x * x
    return y