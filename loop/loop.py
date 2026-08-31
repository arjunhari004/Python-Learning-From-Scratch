# i=0
# while(i<=5):
#     i+=1
#     if(i%2!=0):
#         print(i)
    

# #Print number 10-1 where the numbers should be divisible only by 3

# i=10
# while(i>=1):
#     if(i%3==0):
#         print(i)
#     i-=1   

# Print factorial of 10

i = 10
factorial = 1  

while i > 0:
    factorial *= i  
    i -= 1               

print(factorial)


#Sum of n numbers

n = int(input("enter the number: "))
total_sum = 0
i = n

while i >= 1:
    total_sum += i 
    i -= 1          

print(total_sum)
