#list_comprehensions with if condition and else condition
temps2 = [230, 240, 250, -260, 270, 280, 290, 300]
new_temps = [temp / 10  if temp != -260 else 0 for temp in temps2]
print(new_temps)
#output: [23.0, 24.0, 25.0, 0, 27.0, 28.0, 29.0, 30.0]


#Zeros Instead (E)
'''
Define a function that takes as parameter a list that contains 
both numbers and strings and returns the same list but with 
zeros instead of strings. For example, I called your function 
with foo([99, 'no data', 95, 94, 'no data']) it should 
return [99, 0, 95, 94, 0].
'''
def foo(lists):
    lists_results = [x if not isinstance(x , str) else 0 for x in lists] #meaning “si x no es un string, déjalo tal cual; si es un string, pon 0”.
    return lists_results

print(foo([99, 'no data', 95, 94, 'no data']))