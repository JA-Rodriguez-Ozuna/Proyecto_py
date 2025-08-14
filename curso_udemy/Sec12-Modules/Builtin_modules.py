import time

while True:

    with open("Aprendiendo/APRENDIENDO.PY/curso_udemy/Sec12-Modules/Vegetables.txt",) as file:
        content = file.read()
        print(content)
        time.sleep(10)
#como parar el bucle infinito: Ctrl + C o Ctrl + Z