def pattern3():
    size = input()
    print("capsule namelength",len(size))
    print("filled hexagon of side",len(size))
    fill_char = "*"
    num_spaces = (len(size)*2-1)
    for i in range(len(size)):
        num_chars = len(size)+i*2
        num_row_spaces = num_spaces - num_chars // 2
        print(" " * num_row_spaces, end="")
        print(fill_char * num_chars)
    for i in range(len(size)-1,0,-1):
        num_chars = len(size)+i*2 - 2
        num_row_spaces = num_spaces - num_chars // 2
        print(" " * num_row_spaces, end="")
        print(fill_char * num_chars)
pattern3()