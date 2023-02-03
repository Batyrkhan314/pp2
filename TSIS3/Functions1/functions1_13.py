'''13. Write a program able to play the "Guess the number" - game, 
where the number to be guessed is randomly chosen between 1 and 20. This is how it should work when run in a terminal:
'''
import random



print("Hellp! What is your name?")
name = input()

print("Well, " + name + ", I am thinking of a number between 1 and 20.")
print("Take a guess.")


state = True
p=1

while state:
    t = random.randint(1,20)
    n = int(input())



    if t != n:
        print("Your guess is too low.")
        print("Take a guess.")
        p+=1
    else:
        print("Good job, KBTU! You guessed my number in " + str(p) +  " guesses!")
        state = False
