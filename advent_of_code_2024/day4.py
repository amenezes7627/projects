# part 1
fp = open("day4.txt")
lines = [line.strip() for line in fp.readlines()]
num_rows = len(lines)
num_cols = len(lines[0])
word = "XMAS"
count = 0

def check_bounds(i, j):
    row = i >= 0 and i < num_rows
    col = j >= 0 and j < num_cols
    return (row and col)

def check_right(i, j):
    global count
    result = "X"
    c = 1
    while (check_bounds(i, j + c) and c < 4):
        result += lines[i][j + c]
        c += 1
    if (result == word):
        count += 1
    return

def check_back(i, j):
    global count
    result = "X"
    c = 1
    while (check_bounds(i, j - c) and c < 4):
        result += lines[i][j - c]
        c += 1
    if (result == word):
        count += 1
    return

def check_up(i, j):
    global count
    result = "X"
    c = 1
    while (check_bounds(i - c, j) and c < 4):
        result += lines[i - c][j]
        c += 1
    if (result == word):
        count += 1
    return

def check_down(i, j):
    global count
    result = "X"
    c = 1
    while (check_bounds(i + c, j) and c < 4):
        result += lines[i + c][j]
        c += 1
    if (result == word):
        count += 1
    return

def check_leftupdiag(i, j):
    global count
    result = "X"
    c = 1
    while (check_bounds(i - c, j + c) and c < 4):
        result += lines[i - c][j + c]
        c += 1
    if (result == word):
        count += 1
    return

def check_rightupdiag(i, j):
    global count
    result = "X"
    c = 1
    while (check_bounds(i - c, j - c) and c < 4):
        result += lines[i - c][j - c]
        c += 1
    if (result == word):
        count += 1
    return

def check_leftdowndiag(i, j):
    global count
    result = "X"
    c = 1
    while (check_bounds(i + c, j + c) and c < 4):
        result += lines[i + c][j + c]
        c += 1
    if (result == word):
        count += 1
    return

def check_rightdowndiag(i, j):
    global count
    result = "X"
    c = 1
    while (check_bounds(i + c, j - c) and c < 4):
        result += lines[i + c][j - c]
        c += 1
    if (result == word):
        count += 1
    return

for i in range(num_rows):
    for j in range(num_cols):
        if (lines[i][j] == 'X'):
            check_right(i, j)
            check_back(i, j)
            check_up(i, j)
            check_down(i, j)
            check_leftupdiag(i, j)
            check_rightupdiag(i, j)
            check_leftdowndiag(i, j)
            check_rightdowndiag(i, j)

print(count)

# part 2

def x_bounds(i, j):
    if (i >= 0) and (i < num_rows) and (j >= 0) and (j < num_cols):
        if (i - 1 >= 0) and (i + 1 < num_rows) and (j - 1 >= 0) and (j < num_cols):
            return True    
    return False

count2 = 0
for i in range(1, num_rows - 1):
    for j in range(1, num_cols - 1):
        UL = lines[i-1][j-1]
        UR = lines[i-1][j+1]
        BL = lines[i+1][j-1]
        BR = lines[i+1][j+1]
        if(lines[i][j] == 'A'):
            # check left
            if (UL == 'M' and BL == 'M' and UR == 'S' and BR == 'S'):
                count2 += 1
            # check top
            elif (UL == 'M' and UR == 'M' and BL == 'S' and BR == 'S'):
                count2 += 1
            # check right
            elif (UR == 'M' and BR == 'M' and BL == 'S' and UL == 'S'):
                count2 += 1
            # check bottom
            elif (BR == 'M' and BL == 'M' and UL == 'S' and UR == 'S'):
                count2 += 1

print(count2)
