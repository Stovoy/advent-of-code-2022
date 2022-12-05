def read_input_lines(strip=False):
    with open('input.txt') as file:
        lines = []
        for line in file.readlines():
            lines.append(line)
    return lines


def chunks(arr, n):
    for i in range(0, len(arr), n):
        yield arr[i:i + n]


def flatten(nested_list):
    return [item for sublist in nested_list for item in sublist]


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def rotate(matrix, clockwise=True):
    return transpose(matrix[::-1] if clockwise else matrix[:])


def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
