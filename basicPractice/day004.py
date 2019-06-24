import random
sum = 0
for x in range(0, 100, 2):
    sum += x
print(sum)

answer = random.randint(0, 100)
cnt = 0
while True:
    print("input your guess number:")
    guess = int(input("guess="))
    cnt += 1
    if guess > answer:
        print("smaller.")
    elif guess < answer:
        print("bigger.")
    else:
        print("you are right")
        break
print("you guess %d times." % cnt)
