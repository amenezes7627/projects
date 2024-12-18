# part 1
fp = open("day5.txt")
input = fp.read()
sections = input.strip().split("\n\n")
rules = [line.split("|") for line in sections[0].splitlines()]
updates = [list(map(int, line.split(","))) for line in sections[1].splitlines()]
wrong_updates = []

def validate(rules, update):
    pos = {}
    for i, page in enumerate(update):
        pos[page] = i
    for x, y in rules:
        x, y = int(x), int(y)
        if x in pos and y in pos:
            if pos[x] >= pos[y]:
                return False
    return True

sum = 0
for update in updates:
    if validate(rules, update):
        mid = update[len(update) // 2]
        sum += mid
    else:
        wrong_updates.append(update)
        

print(sum)

# part 2
sum2 = 0
for update in wrong_updates:
    remaining = set(update)
    ordered = []

    while remaining:
        placed = False  

        for page in list(remaining):  
            if all(int(x) in ordered for x, y in rules if int(y) == page and int(x) in update):
                ordered.append(page)
                remaining.remove(page)
                placed = True

        if not placed:
            ordered.extend(remaining)
            break

    mid = ordered[len(ordered) // 2]
    sum2 += mid

print(sum2)
