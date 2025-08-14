#[expresión for elemento in iterable if condición]

temps = [230, 240, 250, 260, 270, 280, 290, 300]

new_temp = [temp / 10 for temp in temps] 

print(new_temp)

nombres = ["Ana", "Luis", "Mario"]
nombres_mayus = [nombre.upper() for nombre in nombres]
print(nombres_mayus)






