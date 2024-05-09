# Example code
count = 0
total = 0
avg = 0
while True:
    s = int(input("please enter score"))
    if s == -100:
        break
    elif s > 100:
        print("too big")
    elif s < 0:
        print("too small")
    elif s >= 90:
        print("A")
    elif s >= 80:
        print("B")
    elif s >= 70:
        print("C")
    elif s >= 60:
        print("D")
    else:
        print("F")
    if s <= 100 and s >= 0:
        count = count + 1
        total = total + s

print("Finish")
print("Count is ", count)
print("Total is ", total)
avg = total / count
avg = round(avg, 2)
print("average is ", avg)