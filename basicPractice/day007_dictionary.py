meow = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6
}
for me in meow:
    print("%s:::%d" % (me, meow[me]))
meow["four"] = 41234123
print(meow)
print(meow.get("four", 2222))
print(meow.get("xxx", 12))
print(meow.popitem())
print(meow.pop("five", 2333))
print(meow)

