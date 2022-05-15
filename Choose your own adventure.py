#Name:
name = input("Type your name: ")
print("Hi", name, "welcome to your adventure")

#First Question:
q1 = input("You are on a dirt road, it has ust come to and end. Would you like to go left or right?: ").lower()


if q1 == "left":
    q2 = input("You've chosen to go left. You've just arrived at a river and have been given another option: Would you like to swim across or would you like to go around it?: ").lower()
elif q1 == "right":
    print("You died because you're a noob")
#Answer1:
if q2 == "swim":
    q3 = input("""You were able to successfully swim across however, when you reached the other side you noticed that you'd been wearing your clothes across and had now become very cold.
    Would you like to sit down and make a fire to warm up or would you like to continue your journey saving you time?: """).lower()
elif q2 == "go around":
    q3 = input("""Although it took many more hours than climbing it was much more worth it since you stopped yourself from getting in those rapids. Now you're at the top of the hill would you like to:
    Rest for the night or would you like to continue your journey throughout the night?: """).lower()
else:
    print("NOT A VALID OPTION")

#Question 3:
if q3 == "make a fire":
    q4 = input("""You built yourself a sleeping area out of wood and leave whilst your sat around your fire in the hopes of warming yourself up.
     When you woke up you went out for a walk and stumbled into a old abandoned looking house.
      Do you take a look inside for supplies or do you go and try to find other things around?""").lower()
elif q3 == "continue":
     print("You continued your journey throughout the night however you got malled by a mountain lion (You Died)")

else:
    print("NOT A VALID OPTION")

#Question 4:
if q4 == "look for supplies":
    q5 = input("""You had a look around the house and found some old canned food however it's 2years out of date.
    Will you still eat it?""").lower()
elif q4 == "go look around":
    q5 = input("""You went for a 2mile walk around however saw nothing
    Do you continue your journey or head back to camp?""").lower()

else:
    print("NOT A VALID OPTION")

#Question 5:
if q5 == "eat it":
    print("You were okay at first however when you got back to camp you realised that you were feeling really ill. You threw up ur guts and died")
elif q5 == "continue":
    print("You ended up dying because you fell off a cliff :)")
elif q5 == "Head back to camp":
    q6 = input("""You went back to camp. Living another day. The next morning you gave yourself two options:
    Stay at the camp and rest up for another day or go explore the opposite direction to the place where we found the house""").lower()

else:
    print("NOT A VALID OPTION")

#Question 6:
if q6 == "rest":
    print("You were bitten by a snake in your sleep and the venom got to your heart and killed you")
elif q6 == "explore":
    q7 = input("""You rested for another day and decided to go back out the next morning. When you wake up you're offered the same options:
         Stay at the camp and rest up for another day or go explore the opposite direction to the place where we found the house""").lower()

else:
    print("NOT A VALID OPTION")

#Question 7:
if q7 == "rest":
    print("You reached the end of the game and died")
elif q7 == "explore":
    print("You reached the end of the game and died")

else:
    print("NOT A VALID OPTION")
print("Thank you for playing!")
