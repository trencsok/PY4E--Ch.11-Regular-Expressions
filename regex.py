import re
name = input("Enter file:")
if len(name) < 1:
    name = "regex_sum_1574693.txt"
handle = open(name)
tot = 0

for line in handle:
    line = line.strip()
    numlin = re.findall(('[0-9]+'),line)
    for num in numlin:
        num = int(num)
        tot = tot + num
print(tot)
