def fact3(x: int) -> int:
    print(x)
    if x == 1:
        return 1
    else:
        return fact3(x-1) * x


print(fact3(12))