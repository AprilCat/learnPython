import math
num = int(input("input="))
sqrt_num = int(math.sqrt(num))
isPrime = 1
for x in range(2, sqrt_num+1):
    if num % x == 0:
        isPrime = 0
        break
if isPrime:
    print("%d is prime" % num)
else:
    print("%d is not prime" % num)

