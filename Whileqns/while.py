# # #Get value of n Let n be a 2 digit number
# # #Reverse the number and Check whether the number is magic num or not
# # #0+1--->1(magic number)
# # #7+2---->9 not a magic number


i=0
n=int(input("Enter a number to find the number is magic number or not: "))
s=0
while(i<=n):
    d=n%10
    s=d+s
    n=n//10
    i=i+1
print(s)
f=0
while(i<=s):
    e=s%10
    f=e+f
    s=s//10
    i=i+1
if(s==1):
    print("magic number")
else:
    print("not magic")





#fibonocci series
n=int(input("Enter a number to find fibonocci series: "))
i=2
t1=0
t2=1
print(t1)
print(t2)
while(i<n):
    t3=t1+t2
    print(t3)
    t1=t2
    t2=t3
    i=i+1


#Reverse of a digit


num = int(input("Enter the number to reverse: "))

rev = 0

while(num > 0):
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print(rev)


#factorial

i=1
n=int(input("Enter a number to find the number to find factorial: "))
s=1
while(i<=n):
        s=s*i
        i=i+1
print(s)


#Check whether a number is a palindrome.


num = int(input("Enter the number: "))

original = num
rev = 0

while(num > 0):
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if original == rev:
    print("Palindrome")
else:
    print("Not a palindrome")


#Find the first digit of a number.


num = int(input("Enter the number: "))

while(num >= 10):
    num = num // 10

print("First digit:", num)


#Find the last digit of a number.

num = int(input("Enter the number: "))

digit = num % 10

print("Last digit:", digit)


#Find the largest digit in a number

num = int(input("Enter the number: "))

largest = 0

while(num > 0):
    digit = num % 10

    if digit > largest:
        largest = digit

    num = num // 10

print("Largest digit:", largest)


#29. Find the smallest digit in a number.

num = int(input("Enter the number: "))

smallest = 9

while(num > 0):
    digit = num % 10

    if digit < smallest:
        smallest = digit

    num = num // 10

print("Smallest digit:", smallest)


#30. Count even digits in a number.

num = int(input("Enter the number: "))

count = 0

while(num > 0):
    digit = num % 10

    if digit % 2 == 0:
        count += 1

    num = num // 10

print("Even digits:", count)



#31. Count odd digits in a number.


num = int(input("Enter the number: "))

count = 0

while(num > 0):
    digit = num % 10

    if digit % 2 != 0:
        count += 1

    num = num // 10

print("Odd digits:", count)



#32. Find the sum of even digits.


num = int(input("Enter the number: "))

sum = 0

while(num > 0):
    digit = num % 10

    if digit % 2 == 0:
        sum += digit

    num = num // 10

print("Sum of even digits:", sum)


#33. Find the sum of odd digits.


num = int(input("Enter the number: "))

sum = 0

while(num > 0):
    digit = num % 10

    if digit % 2 != 0:
        sum += digit

    num = num // 10

print("Sum of odd digits:", sum)



#34. Find the product of even digits.


num = int(input("Enter the number: "))

product = 1

while(num > 0):
    digit = num % 10

    if digit % 2 == 0:
        product = product * digit

    num = num // 10

print("Product of even digits:", product)

#35. Find the product of odd digits.

num = int(input("Enter the number: "))

product = 1

while(num > 0):
    digit = num % 10

    if digit % 2 != 0:
        product = product * digit

    num = num // 10

print("Product of odd digits:", product)


#36. Count how many times digit 5 appears in a number

num = int(input("Enter the number: "))

count = 0

while(num > 0):
    digit = num % 10

    if digit == 5:
        count += 1

    num = num // 10

print("Digit 5 appears:", count, "times")


#37. Count the frequency of a given digit.

#while

num = int(input("Enter the number: "))
given = int(input("Enter the digit to find: "))

count = 0

while(num > 0):
    digit = num % 10

    if digit == given:
        count += 1

    num = num // 10

print("Frequency:", count)


#for

num = int(input("Enter the number: "))
given = int(input("Enter the digit to find: "))

count = 0

for digit in str(num):
    if int(digit) == given:
        count += 1

print("Frequency:", count)

#38. Check whether all digits are even.

#for

num = int(input("Enter the number: "))

all_even = True

while(num > 0):
    digit = num % 10

    if digit % 2 != 0:
        all_even = False
        break

    num = num // 10

if all_even:
    print("All digits are even")
else:
    print("Not all digits are even")


#while

num = int(input("Enter the number: "))

all_even = True

for digit in str(num):
    if int(digit) % 2 != 0:
        all_even = False
        break

if all_even:
    print("All digits are even")
else:
    print("Not all digits are even")

#39. Check whether all digits are odd.

#for

num = int(input("Enter the number: "))

all_odd = True

while(num > 0):
    digit = num % 10

    if digit % 2 == 0:
        all_odd = False
        break

    num = num // 10

if all_odd:
    print("All digits are odd")
else:
    print("Not all digits are odd")


#while

num = int(input("Enter the number: "))

all_odd = True

for digit in str(num):
    if int(digit) % 2 == 0:
        all_odd = False
        break

if all_odd:
    print("All digits are odd")
else:
    print("Not all digits are odd")



#Print sunny numbers


#while 


n = int(input("Enter number: "))

num = 1

while(num <= n):

    i = 1

    while(i * i <= num + 1):
        if i * i == num + 1:
            print(num)
            break

        i += 1

    num += 1


#for

n = int(input("Enter number: "))

for num in range(1, n + 1):

    for i in range(1, num + 2):

        if i * i == num + 1:
            print(num)
            break



#5 number from the user check which is greatest from those

greatest = 0

for i in range(5):
    num = int(input("Enter a number: "))

    if num > greatest:
        greatest = num

print("Greatest number:", greatest)


#count and print factors of entering number by the user


n = int(input("Enter a number: "))

count=0

print("Factors are:")

for i in range(1,n+1):
    if n%i==0:
        print(i)
        count+=1

print("Number of Factors:",count)        


#Check Whether the entered number is spy or not


num = int(input("Enter the number: "))

sum = 0
product = 1

while(num > 0):
    digit = num % 10

    sum = sum + digit
    product = product * digit

    num = num // 10

if sum == product:
    print("Spy Number")
else:
    print("Not a Spy Number")

#check whether the number is harshad or not

num = int(input("Enter the number: "))

original = num
sum = 0

while(num > 0):
    digit = num % 10
    sum = sum + digit
    num = num // 10

if original % sum == 0:
    print("Harshad Number")
else:
    print("Not a Harshad Number")