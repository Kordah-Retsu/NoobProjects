print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Okay! Lat's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")
    score -= 1
    
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")
    score -= 1
    
answer = input("What does RAM stand for? ")
if answer.lower() == "random access unit":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")
    score -= 1
    
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")
    score -= 1
    
print("You scored" + str(score))