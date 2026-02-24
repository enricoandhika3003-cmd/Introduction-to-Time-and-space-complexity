def func(n, m):
    result = n*m
    return result

print(func(2, 3))

def func2(n, m):
    result = 0
    for i in range(n):
        result = result+m
    return result

print(func2(2, 3))