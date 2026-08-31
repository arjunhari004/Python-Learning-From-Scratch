#1.Take one integer and print whether it is positive, negative, or zero.

a=0
if(a>0):
    print(a,"is positive")
elif(a<0):
    print(a,"is negative")
else:
    print(a,"is zero")


#2.Take one integer and determine whether it is even or odd.

b=15
if(b%2==0):
    print(b," is even")
elif(b%2==1):
    print(b," is odd")
else:
    print(b,"Condition Not Satisfied")


#3.Take one integer and determine whether it is a single-digit, two-digit, three-digit, or more-than-three-digit number.

c=100
if((c>-10) & (c<10)):
    print(c,"is single digit")
elif((c>9) & (c<100)):
    print(c,"is double digit")
elif((c>99) & (c<1000)):
    print(c,"is triple digit")
else:
    print(c,"more than-three digit number")


#4.Take one integer and print Positive/Negative/Zero. If positive, additionally print Even/Odd using nested if.

d=19
if(d>0):
    print("is positive")
    if(d%2==0):
        print("is even")

#5.Take three numbers and find the second largest number without using max(), min(), sorting, or loops.

e=12
f=14
g=17

if((e>f>g) | (g>f>e)):
    print(f,"is the second largest")
elif((f>e>g)|(g>e>f)):
    print(e,"is the second largest")
elif((f>g>e)|(e>g>f)):
    print(g,"is the second largest")   
else:
    print("not valid")

#6.Take marks as input and print Grade A, B, C, D, or Fail using if-elif.

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")


#7.Take marks and attendance as input. If attendance is below 75, print Not Eligible. Otherwise determine the grade based on marks.

marks = int(input("Enter your marks: "))
attendance = int(input("Enter your attendance: "))

if attendance < 75:
    print("Not Eligible")
elif marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")

#8.Take a year and determine whether it is a leap year using the correct 400/100/4 rules.

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not a Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")

#9.Take three sides and determine whether they can form a valid triangle. If valid, determine Equilateral, Isosceles, or Scalene.

side1 = int(input("Enter side 1: "))
side2 = int(input("Enter side 2: "))
side3 = int(input("Enter side 3: "))

if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
    if side1 == side2 == side3:
        print("Equilateral")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Invalid Triangle")
#10.Take three angles and determine whether they form a valid triangle. If valid, determine Acute, Right, or Obtuse triangle.

angle1 = int(input("Enter angle 1: "))
angle2 = int(input("Enter angle 2: "))
angle3 = int(input("Enter angle 3: "))

if angle1 + angle2 + angle3 != 180 or angle1 <= 0 or angle2 <= 0 or angle3 <= 0:
    print("Invalid Triangle")
elif angle1 == 90 or angle2 == 90 or angle3 == 90:
    print("Right Triangle")
elif angle1 > 90 or angle2 > 90 or angle3 > 90:
    print("Obtuse Triangle")
else:
    print("Acute Triangle")
#11.Take a number and determine whether it is positive/negative/zero, then even/odd, and then classify its number of digits using nested if.

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

    if num < 10:
        print("1 Digit")
    elif num < 100:
        print("2 Digits")
    elif num < 1000:
        print("3 Digits")
    else:
        print("More than 3 Digits")

elif num < 0:
    print("Negative")
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

    if num > -10:
        print("1 Digit")
    elif num > -100:
        print("2 Digits")
    elif num > -1000:
        print("3 Digits")
    else:
        print("More than 3 Digits")

else:
    print("Zero")
    print("Even")
    print("1 Digit")
#12.Create an ATM withdrawal program using balance and withdrawal amount. Check whether the amount is positive, within balance, and a multiple of 100. Use nested if.

#13.Create an electricity bill calculator using these slabs:
#unit is 600
#0-100 units: Rs.2/unit
#101-200 units: Rs.3/unit
#Above 500 units: Rs. 8/unit
#After calculating the bill, print High Bill if the bill is above Rs.2000, otherwise Normal Bill.

#14. Create a salary tax calculator:
#Up to Rs.2,50,000: 0%
#Rs.2,50,001-5,00,000: 5%
#Rs.5,00,001-10,00,000: 20%
#Above Rs.10,00,000: 30%
#Also classify the salary as Low Income, Middle Income, or High Income.

#15. Create a shopping discount calculator:
#Below Rs.1000: No discount
#Rs.1000-4999: 10%
#Rs.5000-9999: 20%
#Rs.10000 and above: 30%
#After discount, check whether the final amount qualifies for free delivery.

#16. Create a login system using username and password. Print Login Successful, Wrong Password, or User Not Found using nested if.

#17. Create a movie ticket calculator using age and day. Apply different ticket prices/discounts based on age groups and add a Sunday surcharge.

#18. Create a railway ticket fare calculator using age, ticket type, and distance. Apply age-based discounts, ticket-type pricing, and distance surcharge using nested if.

#19. Create a number analyzer using one integer. Print Positive/Negative/Zero, digit classification, and Even/Odd. Do not use loops, len(), abs(), max(), or min().

#20. Create a student result program using marks and attendance. Validate marks first, check attendance, then print the appropriate result and grade.

#21. Create a bank loan eligibility program using salary, age, and credit score. Use nested if to determine whether the applicant is eligible.

#22. Create a mobile recharge plan selector using age and recharge amount. Apply different benefits based on the amount and age group.

#23. Create a restaurant billing program using bill amount and customer type. Apply different discounts and then determine whether free delivery is available.

#24. Create a parking fee calculator using vehicle type and parking hours. Use nested if to calculate the final fee.

#25. Create a hospital billing program using patient age and treatment type. Apply different discounts based on age and treatment category.

#26. Create a water usage bill calculator using consumed litres and customer type. Apply different rates and additional charges using nested if.

#27. Create a final-score evaluator using marks, attendance, and assignment completion. The student must satisfy multiple conditions to be eligible for the final result.