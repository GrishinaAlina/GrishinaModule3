import sys
import time
sys.setrecursionlimit(10000)


def r(text):
    if not text:
        return 0
    elif text[0].isdigit():
        # text.pop(0)
        return 1 + r(text[1:])
    else:
        return r(text[1:])


def r2(text):
    s = 0
    for i in text:
        if i.isdigit():
            s += 1
    return s


txt = [x for x in open("test.txt")][0]
#print(txt)

start1 = time.perf_counter()
print(r(txt))
finish1 = time.perf_counter()

start2 = time.perf_counter()
print(r2(txt))
finish2 = time.perf_counter()
print(finish1-start1)
print(finish2-start2)

