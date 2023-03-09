def yourFunction(name):
    
    name = name.replace(" ", "")
    
    nums = [str(i % 10) for i in range(len(name))]

    print("Diagonal sequence:")
    for i in range(len(name)):
        print(" " * i + name[i] + " " * (len(name) - i - 1) + nums[i])
    
    print("\nCross-diagonal sequence:")
    for i in range(len(name)):
        print(" " * i + nums[i] + " " * (len(name) - i - 1) )
yourFunction("Nipun Magotra")