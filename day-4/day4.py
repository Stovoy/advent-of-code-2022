import utils

lines = utils.read_input_lines()

result_a = 0
result_b = 0
for line in lines:
    a, b = line.split(',')
    a1, a2 = a.split('-')
    b1, b2 = b.split('-')
    a1 = int(a1)
    a2 = int(a2)
    b1 = int(b1)
    b2 = int(b2)

    if (a1 >= b1 and a2 <= b2) or (b1 >= a1 and b2 <= a2):
        result_a += 1

    if (a1 <= b1 <= a2) or (b1 <= a1 <= b2):
        result_b += 1

print(result_a)
print(result_b)
