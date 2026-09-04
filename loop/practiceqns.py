# #print numbers from 1 to n

# num1=eval(input("Enter the Number:"))
# i=1
# while(i<=num1):
#     print(i)
#     i=i+1

# #Find the sum of even Numbers from 1 to n

# n = int(input("Enter n: "))

# i = 1
# sum = 0

# while(i <= n):
#     if(i % 2 == 0):
#         sum = sum + i
#     i = i + 1

# print(sum)


# #find the sum of odd numbers from 1 to n


# n = int(input("Enter n: "))

# i = 1
# sum = 0

# while(i <= n):
#     if(i % 2 != 0):
#         sum = sum + i
#     i = i + 1

# print(sum)


#Count how many numbers are present between 1 to n

# num1=int(input("Enter the number:"))
# i=1
# count=0
# while(i<=num1):
#     count+=1
#     i+=1
# print(count)


#Print the multiplication table of a given number

# num = int(input("Enter the number: "))

# i = 1

# while(i <= 10):
#     print(num, "x", i, "=", num * i)
#     i += 1

#Print square of numbers from 1 to n


# n = int(input("Enter the number: "))

# i = 1

# while(i <= n):
#     print(i, "=", i * i)
#     i += 1

#Find sum of digits of a number

# num = int(input("Enter the number: "))

# sum = 0

# while(num > 0):
#     digit = num % 10
#     sum = sum + digit
#     num = num // 10

# print(sum)


#Reverse of a digit


num = int(input("Enter the number: "))

rev = 0

while(num > 0):
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print(rev)


#Product of a digit 

# num = int(input("Enter the number: "))

# product = 1

# while(num > 0):
#     digit = num % 10
#     product = product * digit
#     num = num // 10

# print(product)