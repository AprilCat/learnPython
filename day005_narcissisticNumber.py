a = 0
b = 0
c = 0
for x in range(100, 1000):
    a = x // 100
    b = (x % 100) // 10
    c = x % 10
    if a * a * a + b * b * b + c * c * c == x:
        print("%d" % x)

