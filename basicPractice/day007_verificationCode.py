import random


def generateVerificationCode(length):
    charSet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    code = ""
    for _ in range(length):
        num = random.randint(0, len(charSet)-1)
        code = code + charSet[num]
    return code


print(generateVerificationCode(5))

