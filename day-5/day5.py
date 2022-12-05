import collections
import utils

lines = utils.read_input_lines()

columns_1 = collections.defaultdict(list)
columns_2 = collections.defaultdict(list)
for line in lines:
    if line.startswith(" 1"):
        pass
    elif line.startswith(" ") or line.startswith("["):
        line = line.replace("    ", " ")
        # Stack line
        stacks = line.split(" ")
        for i, stack in enumerate(stacks):
            stack = stack.strip()
            if stack == '':
                continue
            stack = stack[1]
            columns_1[i+1].append(stack)
            columns_2[i+1].append(stack)
    elif line.startswith("move"):
        # Parse integers from a string like "move 10 from 9 to 5"
        line = line.strip()
        line = line.replace("move ", "")
        line = line.replace("from ", "")
        line = line.replace("to ", "")
        line = line.split(" ")
        line = [int(x) for x in line]
        amount, column_from, column_to = line
        for i in range(amount):
            # Pop left
            item = columns_1[column_from].pop(0)
            columns_1[column_to].insert(0, item)
        items = columns_2[column_from][:amount]
        columns_2[column_from] = columns_2[column_from][amount:]
        columns_2[column_to] = [*items, *columns_2[column_to]]

text = ''
for i in range(1, 10):
    text += columns_1[i][0]
print(text)

text = ''
for i in range(1, 10):
    text += columns_2[i][0]
print(text)
