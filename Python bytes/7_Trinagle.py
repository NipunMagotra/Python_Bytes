def print_triangle(s):
    length = len(s)
    print(f"{s} Length = {length}\n")
    count = 1
    for i in range(length):
        print(' ' * (length - i - 1), end='')
        for j in range(i+1):
            print(f"{count:02d}", end=' ')
            count += 1
        print()
        if count > 55:
            break

result = print_triangle("NipunMagotra")