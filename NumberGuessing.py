import random;

print("Number Guessing Game")
print("Guess a Number in Between 1 and 9")
number = random.randint(1,9)
for i in range(5):
    guess=int(input("Enter Your Guess"))
    if guess==number:
        print("Congratulations You Won")
        break
    elif guess<number:
        print("Your Guess Was Too Slow, Guess A Higher Number Than",guess)
    else:
        print("Your Number Is Too High, Please Select A Lesser Number Than",guess)
if i > 4:
    print("You Loose")        