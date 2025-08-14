def mean(mylist): #def-nombre_funcion-(opcional-parametro-(variable-entrada))
    the_mean = sum(mylist) / len(mylist) 
    return the_mean # retorna la funcion

print(mean([1,2,3]))# con el nombre de la funcion llamamos la funcion

'''
 example of a function that converts an amount of money from one currency to another assuming the conversion rate today is 1.75.
'''
def convert(money):
    amount = money * 63
    return amount 

print(convert(100))

'''
If Conditional Example- functions that can print the mean of diccionary and list
'''

def mean2(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean

monday_temperature = [8.8, 9.1, 9.9]
students_grades = {"Maarry": 9.1, "Simon": 8.8, "Jhon": 7.5}
print("mean_of_list")
print(mean2(monday_temperature))
print()
print("mean_of_diccionary")
print(mean2(students_grades))