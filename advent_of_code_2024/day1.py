# part 1
fp = open("input.txt")
list1 = []
list2 = []
for line in fp.readlines():
    x = line.split()
    list1.append(int(x[0]))
    list2.append(int(x[1]))

list1.sort()
list2.sort()
sum = 0
for i in range(len(list1)):
    dist = abs(list1[i] - list2[i])
    sum += dist
    
print(sum)

# part 2
sim_score = 0;
for num in list1:
    count = list2.count(num)
    sim_score += num * count

print(sim_score)