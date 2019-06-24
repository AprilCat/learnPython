import os
import time

def main():
    content = "1 2 3 4 5 6 7 8 "
    while True:
        os.system("cls")
        print(content)
        time.sleep(0.2)
        content = content[1:]+content[0]


if __name__ == "__main__":
    main()