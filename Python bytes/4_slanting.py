def yourFunction(name):
    surname = name.split()[-1]
    width = len(name)
    height = len(surname)

    for i in range(height):
        for j in range(i):
            print(" ", end="")
        for j in range(width):
            if i == 0 or i == height+2 or j == 0 or j == width+2:
                print("*", end="")
            else:
                print("*", end="")
        print()


yourFunction("Nipun Magotra")
