# 这是一个计算从1加到n的和的程序：
n = 0
total = 0
# 输入要计算的和的上限r
r = int(input("Enter the value n [1+2+3+...+n]"))
# 循环变量n从1开始，直到r为止
while n<r:
    # n加1
    n=n+1
    # total加上n
    total = total + n
# 输出和
print(total)
