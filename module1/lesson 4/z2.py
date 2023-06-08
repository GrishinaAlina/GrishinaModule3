psw1 = input()
if len(psw1) >= 8:
    psw2 = input()
    if psw1 == psw2:
        print("ok")
    else:
        print("Пароли различны")
else:
    print("пароль слишком короткий <8")


