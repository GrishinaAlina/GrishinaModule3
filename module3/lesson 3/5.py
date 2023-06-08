# (2x + 3y < A) ∨ (x ≥ y) ∨ (y > 24)
for A in range(1000):
    f = True
    for x in range(1000):
        for y in range(1000):
            if not ((2 * x + 3 * y < A) or (x >= y) or (y > 24)):
                f = False
                break
        if not f:
            break
    else:
        print(A)
        break

