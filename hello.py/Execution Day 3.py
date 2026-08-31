#Check whether 36 is divisible by 6.
if (36%6==0):
        print('36 is divisible by 6')
#Check whether 37 is not divisible by 5.
if(37%5!=0):
        print("37 is not divisible by 5")
#Check whether 48 is a multiple of 8.
if(48%8==0):
        print('48 is multiple of 8')
#Check whether 50 is not a multiple of 7.
if (50%7!=0):
        print("50 is not a multiple of 7")
#Check whether 25 is between 10 and 40.
if((25>10) & (25<40)):
        print ("25 is between 10 and 40")
# Check whether 55 is outside the range 20 to 45.
a=55
b=20
c=45
if((a>b)&(a>c)):
        print("55 is outside the range of 20 to 45" )
else:
        print("55 is inside the range of 20 to 45")
 #Check whether 80 is greater than both 35 and 60.
a=80
b=35
c=60
if((a>b) & (a>c)):
        print("a is greater than b and c")  
 #Check whether 12 is smaller than both 20 and 30.
a=12
b=20
c=30
if((a<b)&(a<c)):
        print('a is smaller than both b and c')  
# Check whether 15 is equal to either 15 or 25.
a=15
b=15
c=25
if((a==b)|(a==c)):
        print('15 is eqaul to either 15 or 25')
#Check whether 20 is different from both 10 and 30.
a=20
b=10
c=30
if((a!=b)&(a!=c)):
        print('20 is different from both 10 and 30')
#Check whether the sum of 8 and 14 is positive.
a=8
b=14
c=a+b
if(c>0):
        print('8 and 14 is positive')
#Check whether the sum of 11 and 13 is even.
a=11
b=13
c=a+b
if(c%2==0):
        print('sum of 11 and 13 is even')  
#Check whether the sum of 42 and 7 is divisible by 7.
a=42
b=7
c=a+b
if(c%7==0):
        print("a and b is divisible by c")  
#Check whether the difference between 25 and 10 is positive.
a=25
b=10
c=a-b
if(c>0):
        print('Difference between a and b is positive')
# Check whether the difference between 18 and 6 is even.
a=18
b=6
c=a-b
if(c%2==0):
        print('Difference between a and b is even') 
#Check whether the product of 7 and 9 is positive.
a=7
b=9
c=7*9
if(c>0):
        print("Product of 7 and 9 is positive")
#Check whether the product of 12 and -5 is negative.
a=12
b=-5
c=a*b
if(c<0):
        print("Product of 12 and -5 is negative")
#Check whether the product of 36 and 6 is divisible by 6.
a=36
b=6
c=a*b
if(c%6==0):
        print("Product of 36 and 6 is divisible by 6")
#Check whether 45 is a two-digit number.
a=45
if(a>9):
        print('45 is a 2 digit number')
#Check whether 125 is a three-digit number.
a=125
if(a>99):
        print('125 is a 3 digit number') 
#Check whether 150 is greater than 100.
a=150
b=100
if(a>b):
        print('150 is greater than 100') 
#Check whether 75 is smaller than 100.
a=75
b=100
if(a<100):
        print('75 is smaller than 100') 
#Check whether 600 is greater than 500.
a=600
b=500
if(a>b):
        print('600 is greater than 500 ') 
# Check whether 250 is smaller than 500.
a=250
b=500
if(a<500):
        print('250 is less than 500')
#Check whether 72 is divisible by both 8 and 9.
a=72
b=8
c=9
if(a%b==0)&(a%c==0):
        print('72 is divisible by bothe 8 and 9')
#Check whether 35 is divisible by either 6 or 7. 
a=35
b=6
c=7
if((a%b==0)|(a%c==0)):
        print("35 is divisible by either 6 or 7")
else:
        print('35 is not divisible by 6 or 7')                              
#Check whether 25 is greater than 10 but smaller than 40.
a=25
b=10
c=40
if((a>b)&(a<c)):
        print('25 is greater than 10 but smaller than 40')

#Check whether 15 is smaller than 30 but greater than 5.
a=15
b=30
c=5
if((a<b)&(a>c)):
        print('15 is smaller than 30 but greater than 5')


#Check whether 12 and 18 have the same parity.
a=12
b=18
if((a%2==0)&(b%2==0)):
        print('12 and 18 have the same parity')


