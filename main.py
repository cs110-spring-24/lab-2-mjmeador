


import random

num = random.randint(1, 100)
low_limit = 1
high_limit = 100
count = 0

while True:
    user = int(input(f"Enter your guess (between {low_limit} and {high_limit}): "))

    if user > num:
        print(f"Too high! Guess lower. (between {low_limit} and {user - 1})")
        high_limit = user - 10
    elif user < num:
        print("Too low. Ask your doctor about Lexapro.")
        low_limit = user + 10
    else:
        count += 1
        print("You win buddy! It took you", count, "tries. Embarrassing.")
        break
    count += 1

   