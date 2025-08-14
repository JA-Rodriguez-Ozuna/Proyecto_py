monday_temperatures = [9.1, 8.8, 7.6]

for temperature in monday_temperatures:
    print(round(temperature))

for Letters in "hello":
    print(Letters.title())

#Loop Over Big Colors (E)
'''
Loop over the colors items and print out the item 
in every loop only if the item is greater than 50. So, 
the output of your program would be:
98
54
54
'''
colors = [11, 34, 98, 43, 45, 54, 54]

for items in colors:
    if items > 50: 
        print(items)

'''
Loop Over Integer Colors (E)
Loop over the colors items and print out 
the item in every loop only if the item is an integer. 
So, the output of your program would be:
11
43
54
54
'''
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for items in colors:
    if isinstance(items, int): #isinstance(objeto, clase) objeto: el valor o variable que quieres verificar.
        print(items)                                      #clase: el tipo de dato que estás comprobando (por ejemplo, int, str, float, etc.).

'''
Loop Over Int and Big Colors (E)
Loop over the colors items and print out the item 
in every loop only if the item is an integer and it 
is greater than 50. So, the output of your program would be:
54
54
'''
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for items in colors:
    if (isinstance(items, int) and items > 50):
        print(items)

'''
For Loop Over a Function
A for loop can also be used to execute a function 
multiple times. For example, below we are executing
celsius_to_kelvin three times since there are three items in the iterating list:
'''

def celsius_to_kelvin(celsius):
    return celsius + 273.15

for temperatures in [9.1, 8.8, -270.15]:
    print(celsius_to_kelvin(temperatures)) 