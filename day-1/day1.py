import utils

lines = utils.read_input_lines(strip=True)

elves = []
current_elf = []
for line in lines:
    if line.strip() == '':
        elves.append(current_elf)
        current_elf = []
    else:
        current_elf.append(int(line))

elves = [sum(elf) for elf in elves]
elves = sorted(elves, reverse=True)
print(elves[0])
print(sum(elves[:3]))
