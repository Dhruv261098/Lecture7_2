import my_functions # import the whole file (or library)
from my_functions import greet_user, f # import the functions that I want
import calculator


print(greet_user.__code__.co_varnames) # show the variable name
print(greet_user.__code__.co_nlocals) # show the number of local variables (private)

calculator.my_calculator(4,6) # when we call function from directly file then we have to specify that (file name. function)