print("please input two number")
a = int(input("a="))
b = int(input("b="))
maxFactor = 1
if a > b:
    a, b = b, a
for x in range(a, 0, -1):
    if (a % x == 0) & (b % x == 0):
        maxFactor = x
        break
print("greatest common divisor of %d and %d is %d" % (a, b, maxFactor))
print("least common multiple of %d and %d is %d" % (a, b, a * b // maxFactor))

