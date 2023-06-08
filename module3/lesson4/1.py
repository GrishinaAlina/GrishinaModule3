def m(n, s, f):
    if n > 0:
        t = 5 - s - f
        m(n - 1, s, t)
        print("gtht", n, "sdf", s, "sfd", f)
        m(n - 1, t, f)


m(3, 1, 3)
