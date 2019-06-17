import random
print("Hello. what is your name!")
x = input()
y = random.randint(1,20)
print("well, " + x + ",I am thinking the number is between  to 1 to 20")

for z in range(1, 7):
    print("Take a guess")
    a = int(input())
    if a < y :
        print("Your guess is too low!")
    elif a > y:
        print("Your guess is too high!")
    else:
        break

if a == y :
    print("Good job " + x + " You guess my number in " + str(z))
else:
    print("Nope the number I was thinking of was  " + str(y))
    
