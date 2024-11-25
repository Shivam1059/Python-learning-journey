#question 1
age = 17
if(age >= 18):
    print("vote")
else:
    print("not vote")


#question 2
light = input("light color:")
if (light == "red"):
    print("stop")
elif(light == "yellow"):
    print("redy for driving")
elif(light == "green"):
    print("go")
else:
    print("light is broken")


# question 3
marks = 99
if(marks >= 90):
    print("Grade : A+")
elif(marks >= 75):
    print("Grade : B")
elif(marks >= 60):
    print("Grade : C")
elif(marks >= 33):
    print("Grade : D")
else:
    print("Grade : Fail")


#single Line if / Ternary Operator
food = input("food :")
print("sweet") if food == "cake" or food == "jalebi" else print("not sweet")


#claculate simpale intrest
p = float(input("p : "))
r = float(input("r : "))
t = float(input("t : "))
si = (p*r*t)/100
print(si)