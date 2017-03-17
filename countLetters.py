name = ""

while name == "":
    name = input("Item name: ")
    name = name.strip()
    if name =="":
        print("Input can't be blank")

letterCount = 0

for letter in name:
    letterCount += 1

print("{} has {} letter/s in in it".format(name, letterCount))