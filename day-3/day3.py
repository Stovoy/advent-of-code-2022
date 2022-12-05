import string
import utils

priorities = {k: i + 1 for i, k in enumerate(string.ascii_lowercase + string.ascii_uppercase)}

lines = utils.read_input_lines(strip=True)

result = 0
for line in lines:
    half = len(line) // 2
    a = line[half:]
    b = line[:half]
    intersection = set(a).intersection(set(b))
    result += priorities[list(intersection)[0]]
print(result)

result = 0
for group in utils.chunks(lines, 3):
    intersection = set.intersection(*[set(line) for line in group])
    result += priorities[list(intersection)[0]]
print(result)
