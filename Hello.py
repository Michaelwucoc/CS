while True:
    S = int(input("Enter your grade"))
    if S > 100:
        print("too big")
    elif S == -66:
        break
    elif S < 0:
        print("too small")
    elif S >= 90:
        print("A")
    elif 90 > S >= 80:
        print("B")
    elif 80 > S >= 70:
        print("C")
    elif not (not (S < 70) or not (S >= 60)):
        print("D")
    else:
        print("F")


