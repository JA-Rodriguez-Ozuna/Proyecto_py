def count_character_in_file(character, filepath):  
    with open(filepath, 'r', encoding='utf-8') as Myfile:
        content = Myfile.read()
        return content.count(character)

# Ejemplo de uso
print(count_character_in_file("a", "Aprendiendo/APRENDIENDO.PY/curso_udemy/Sec11-File precessing/bear.txt"))
        
