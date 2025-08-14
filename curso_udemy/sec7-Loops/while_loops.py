username = ''

while username != "python":
    username = input("Enter the user:")
    if username != "python":
        print("Incorrect")
    else:
        print("success")

#another way to do it!
while True:
    username = input("Enter the user:")
    if username == "pypy":
        break
    else:
        continue

a = 0
while a < 5:
    a = a + 1
    print(a)










