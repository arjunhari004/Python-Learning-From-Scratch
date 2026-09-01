# # i=0
# # while(i<=5):
# #     i+=1
# #     if(i%2!=0):
# #         print(i)
    

# # #Print number 10-1 where the numbers should be divisible only by 3

# # i=10
# # while(i>=1):
# #     if(i%3==0):
# #         print(i)
# #     i-=1   

# # Print factorial of 10

# i = 10
# factorial = 1  

# while i > 0:
#     factorial *= i  
#     i -= 1               

# print(factorial)


# #Sum of n numbers

# n = int(input("enter the number: "))
# total_sum = 0
# i = n

# while i >= 1:
#     total_sum += i 
#     i -= 1          

# print(total_sum)


# # check whether the number is prime or not


# inp=int(input("Enter the number:"))
# max=inp//2
# flag=0
# while max>=2:
#     if inp%max==0:
#         flag=1
#         break
#     max-=1
# if flag==1:
#     print("not prime")
# else:
#     print("Prime")        



# #even number from 1 to 51


i=1
c=0
while(i<=51):
    if(i%2==0):
        c=c+1
    i=i+1
print(c)       
