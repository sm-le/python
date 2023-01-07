import re

with open("data/regex_sum_1038605.txt") as f:
    T = f.read()
    P = "[0-9]+"
    n = re.findall(P,T)
    print(sum([int(a) for a in n]))
