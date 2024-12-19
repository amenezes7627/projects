# part 1
fp = open("day6.txt")
map = [list(line.strip()) for line in fp.readlines()]
count = 0
num_rows = len(map)
num_cols = len(map[0])
r = 0
c = 0

for i in range(num_rows):
    for j in range(num_cols):
        if map[i][j] == '^':
            r = i
            c = j
            map[i][j] == 'X'
            count += 1
            break

def check_bounds(i, j):
    global count
    row = i >= 0 and i < num_rows
    col = j >= 0 and j < num_cols
    if not (row and col):
        for row in map:
            print("".join(row))
        print(count)
        exit()
    return (row and col)

def turn(r, c):
    global count
    global map
    obj = '#'
    # up
    while (check_bounds(r - 1, c) is True and map[r - 1][c] != obj):
        if (map[r - 1][c] != 'X'):
            count += 1
            map[r - 1][c] = 'X'
        r -= 1
        
    # right
    while (check_bounds(r, c + 1) is True and map[r][c + 1] != obj):
        if (map[r][c + 1] != 'X'):
            count += 1
            map[r][c + 1] = 'X'
        c += 1

    # down
    while (check_bounds(r + 1, c) is True and map[r + 1][c] != obj):
        if (map[r + 1][c] != 'X'):
            count += 1
            map[r + 1][c] = 'X'
        r += 1

    # left
    while (check_bounds(r, c - 1) is True and map[r][c - 1] != obj):
        if (map[r][c - 1] != 'X'):
            count += 1
            map[r][c - 1] = 'X'
        c -= 1
    return r, c

while True:
    r, c = turn(r, c)

# part 2