import random

random_number = random.randrange(1, 100)
print(f"The answer is: {random_number}")
diff = input("Choose a difficulty. Type easy or medium. ")
user_guess = int(input("Make a guess: "))

if diff == 'easy':
    n = 10
    while n >= 1:
        if user_guess > random_number:
            n -= 1
            print(f"Too high. You have {n} attemtps left.")
            user_guess = int(input("Make a guess: "))
            if n == 1:
                print(f"You ran out of lives. The correct answer is {n}.")
        elif user_guess < random_number:
            n -= 1
            print(f"Too low. You have {n} attemtps left.")
            user_guess = int(input("Make a guess: "))
            if n == 1:
                print(f"You ran out of lives. The correct answer is {n}.")
        else:
            print(f"Correct. The answer is {random_number}")
            n = 0
elif diff == 'hard':
    x = 5
    while x >= 1:
        if user_guess > random_number:
            x -= 1
            print(f"Too high. You have {x} attemtps left.")
            user_guess = int(input("Make a guess: "))
            if x == 1:
                print(f"You ran out of lives. The correct answer is {x}.")
        elif user_guess < random_number:
            x -= 1
            print(f"Too low. You have {x} attemtps left.")
            user_guess = int(input("Make a guess: "))
            if x == 1:
                print(f"You ran out of lives. The correct answer is {x}.")
        else:
            print(f"Correct. The answer is {random_number}")
            x = 0
