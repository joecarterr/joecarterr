#Welcome Message:
print("Hello there and welcome to my quiz")

play = input("Would you like to start? ")

score = 0

#Giving Commands Different Values
if play.lower() == "yes":
    print("Okay, we can now begin")

if play == "no":
    print("Thank you!!!")
    quit()

#Question One
answer = input("Who is Elon Musk? ")
answer1 = "He is the CEO of both SpaceX and Tesla"

if answer == "He is the CEO of both SpaceX and Tesla":
    print("Well done you got that correct!!!")
    score += 1

else:
    print("""\nSorry this is wrong,
this is the real answer: """)
    print(answer1)

#Second Question:
answer = input("\nWho is Mark Zuckerberg?: ")
answer2 = "He is the CEO of FaceBook"

if answer == "He is the CEO of FaceBook":
    print("Well done you got that correct!!!")
    score += 1

else:
    print("""\nSorry this is wrong,
this is the real answer: """)
    print(answer2)

#Third Question:
answer = input("\nWho is Jordan Belfort?: ")
answer3 = "He is known as The Wolf Of Wall Street"

if answer == "He is known as The Wolf Of Wall Street":
    print("Well done you got that correct!!!")
    score += 1

else:
    print("""\nSorry this is wrong,
this is the real answer: """)
    print(answer3)

#Fourth Question:

answer = input("\nWho is Bill Gates?: ")
answer4 = "He is mainly known for being the founder of Microsoft"

if answer == "He is mainly known for being the founder of Microsoft":
    print("Well done you got that correct!!!")
    score += 1

else:
    print("""\nSorry this is wrong,
this is the real answer: """)
    print(answer4)

#Answers Correct And Percent
print("\n")
print("You got " + str(score) + " correct!")
print("\nAs a percentage you got: " + str((score/4)*100) + "%")
