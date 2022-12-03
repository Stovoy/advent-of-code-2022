def read_input_lines():
    with open('input.txt') as file:
        lines = []
        for line in file.readlines():
            lines.append(line.strip())
    return lines


def chunks(arr, n):
    for i in range(0, len(arr), n):
        yield arr[i:i + n]
