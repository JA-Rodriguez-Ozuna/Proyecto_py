students_grades = {"marry": 9.1, "sim": 8.8, "jose": 7.6}

for students in students_grades.items():
    print(students)

for students in students_grades.keys():
    print(students)

for students in students_grades.values():
    print(students)

'''
Dictionary Loop and String Formatting
Here is an example that combines a dictionary loop with 
string formatting. The loop iterates over the dictionary 
and it generates and prints out a string in each iteration:
'''
phone_numbers = {"John": "+37682929928", "Marry": "+423998200919"}
 
for pair in phone_numbers.items():
    print(f"{pair[0]} has as phone number {pair[1]}")

#And here is a better way to achieve the same results by iterating over keys and values:

phone_numbers = {"John": "+37682929928", "Marry": "+423998200919"}
 
for key, value in phone_numbers.items():
    print(f"{key} has as phone number {value}")

'''
In both cases, the output is:

John has as phone number +37682929928

Marry has as phone number +423998200919
'''

"""
Loop Over Dictionary and Replace
Loop over the phone_numbers values and in 
each loop print out the phone number, but with '00' 
instead of '+'. In other words, your code should output:

0037682929928
00423998200919

Hint: You can access dictionary values with 
phone_numbers.values() and you can replace 
characters using str.replace() .
"""
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for values in phone_numbers.values():
    print(values.replace("+", "00"))
  