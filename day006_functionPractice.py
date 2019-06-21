from random import randint as rd
import day006_module1 as m1
import day006_module2 as m2



def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += rd(1, 6)
    return total


def add(*args):
    total = 0
    for _ in args:
        total += _
    return total


print(roll_dice())
print(roll_dice(3))
print(add())
print(add(2, 4))
m1.meow()
m2.meow()
print(m1.gcd(6, 9))
print(m1.lcm(6, 9))
print(m1.isPalindrome(12))
