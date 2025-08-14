def area(a, b ):
    return a * b

print(area(5, 10)) # 50

# Functions with an Arbitrary Number of Non-keyword Arguments
def mean(*args):
    return sum(args) / len(args) #the type of the args is a tuple

print(mean(1, 2, 3, 4, 5)) # 3.0
print(mean(10, 20, 30)) # 20.0

'''
Indefinite Number of Strings Processed (E)
Define a function that takes an indefinite number of strings as parameters 
and returns a list containing all the strings in UPPERCASE and sorted alphabetically. 
For example, if I called your function with foo("snow", "glacier", "iceberg") 
it should return ["GLACIER", "ICEBERG", "SNOW"].
'''
def foo(*args):
    list_sorted = list(sorted(args))
    return [x.upper() for x in list_sorted] 
    
print(foo("snow", "glacier", "iceberg"))

#Functions with an Arbitrary Number of Keyword Arguments
def print_args(**kwards):
    return kwards       # the type of the kwards is a dictionary                                
print(print_args(a=1, b=2, c=3)) # {'a': 1, 'b': 2, 'c': 3}

'''
Indefinite Number of Keyword Arguments (E)
Enter the correct parameters inside find_sum() 
so that the output of the code is 9.
'''
def find_sum(**kwargs):
    return sum(kwargs.values())
print(find_sum(a=3, b=3, c=3)) # 9
