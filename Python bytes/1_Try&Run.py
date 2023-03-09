namestring=input()
print(namestring,"has length",len(namestring))
nameParts= namestring.split(" ")
parts = len(nameParts)
for i in range(0,parts,1):
    print(i,nameParts[i],"has length",len(nameParts[i]))
print(namestring)
for i  in range(len(namestring)):
    if namestring[i]!=" ":
        print("*", end="")
    else:
        print(" ",end="")
print()
