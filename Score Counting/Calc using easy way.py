# This code defines a recursive function func1 that calculates the factorial of a number n. If n is 0, it returns 1.
# Otherwise, it multiplies n by the factorial of n-1 recursively.
def func1(n):
    if n == 0:
        return 1
    else:
        return n * func1(n - 1)


first = int(input("Enter the number: "))
result = func1(first)
print(result)

print ("Result")