def fib(x: int) -> int:
    x1 = 0
    x2 = 1
    for i in range(x):
        x1, x2 = x2, x1 + x2
    return x1


def fib3(x: int) -> int:
    if x == 1:
        return 1
    else:
        return fib3(x-1) + x

print(fib(4))
print(fib3(3))
