def get_cusip9(cusip8):
    sum = 0
    for i in range(1, 9):
        c = cusip8[i-1]
        if c.isdigit():
            v = int(c)
        elif c.isalpha():
            p = ord(c.lower()) - 96
            v = p + 9
        elif c == "*":
            v = 36
        elif c == "@":
            v = 37
        elif c == "#":
            v = 38
        else:
            print("invalid cusip")
            exit()
        if i%2 == 0:
            v = v*2
        # print(v)
        sum = sum + int(v/10) + v % 10

    return cusip8 + str((10 - (sum % 10)) % 10)


t = get_cusip9('TC6BNDOJ')
print(t)