#Check whether 21 and 9 have different parity.
a=21
b=9
if((a%2!=b%2)):
        print('21 and 9 have different parity')


#Check whether 18 is exactly twice 9.
a=18
b=9
if(a==2*b):
        print('18 is exactly twice 9')


#Check whether 24 is exactly three times 8.
a=24
b=8
if(a==3*b):
        print('24 is exactly three times 8')


#Check whether 8 is half of 16.
a=8
b=16
if(a==b/2):
        print('8 is half of 16')


#Check whether 49 is the square of 7.
a=49
b=7
if(a==b**2):
        print('49 is the square of 7')


#Check whether 60 is greater than the sum of 20 and 30.
a=60
b=20
c=30
if(a>(b+c)):
        print('60 is greater than the sum of 20 and 30')


#Check whether 10 is smaller than the sum of 20 and 5.
a=10
b=20
c=5
if(a<(b+c)):
        print('10 is smaller than the sum of 20 and 5')


#Check whether 100 is equal to the difference of 120 and 20.
a=100
b=120
c=20
if(a==b-c):
        print('100 is equal to the difference of 120 and 20')


#Check whether 72 is greater than the product of 8 and 8.
a=72
b=8
c=8
if(a>(b*c)):
        print('72 is greater than the product of 8 and 8')


#Check whether 72 is smaller than the product of 10 and 8.
a=72
b=10
c=8
if(a<(b*c)):
        print('72 is smaller than the product of 10 and 8')


#Check whether 72 is divisible by the sum of 8 and 4.
a=72
b=8
c=4
if(a%(b+c)==0):
        print('72 is divisible by the sum of 8 and 4')

#51. For 7, print 1 if it is positive, otherwise print 2 if it is negative, otherwise print 3.
a=7
if(a>0):
        print(1)
elif(a<0):
        print(2)
else:
        print(3)


#52. For 18, print 1 if it is even, otherwise print 2 if it is odd.
a=18
if(a%2==0):
        print(1)
else:
        print(2)


#53. For 65, print 1 if it is greater than 50, otherwise print 2 if it is equal to 50, otherwise print 3.
a=65
if(a>50):
        print(1)
elif(a==50):
        print(2)
else:
        print(3)


#54. For 25, print 1 if it is divisible by 3, otherwise print 2 if it is divisible by 5, otherwise print 3.
a=25
if(a%3==0):
        print(1)
elif(a%5==0):
        print(2)
else:
        print(3)


#55. For 14, print 1 if it is below 10, otherwise print 2 if it is between 10 and 20, otherwise print 3.
a=14
if(a<10):
        print(1)
elif((a>=10)&(a<=20)):
        print(2)
else:
        print(3)


#56. For 0, print 1 if it is zero, otherwise print 2 if it is positive, otherwise print 3.
a=0
if(a==0):
        print(1)
elif(a>0):
        print(2)
else:
        print(3)


#57. For 37, print 1 if it is less than 25, otherwise print 2 if it is less than 50, otherwise print 3.
a=37
if(a<25):
        print(1)
elif(a<50):
        print(2)
else:
        print(3)


#58. For 21, print 1 if it is divisible by 2, otherwise print 2 if it is divisible by 3, otherwise print 3.
a=21
if(a%2==0):
        print(1)
elif(a%3==0):
        print(2)
else:
        print(3)


#59. For 75, print 1 if it is greater than 100, otherwise print 2 if it is between 50 and 100, otherwise print 3.
a=75
if(a>100):
        print(1)
elif((a>=50)&(a<=100)):
        print(2)
else:
        print(3)


#60. For 105, print 1 if it is a one-digit number, otherwise print 2 if it is a two-digit number, otherwise print 3.
a=105
if(a>=0 and a<=9):
        print(1)
elif(a>=10 and a<=99):
        print(2)
else:
        print(3)


#61. For 18, print 1 if it is divisible by 4, otherwise print 2 if it is divisible by 6, otherwise print 3.
a=18
if(a%4==0):
        print(1)
elif(a%6==0):
        print(2)
else:
        print(3)


#62. For -4, print 1 if it is below 0, otherwise print 2 if it is below 100, otherwise print 3.
a=-4
if(a<0):
        print(1)
elif(a<100):
        print(2)
else:
        print(3)


#63. For 27, print 1 if it is odd, otherwise print 2 if it is divisible by 4, otherwise print 3.
a=27
if(a%2!=0):
        print(1)
