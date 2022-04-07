# Computer Quiz Game
print("Welcome to Computer Quiz")

play = input("Wanna Play? ")
if play.lower() != "yes":
    print("Bye")
    quit()

print("Let's Play!")
score = 0

answer = input("WWW stands for? ")
if answer.lower() == "world wide web":
    print("It's Correct!")
    score += 1
else:
    print("It's Incorrect!")

answer = input("URL stands for? ")
if answer.lower() == "uniform resource locator":
    print("It's Correct!")
    score += 1
else:
    print("It's Incorrect!")

answer = input("RAM stands for? ")
if answer.lower() == "random access memory":
    print("It's Correct!")
    score += 1
else:
    print("It's Incorrect!")

answer = input("CPU stands for? ")
if answer.lower() == "central processing unit":
    print("It's Correct!")
    score += 1
else:
    print("It's Incorrect!")

answer = input("AI stands for? ")
if answer.lower() == "artificial intelligence":
    print("It's Correct!")
    score += 1
else:
    print("It's Incorrect!")

print("You scored " + str((score/5) * 100) + "%.")   #divide by no of questions
print("Thanks for Playing!!")
