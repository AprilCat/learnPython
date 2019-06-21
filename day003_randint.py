from random import randint


def switch_number(arg):
    switcher = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six"
    }
    print(switcher.get(arg, "invalid parameter"))


number = randint(1, 6)
switch_number(number)
