import time
import os

while True:
    if os.path.exists("Aprendiendo/APRENDIENDO.PY/curso_udemy/Sec12-Modules/Vegetables.txt"):
        with open("Aprendiendo/APRENDIENDO.PY/curso_udemy/Sec12-Modules/Vegetables.txt",) as file:
            content = file.read()
            print(content)
            time.sleep(10)
    else:
        print("El archivo no existe.")
        break