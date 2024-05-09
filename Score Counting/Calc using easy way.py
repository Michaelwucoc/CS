# This code defines a recursive function func1 that calculates the factorial of a number n. If n is 0, it returns 1.
# Otherwise, it multiplies n by the factorial of n-1 recursively.
# 这是一个名为 func1 的函数，它接受一个数字 n 作为输入，并根据以下规则进行计算：
# 如果 n = 0，则返回 1
# 如果 n 不等于 0，则返回 n 乘以 func1(n - 1)

def func1(n):
    # 如果 n = 0，则返回 1
    if n == 0:
        return 1
    # 如果 n 不等于 0，则返回 n 乘以 func1(n - 1)
    else:
        return n * func1(n - 1)


first = int(input("Enter the number: "))
result = func1(first)
print(result)

print ("Result")