elif(a%4==0):
        print(2)
else:
        print(3)


#64. For 150, print 1 if it is greater than 200, otherwise print 2 if it is greater than 100, otherwise print 3.
a=150
if(a>200):
        print(1)
elif(a>100):
        print(2)
else:
        print(3)


#65. For 63, print 1 if it is divisible by 7, otherwise print 2 if it is divisible by 9, otherwise print 3.
a=63
if(a%7==0):
        print(1)
elif(a%9==0):
        print(2)
else:
        print(3)


#66. For -9, print 1 if it is less than 0, otherwise print 2 if it is equal to 0, otherwise print 3.
a=-9
if(a<0):
        print(1)
elif(a==0):
        print(2)
else:
        print(3)


#67. For 15, print 1 if it is between 1 and 10, otherwise print 2 if it is between 11 and 20, otherwise print 3.
a=15
if((a>=1)&(a<=10)):
        print(1)
elif((a>=11)&(a<=20)):
        print(2)
else:
        print(3)


#68. For 40, print 1 if it is a multiple of 10, otherwise print 2 if it is a multiple of 5, otherwise print 3.
a=40
if(a%10==0):
        print(1)
elif(a%5==0):
        print(2)
else:
        print(3)


#69. For 350, print 1 if it is greater than 500, otherwise print 2 if it is greater than 250, otherwise print 3.
a=350
if(a>500):
        print(1)
elif(a>250):
        print(2)
else:
        print(3)


#70. For 24, print 1 if it is divisible by 8, otherwise print 2 if it is divisible by 4, otherwise print 3.
a=24
if(a%8==0):
        print(1)
elif(a%4==0):
        print(2)
else:
        print(3)


#71. For 32, print 1 if it is smaller than 20, otherwise print 2 if it is smaller than 40, otherwise print 3.
a=32
if(a<20):
        print(1)
elif(a<40):
        print(2)
else:
        print(3)


#72. For 42, print 1 if it is positive and even, otherwise print 2 if it is positive and odd, otherwise print 3.
a=42
if((a>0)&(a%2==0)):
        print(1)
elif((a>0)&(a%2!=0)):
        print(2)
else:
        print(3)


#73. For -15, print 1 if it is negative and even, otherwise print 2 if it is negative and odd, otherwise print 3.
a=-15
if((a<0)&(a%2==0)):
        print(1)
elif((a<0)&(a%2!=0)):
        print(2)
else:
        print(3)


#74. For 17, print 1 if it is divisible by 2, otherwise print 2 if it is divisible by 5, otherwise print 3.
a=17
if(a%2==0):
        print(1)
elif(a%5==0):
        print(2)
else:
        print(3)


#75. For 80, print 1 if it is greater than 75, otherwise print 2 if it is between 25 and 75, otherwise print 3.
a=80
if(a>75):
        print(1)
elif((a>=25)&(a<=75)):
        print(2)
else:
        print(3)


#76. For 35, print 1 if it is less than 10, otherwise print 2 if it is between 10 and 50, otherwise print 3.
a=35
if(a<10):
        print(1)
elif((a>=10)&(a<=50)):
        print(2)
else:
        print(3)


#77. For 30, print 1 if it is divisible by 10, otherwise print 2 if it is divisible by 2, otherwise print 3.
a=30
if(a%10==0):
        print(1)
elif(a%2==0):
        print(2)
else:
        print(3)


#78. For 750, print 1 if it is greater than 1000, otherwise print 2 if it is greater than 500, otherwise print 3.
a=750
if(a>1000):
        print(1)
elif(a>500):
        print(2)
else:
        print(3)


#79. For 27, print 1 if it is a multiple of 3, otherwise print 2 if it is a multiple of 2, otherwise print 3.
a=27
if(a%3==0):
        print(1)
elif(a%2==0):
        print(2)
else:
        print(3)


#80. For 150, print 1 if it is smaller than 100, otherwise print 2 if it is smaller than 200, otherwise print 3.
a=150
if(a<100):
        print(1)
elif(a<200):
        print(2)
else:
        print(3)


#81. For 45, print 1 if it is between 20 and 30, otherwise print 2 if it is between 40 and 50, otherwise print 3.
a=45
if((a>=20)&(a<=30)):
        print(1)
elif((a>=40)&(a<=50)):
        print(2)
