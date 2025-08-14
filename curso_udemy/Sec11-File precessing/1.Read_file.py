Myfile = open("Aprendiendo/APRENDIENDO.PY/curso_udemy/Sec11-File precessing/fruits.txt", "r")
content = Myfile.read()
print(content)
Myfile.close()

#opening files using with statement
with open("Aprendiendo/APRENDIENDO.PY/curso_udemy/Sec11-File precessing/fruits.txt", "r") as Myfile:
    print(Myfile.read())

#Read the bear.txt file, and print out the first 90 characters of its content.
with open("Aprendiendo/APRENDIENDO.PY/curso_udemy/Sec11-File precessing/bear.txt", "r") as Myfile:
    print(Myfile.read(90))


'''
Write First 90 (E)
Create a first.txt file that contains the first 90 characters of bear.txt.

Note that you should read the content of bear.txt with Python, extract 
its first 90 characters with Python, and write those 
characters in first.txt with Python.

Codigo:
with open("bear.txt") as file:
    content = file.read()

with open("first.txt", "w") as file:
    file.write(content[:90])
'''


'''
#appending text to an existing file
with open("Aprendiendo/APRENDIENDO.PY/curso_udemy/Sec11-File precessing/fruits.txt", "a") as Myfile:
    Myfile.write("\nkiwi\n")
    Myfile.write("mango\n")
    Myfile.write("peach\n")

# if  you want to add and read the file at the same time, you can use "a+" mode
 with open("Aprendiendo/APRENDIENDO.PY/curso_udemy/Sec11-File precessing/fruits.txt", "a+") as Myfile:
     Myfile.write("\nkiwi\n")
     Myfile.write("mango\n")
     Myfile.write("peach\n")
     Myfile.seek(0)  # Move the cursor to the beginning of the file
     content = Myfile.read()
'''

'''
#Read and Append (E)
Append the text of bear1.txt to bear2.txt. 
In other words, bear2.txt should contain its 
text and the text of bear1.txt after that.

Codigo:
with open("bear1.txt") as file:
    content = file.read()
    
with open("bear2.txt", "a") as file:
    file.write(content)with open("bear1.txt") as file:
    content = file.read()
    
with open("bear2.txt", "a") as file:
    file.write(content)
'''


'''
#Copy n-times (E)
The existing content of data.txt looks like this:

1.3, 1.5

2.3, 2.7

Use Python to modify the content of data.txt 
so that its content looks like below:

1.3, 1.5

2.3, 2.7

1.3, 1.5

2.3, 2.7

1.3, 1.5

2.3, 2.7

So, you need to find a way to insert the 
existing content two more times.

# Codigo:
with open("data.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    file.seek(0)
    file.write(content)
    file.write(content)



'''