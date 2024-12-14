import re

# part 1
fp = open("day3.txt")
lines = fp.readlines()
input = ""
for line in lines:
    input += line
input = re.sub(r'[^a-zA-Z0-9(),]', '', input)
pattern = r"mul\((\d+),(\d+)\)"
matches = re.findall(pattern, input)
sum = 0
count = 0
for x in matches:
    sum += int(x[0]) * int(x[1])
    count += 1
print(sum)

# part 2
str2 = ""
for line in lines:
    str2 += line
str2 = re.sub(r'[^a-zA-Z0-9(),]', '', str2)   
flags = r"(do\(\)|dont\(\))"
matches2 = re.split(flags, str2)
new_sum = 0
do = True
for segment in matches2:
    if segment == "do()":
        do = True
    elif segment == "dont()":
        do = False
    else:
        if do:
            seg_matches = re.findall(pattern, segment)
            for x in seg_matches:
                new_sum += int(x[0]) * int(x[1])
print(new_sum)