else:
        print(3)


#82. For 55, print 1 if it is divisible by 11, otherwise print 2 if it is divisible by 5, otherwise print 3.
a=55
if(a%11==0):
        print(1)
elif(a%5==0):
        print(2)
else:
        print(3)


#83. For 46, print 1 if it is even and greater than 20, otherwise print 2 if it is odd and greater than 20, otherwise print 3.
a=46
if((a%2==0)&(a>20)):
        print(1)
elif((a%2!=0)&(a>20)):
        print(2)
else:
        print(3)


#84. For 13, print 1 if it is even and below 20, otherwise print 2 if it is odd and below 20, otherwise print 3.
a=13
if((a%2==0)&(a<20)):
        print(1)
elif((a%2!=0)&(a<20)):
        print(2)
else:
        print(3)


#85. For 72, print 1 if it is positive and below 50, otherwise print 2 if it is positive and 50 or above, otherwise print 3.
a=72
if((a>0)&(a<50)):
        print(1)
elif((a>0)&(a>=50)):
        print(2)
else:
        print(3)


#86. For -80, print 1 if it is negative and below -50, otherwise print 2 if it is negative and -50 or above, otherwise print 3.
a=-80
if((a<0)&(a<-50)):
        print(1)
elif((a<0)&(a>=-50)):
        print(2)
else:
        print(3)


#87. For 36, print 1 if it is divisible by 12, otherwise print 2 if it is divisible by 6, otherwise print 3.
a=36
if(a%12==0):
        print(1)
elif(a%6==0):
        print(2)
else:
        print(3)


#88. For 45, print 1 if it is divisible by 15, otherwise print 2 if it is divisible by 5, otherwise print 3.
a=45
if(a%15==0):
        print(1)
elif(a%5==0):
        print(2)
else:
        print(3)


#89. For 250, print 1 if it is greater than 300, otherwise print 2 if it is between 100 and 300, otherwise print 3.
a=250
if(a>300):
        print(1)
elif((a>=100)&(a<=300)):
        print(2)
else:
        print(3)


#90. For 450, print 1 if it is smaller than 300, otherwise print 2 if it is between 300 and 600, otherwise print 3.
a=450
if(a<300):
        print(1)
elif((a>=300)&(a<=600)):
        print(2)
else:
        print(3)


#91. For 91, print 1 if it is divisible by 13, otherwise print 2 if it is divisible by 7, otherwise print 3.
a=91
if(a%13==0):
        print(1)
elif(a%7==0):
        print(2)
else:
        print(3)


#92. For 16, print 1 if it is a multiple of 4, otherwise print 2 if it is a multiple of 8, otherwise print 3.
a=16
if(a%4==0):
        print(1)
elif(a%8==0):
        print(2)
else:
        print(3)


#93. For 25, print 1 if it is greater than 25, otherwise print 2 if it is equal to 25, otherwise print 3.
a=25
if(a>25):
        print(1)
elif(a==25):
        print(2)
else:
        print(3)


#94. For 75, print 1 if it is less than 75, otherwise print 2 if it is equal to 75, otherwise print 3.
a=75
if(a<75):
        print(1)
elif(a==75):
        print(2)
else:
        print(3)


#95. For 27, print 1 if it is divisible by 9, otherwise print 2 if it is divisible by 3, otherwise print 3.
a=27
if(a%9==0):
        print(1)
elif(a%3==0):
        print(2)
else:
        print(3)


#96. For 150, print 1 if it is between 100 and 200, otherwise print 2 if it is above 200, otherwise print 3.
a=150
if((a>=100)&(a<=200)):
        print(1)
elif(a>200):
        print(2)
else:
        print(3)


#97. For 40, print 1 if it is between 0 and 50, otherwise print 2 if it is above 50, otherwise print 3.
a=40
if((a>=0)&(a<=50)):
        print(1)
elif(a>50):
        print(2)
else:
        print(3)


#98. For -3, print 1 if it is negative, otherwise print 2 if it is zero, otherwise print 3.
a=-3
if(a<0):
        print(1)
elif(a==0):
        print(2)
else:
        print(3)


#99. For 18, print 1 if it is even, otherwise print 2 if it is a multiple of 3, otherwise print 3.
a=18
if(a%2==0):
        print(1)
elif(a%3==0):
        print(2)
else:
        print(3)        