def meow():
    print("meow from module1")


def gcd(x, y):
    if x > y:
        (x, y) = (y, x)
    for factor in range(x, 0, -1):
        if (x % factor == 0) & (y % factor == 0):
            return factor


def lcm(x, y):
    gd = gcd(x, y)
    return x * y // gd

def isPalindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10
        total += temp % 10
        temp = temp // 10
    return total == num


def isPrime(num):
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True if num != 1 else False


def main():
    if (isPalindrome(131) & isPrime(131)):
        print("%d is Prime and palindrome" % 131)


if __name__ == "__main__":
    print("now this file is main file")
    main()
else:
    print("now this file as a module file")
