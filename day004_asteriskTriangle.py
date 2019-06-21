print("input line number")
line = int(input("line="))
for i in range(0, line):
    for j in range(0, i+1):
        print("*", end="")
    print("")
