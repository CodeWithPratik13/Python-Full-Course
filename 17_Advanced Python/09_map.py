number = [1, 2, 3, 34, 24, 52]

def square(x):
    return x * x


new = list(map(square, number))
print(new)