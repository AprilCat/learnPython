print("please input year")
year = int(input("year="))
isLeap = ((year % 400) == 0) | (((year % 100) != 0) & ((year % 4) == 0))
if isLeap:
    print("%d is leap year" % year)
else:
    print("%d is not leap year" % year)


