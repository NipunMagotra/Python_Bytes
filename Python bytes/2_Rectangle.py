def rectangle(name, surname):
    name_length = len(name)
    surname_length = len(surname)
    
    
    print("#" * name_length)
    for i in range(surname_length - 2):
        print("#" + "#" * (name_length - 2) + "#")
    print("#" * name_length)
    
    
    print("#" * name_length)
    for i in range(surname_length - 2):
        print("#" + " " * (name_length - 2) + "#")
    if surname_length > 1:
        print("#" * name_length)
rectangle("Nipun Magotra")
