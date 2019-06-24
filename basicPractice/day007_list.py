import sys


def fib(num):
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        yield a



def main():
    list1 = [1, 1, 2, 3, 5, 8, 13, 21]
    print(list1)
    list2 = ["sukaiqi"] * 5
    print(list2)
    list3 = []
    for _ in range(20):
        list3.append("%d times" % _)
    list3.insert(2, "meow")
    list2 += list3
    print(list2)
    list2.clear()
    print(list2)
    list5 = list1[::-1]
    print(list5)
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']
    for _ in fruits:
        print(_.title(), end=",")
    print("")
    print(sorted(fruits))
    print(sorted(fruits, reverse=True))
    print(sorted(fruits, key=len))
    f = [x for x in range(1, 10)]
    g = [x + y for x in "ABCD" for y in "12345"]
    h = [x ** 2 for x in range(1, 1000)]
    h2 = (x ** 2 for x in range(1, 1000))
    print(h)
    print(sys.getsizeof(h))
    print(sys.getsizeof(h2))
    print(g)
    print(f)
    print(h[5])
    for val in h2:
        print(val, end=",")
    for _ in fib(5):
        print(_)
if __name__ == "__main__":
    main()
