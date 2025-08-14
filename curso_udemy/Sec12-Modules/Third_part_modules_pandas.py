import time
import os
import pandas 

while True:

    if os.path.exists("Aprendiendo/APRENDIENDO.PY/curso_udemy/Sec12-Modules/temps_today.csv"):
        data = pandas.read_csv("Aprendiendo/APRENDIENDO.PY/curso_udemy/Sec12-Modules/temps_today.csv")
        print(data.mean())
    else:
        print("El archivo no existe.")
        break
    time.sleep(10)