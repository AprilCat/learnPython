def main():
    meow = "   c123456789"
    print(meow[1:2])
    print(meow[::-1])
    print(meow.find("123"))
    print(len(meow))
    print(meow.capitalize())
    print(meow.upper())
    print(meow.lower())
    print(meow.startswith("c12"))
    print(meow.endswith("789"))
    print(meow.center(50, "x"))
    print(meow.strip())
    print(meow.isalpha())
    print(meow.isdigit())
    print(meow.isalnum())
    print(meow.strip().rjust(20, "*"))



if __name__ == "__main__":
    main()

