#list_comprehensions with if condition
temps2 = [230, 240, 250, -260, 270, -280, 290, 300]

new_temps = [temp / 10 for temp in temps2 if temp > 0]
print(new_temps)

#Only Numbers (E)
'''
Define a function that takes as a parameter a list that contains 
both integers and strings and returns the list containing only 
the integers. For example, if I called your function with 
foo([99, 'no data', 95, 94, 'no data']) it should return 
[99, 95, 94].
'''
def foo(lists):
    list_results = [x for x in lists if isinstance(x, int)]
    return list_results
    
print(foo([99, 'no data', 95, 94, 'no data']))

#Only Positive Numbers (E)
'''
Define a function that takes as parameter list of numbers and 
returns the list containing only the numbers that are greater 
than 0. For example, I called your function with foo([-5, 3, -1, 101]) 
it should return [3, 101].
'''
def foo(lists):
    lists_results = [x for x in lists if x > 0]
    return lists_results
print(foo([-5, 3, -1, 101]))