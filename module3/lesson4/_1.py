def cheat(n: int, s, f):
    global x

    # n = str(n)
    try:
        if not str(n).isdigit():
            raise ImportError
        if n < 0:
            raise ZeroDivisionError
        if n > 0:
            stolb = 6 - s - f
            cheat(n - 1, s, stolb)
            x += 1
            print(f"Перенести диск {n} cо стержня {s} на стержень {f}")
            cheat(n - 1, stolb, f)


    except ImportError:
        print("НО-НО .. пальчики с букв убрал")
    except ZeroDivisionError:
        print("НО-НО .. пальчики с нуля убрал")
    except:
        print("бооль")


x = 0
cheat(5, 1, 3)
print(x)
