m,n = list(map(int,input().split())) # width, height
p,q = list(map(int,input().split())) # width, height of small patch
col = m // p
row = n // q
a = [] # [width * height] [col * row]
for i in range(m):
    a.append([0] * n)
for i in range(m*n):
    color = input()[1:]
    if len(color) == 6:
        r = eval("0x" + color[:2])
        g = eval("0x" + color[2:4])
        b = eval("0x" + color[4:6])
    elif len(color) == 3:
        r = eval("0x" + color[0])
        g = eval("0x" + color[1])
        b = eval("0x" + color[2])
    elif len(color) == 1:
        r = eval("0x" + color[0])
        g = eval("0x" + color[0])
        b = eval("0x" + color[0])
    a[i//n][i-i//n*n] = ([r,g,b])

print(a)

res = []
for i in range(col):
    res.append([0] * row)
for i in range(col):
    for j in range(row):
        res[i][j] = [0] * 3
        # print(i,j,i*p,(i+1)*p,j*q,(j+1)*q)
        for u in range(i*p,(i+1)*p):
            for v in range(j*q,(j+1)*q):
                for c in range(3):
                    res[i][j][c] += a[u][v][c]
        for c in range(3):
            res[i][j][c] = res[i][j][c] // (p*q)

# print(res)

def get_hex(num):
    # hex_str = "{:0>2d}".format(int(hex(num)[2:])).upper()
    res = ""
    for s in str(num):
        res += "\\x" + "{:0>2d}".format(int(hex(ord(str(int(s))))[2:])).upper()
    return res

# \x1B ESC
# \x5B [
# \x34 4
# \x38 8
# \x3B ;
# \x32 2
# \x6D m
# \x0A \n
# \x20 ' '

curr = [0,0,0]
def change_color(new_color):
    global curr
    if new_color == curr:
        return "\\x20"
    elif new_color == [0,0,0]:
        curr = new_color
        return "\\x1B\\x5B\\x30\\x6D"
    else:
        curr = new_color
        [r,g,b] = new_color
        r,g,b = get_hex(r),get_hex(g),get_hex(b)
        # r,g,b = str(r),str(g),str(b)
        return "\\x1B\\x5B\\x34\\x38\\x3B\\x32\\x3B" + r + "\\x3B" + g + "\\x3B" + b + "\\x6D"

for j in range(row):
    for i in range(col):
        print(change_color(res[i][j]),end="\\x20")
    if curr != [0,0,0]:
        print(change_color([0,0,0]),end="")
    print("\\x0A",end="")
# print()
# print("\\x1B\\x5B\\x34\\x38\\x3B\\x32\\x3B\\x31\\x3B\\x32\\x3B\\x33\\x6D\\x20\\x1B\\x5B\\x30\\x6D\\x0A",end="")
# print("\x1B\x5B\x34\x38\x3B\x32\x3B\x38\x3B\x38\x3B\x38\x6D\x20\x20\x1B\x5B\x30\x6D\x0A",end="")