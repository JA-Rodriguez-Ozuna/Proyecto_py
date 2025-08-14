'''
Define a function that:

(1) takes a string as a parameter

(2) returns False if the string contains less than 8 characters

(3) returns True if the string contains 8 or more characters

In other words, if I called your function with foo("mypass") 
it would return False. If I called it with foo("mylongpassword") 
it would return True, and so on.
'''
def foo(string):
    if len(string) < 8:
        return False
    else:
        return True
    
print(foo("mylongpassword")) #this return True


#What would the following code output?
def foo(x, array):
    if x in array:
        return True
    else:
        return False
 
print(foo(1, [1, 2, 3]))
print(foo(1, [2, 3]))
print(foo(1, ['1', 2, 3]))

#functions and conditionals
'''
In this section, you learned to:



Define functions:

def cube_volume(a):
    return a * a * a


Write if-else conditionals:

message = "hello there"
 
if "hello" in message:
    print("hi")
else:
    print("I don't understand")


Write if-elif-else conditionals:

message = "hello there"
 
if "hello" in message:
    print("hi")
elif "hi" in message:
    print("hi")
elif "hey" in message:
    print("hi")
else:
    print("I don't understand")


Use the and operator to check if both conditions are True at the same time:

x = 1
y = 1
 
if x == 1 and y==1:
    print("Yes")
else:
    print("No")


Use the or operator to check if at least one condition is True:

x = 1
y = 2
 
if x == 1 or y==2:
    print("Yes")
else:
    print("No")


Check if a value is of a particular type with isinstance:

isinstance("abc", str)
isinstance([1, 2, 3], list)
or directly:

type("abc") == str
type([1, 2, 3]) == lst
'''
