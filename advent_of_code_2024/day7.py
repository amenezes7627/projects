# part 1
import itertools

def op_combos(n):
    ops = list(itertools.product('*+', repeat=n))
    return ops

def check_operators(num_ops, ans, eq):
    op = {'*': lambda x, y: x * y,
        '+': lambda x, y: x + y}
    ops = op_combos(num_ops - 1)
    for combo in ops:
        temp = 1


fp = open("day7.txt")
lines = fp.readlines()
sum = 0
for line in lines:
    line.strip(':')
    eq = line.split()
