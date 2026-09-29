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


# num = int(input("Enter the number: "))

# rev = 0

# while(num > 0):
#     digit = num % 10
#     rev = rev * 10 + digit
#     num = num // 10

# print(rev)


#Product of a digit 

# num = int(input("Enter the number: "))

# product = 1

# while(num > 0):
#     digit = num % 10
#     product = product * digit
#     num = num // 10

# print(product)



#FUNCTIONS PRACTICE QN



# def student(name):
#     print(name)
# student("Rahul")

#2
# def city(city_name):
#     print(city_name)
# city("Kochi")

#3
# def course(course_name):
#     print(course_name)
# course("Python")

#4
# def greet(name, city):
#     print(name)
#     print(city)
# greet("Tom", "Kochi")

# 5.
# def student(name, course):
#     print(name)
#     print(course)
# student("Rahul", "Python")


# 6.
# def employee(name, department):
#     print(name)
#     print(department)
# employee("Anu", "HR")


# 7.
# def college(name, course, city):
#     print(name)
#     print(course)
#     print(city)
# college("Lmcst College", "B.Tech", "TVM")


# 8.
# def person(name, age, city):
#     print(name)
#     print(age)
#     print(city)
# person("Arun", 22, "Kochi")


# 9.
# def mobile(number):
#     print(number)
# mobile(9876543210)


# 10.
# def company(name, location):
#     print(name)
#     print(location)
# company("Qspider", "Kochi")


# 11.
# def book(title, author):
#     print(title)
#     print(author)
# book("Python Basics", "John")


# 12.
# def teacher(name, subject, city):
#     print(name)
#     print(subject)
#     print(city)
# teacher("Anu", "Maths", "Kochi")


#13.
# def food(name,type):
#     print(name)
#     print(type)
# food("Chicken Biriyani","Non-veg")


# 14.
# def movie(name, language):
#     print(name)
#     print(language)
# movie("ARM", "Malayalam")


# 15.
# def laptop(brand, model):
#     print(brand)
#     print(model)
# laptop("Acer", "Aspire")


# 16.
# def address(house, city, state):
#     print(house)
#     print(city)
#     print(state)
# address("House 07", "Kochi", "Kerala")


# 17.
# def job(role, company, location):
#     print(role)
#     print(company)
#     print(location)
# job("intern", "Qspider", "Kochi")


# 18.
# def college_student(name, course, city, college):
#     print(name)
#     print(course)
#     print(city)
#     print(college)
# college_student("Rahul", "B.Tech", "Tvm", "LMCST College")


# 19.
# def profile(name, city, course, college):
#     print(name)
#     print(city)
#     print(course)
#     print(college)
# profile("John", "TVM", "B.TECH", "LMCST College")


# 20.
# def details(name, age, city, course, college):
#     print(name)
#     print(age)
#     print(city)
#     print(course)
#     print(college)
# details("Arun", 22, "Tvm", "B.Tech", "LMCST College")

# ---default Arguments---

# 21.
# def greet(name="Student"):
#     print(name)
# greet()


# 22.
# def city(city="Kochi"):
#     print(city)
# city()


# 23.
# def course(course="Python"):
#     print(course)
# course()


# 24.
# def student(name="Arun"):
#     print(name)
# student()


# 25.
# def employee(department="CSE"):
#     print(department)
# employee()


# 26.
# def college(city="Kochi"):
#     print(city)
# college()


# 27.
# def teacher(name="Alan", subject="Python"):
#     print(name)
#     print(subject)
# teacher()


# 28.
# def student(name="Ram", course="Data Science"):
#     print(name)
#     print(course)
# student()


# 29.
# def company(location="Kochi"):
#     print(location)
# company()


# 30.
# def book(author="Albert"):
#     print(author)
# book()


# 31.
# def movie(language="English"):
#     print(language)
# movie()


# 32.
# def food(type="Veg"):
#     print(type)
# food()


# 33.
# def laptop(brand="Acer"):
#     print(brand)
# laptop()


# 34.
# def profile(name="Rahul", city="Kochi", course="Python"):
#     print(name)
#     print(city)
#     print(course)
# profile()


# 35.
# def address(state="Kerala"):
#     print(state)
# address()

#36.
# def job(role="Developer"):
#     print(role)
# job()

#37.
# def language(name="Python"):
#     print(name)
# language()

#38.
# def department(name="IT"):
#     print(name)
# department()

# #39.
# def company_details(company="ABC",city="Kochi"):
#     print(company)
#     print(city)
# company_details()

# #40.
# def student_details(name="anu",course="python",city="kochi"):
#     print(name)
#     print(course)
#     print(city)
# student_details()


# #41
# def student(name, city):
#     print(name)
#     print(city)
# student(name="anu",city="kochi")


# #42
# def employee(name, department):
#     print(name)
#     print(department)
# employee(name="Tom",department="IT")


# #43
# def course(name, duration):
#     print(name)
#     print(duration)
# course(name="python",duration="2 months")

# #44
# def person(name, city, age):
#     print(name)
#     print(city)
#     print(age)
# person(name="Alan",city="Kochi",age=22)


# #45
# def college(name, course, city):
#     print(name,course,city)
# college(name="ABC",course="It",city="Kochi")

# #46
# def teacher(name, subject):
#     print(name)
#     print(subject)
# teacher(name="anu",subject="It")

# #47
# def company(name, location):
#     print(name)
#     print(location)
# company(name="TCS",location="Kochi")


# #48
# def book(title, author):
#     print(title)
#     print(author)
# book(title="UNKNOWN",author="Albert")

# #49
# def movie(name, language):
#     print(name)
#     print(language)
# movie(name="RRR",language="Kanada")





# # 26/09/25

# 50. Create a function `laptop(brand, model)` and call it using keyword

# #50.
# def laptop(brand, model):
#     print(brand)
#     print(model)
# laptop(brand="ACER",model="Aspire")

# 51. Create a function `address(city, state)` and call it using keyword


# def address(city, state):
#     print(city)
#     print(state)
# address(city="Kochi",state="Kerala")

# 52. Create a function `job(role, company)` and call it using keyword

# #52
# def job(role, company):
#      print(role)
#      print(company)
# job(role="Developer",company="Tcs")

# 53. Create a function `food(name, type)` and call it using keyword


# #53
# def food(name, type):
#     print(name)
#     print(type)
# food(name="Biriyani",type="veg")


# 54. Create a function `profile(name, city, course)` and call it using


# #54
# def profile(name, city, course):
#     print(name)
#     print(city)
#     print(course)
# profile(name="Alan",city="Kochi",course="It")

# 55. Create a function `student(name, course, city)` and call it using

# keyword arguments in a different order.

# #55
# def student(name, course, city):
#     print(name)
#     print(city)
#     print(course)
# student(name="Alan",course="Python",city="Kochi")

# 56. Create a function `employee(name, department, city)` and call it

# using keyword arguments in a different order.



# #56
# def employee(name, department, city):
#     print(name)
#     print(department)
#     print(city)
# employee(name="tom",department="It",city="Kochi")

# #57
# def teacher(name, subject, city):
#     print(name)
#     print(subject)
#     print(city)
# teacher(name="Anu",subject="Python",city="Kochi")

# # 58.
# def company(name, location, department):
#     print("Name:", name)
#     print("Location:", location)
#     print("Department:", department)
# company(name="Google", location="Bangalore", department="IT")


# # 59.
# def details(name, age, city, course):
#     print("Name:", name)
#     print("Age:", age)
#     print("City:", city)
#     print("Course:", course)
# details(name="Rahul", age=20, city="Kochi", course="Python")


# # 60.
# def student_details(name, course, college, city):
#     print("Name:", name)
#     print("Course:", course)
#     print("College:", college)
#     print("City:", city)
# student_details(city="Kochi", college="ABC College", name="Anu", course="BCA")


# #-----Varabile postional length aruguments-----

# # 61.
# def students(*names):
#     print(names)
# students("Anu", "Rahul", "Arun")


# # 62.
# def cities(*cities):
#     print(cities)
# cities("Kochi", "Tvm", "Idukki")


# # 63.
# def courses(*courses):
#     print(courses)
# courses("Python", "Java", "C++")


# # 64.
# def subjects(*subjects):
#     print(subjects)
# subjects("Maths", "Science", "English")


# # 65.
# def friends(*names):
#     print(names)
# friends("Akhil", "Amal", "Vishnu")


# # 66.
# def colors(*colors):
#     print(colors)
# colors("Red", "Blue", "Green")


# # 67.
# def foods(*foods):
#     print(foods)
# foods("Pizza", "Burger", "Biryani")


# # 68. 
# def languages(*languages):
#     print(languages)
# languages("Python", "Java", "C")


# # 69.
# def companies(*companies):
#     print(companies)
# companies("Google", "Microsoft", "Apple")


# # 69. 
# def companies(*companies):
#     print(companies)
# companies("TCS", "Infosys", "Wipro")

# # 70. 
# def books(*books):
#     print(books)
# books("Python Book", "Java Book", "SQL Book")

# # 71. 
# def movies(*movies):
#     print(movies)
# movies("Drishyam", "Premam", "Lucifer")

# # 72. 
# def teachers(*teachers):
#     print(teachers)
# teachers("Anu", "Rahul", "John")

# # 73. 
# def employees(*employees):
#     print(employees)
# employees("Arun", "Anu", "Rahul")

# # 74. 
# def sports(*sports):
#     print(sports)
# sports("Football", "Cricket", "Tennis")

# # 75. 
# def fruits(*fruits):
#     print(fruits)
# fruits("Apple", "Mango", "Banana")

# # 76. 
# def devices(*devices):
#     print(devices)
# devices("Laptop", "Mobile", "Tablet")

# # 77. 
# def places(*places):
#     print(places)
# places("Kochi", "Delhi", "Mumbai")

# # 78. 
# def animals(*animals):
#     print(animals)
# animals("Dog", "Cat", "Lion")

# # 79. 
# def skills(*skills):
#     print(skills)
# skills("Python", "SQL", "Excel")

# # 80. 
# def details(*details):
#     print(details)
# details("Albert", 21, "Kochi", "Python")

# # 81. 
# def student(**details):
#     print(details)
# student(name="Albert", course="Python", city="Kochi")


# # 82. 
# def employee(**details):
#     print(details)
# employee(name="Albert", department="IT", city="Kochi")

# # 83. 
# def person(**details):
#     print(details)
# person(name="Albert", age=21, city="Kochi")

# # 84. 
# def college(**details):
#     print(details)
# college(name="VJCET", city="Kochi", course="AI")


# # 85. 
# def teacher(**details):
#     print(details)
# teacher(name="Anu", subject="Python", city="Kochi")

# # 86.
# def company(**details):
#     print(details)
# company(name="TCS", location="Kochi", department="IT")

# # 87. 
# def profile(**details):
#     print(details)
# profile(name="Albert", city="Kochi", course="Python")

# # 88. 
# def address(**details):
#     print(details)
# address(house="Rose Villa", city="Kochi", state="Kerala")

# # 89. 
# def course(**details):
#     print(details)
# course(name="Python", duration="3 Months")

# # 90. 
# def book(**details):
#     print(details)
# book(title="Python Programming", author="John")

# # 91.
# def movie(**details):
#     print(details)
# movie(name="Drishyam", language="Malayalam")

# # 92. 
# def laptop(**details):
#     print(details)
# laptop(brand="Dell", model="Inspiron")

# # 93. 
# def job(**details):
#     print(details)
# job(role="Software Engineer", company="TCS", location="Kochi")

# # 94. 
# def food(**details):
#     print(details)
# food(name="Biriyani", type="Veg")

# # 95. 
# def hospital(**details):
#     print(details)
# hospital(name="City Hospital", location="Kochi")

# # 96. 
# def school(**details):
#     print(details)
# school(name="ABC School", city="Kochi")

# # 97. 
# def project(**details):
#     print(details)
# project(name="AI Fitness Trainer", language="Python")

# # 98. 
# def product(**details):
#     print(details)
# product(name="Laptop", brand="Dell", price=50000)

# # 99.
# def customer(**details):
#     print(details)
# customer(name="Albert", city="Kochi", phone="9876543210")

# # 100. 
# def information(**details):
#     print(details)
# information(name="Albert", age=21, course="Python", city="Kochi")

# # 101.
# def a():
#     print("Hello")
# def b():
#     a()
# b()

# # 102.
# def welcome():
#     print("Welcome")
# def start():
#     welcome()
# start()

# # 103.
# def name():
#     print("Arun")
# def student():
#     name()
# student()

# # 104. 
# def city():
#     print("Kochi")
# def place():
#     city()
# place()

# # 105. 
# def course():
#     print("Python")
# def training():
#     course()
# training()

# # 106. 
# def hello():
#     print("Hello Student")
# def message():
#     hello()
# message()

# # 107. 
# def one():
#     print("One")
# def two():
#     one()
# two()

# # 108. 
# def greet():
#     print("Good Morning")
# def start():
#     greet()
# start()

# # 109. 
# def student():
#     print("Student")
# def college():
#     student()
# college()

# # 110. 
# def teacher():
#     print("Teacher")
# def classroom():
#     teacher()
# classroom()

# # 111.
# def python():
#     print("Python")
# def programming():
#     python()
# programming()

# # 112.
# def data():
#     print("Data")
# def analytics():
#     data()
# analytics()

# # 113. 
# def morning():
#     print("Morning")
# def day():
#     morning()
# day()

# # 114. 
# def welcome():
#     print("Welcome")
# def college():
#     welcome()
# college()

# # 115. 
# def hello():
#     print("Hello")
# def greet():
#     hello()
# greet()

# # 116.
# def first():
#     print("First")
# def second():
#     first()
# second()

# # 117.
# def name():
#     print("Meera")
# def student():
#     name()
# student()

# # 118. 
# def city():
#     print("Kochi")
# def address():
#     city()
# address()

# # 119. 
# def course():
#     print("Data Analytics")
# def training():
#     course()
# training()

# # 120.
# def company():
#     print("ABC")
# def employee():
#     company()
# employee()

# # 121. 
# def a():
#     print("A")
# def b():
#     a()
# def c():
#     b()
# c()

# # 122. 
# def one():
#     print("One")
# def two():
#     one()
# def three():
#     two()
# three()

# # 123. 
# def hello():
#     print("Hello")
# def welcome():
#     hello()
# def start():
#     welcome()
# start()

# # 124. 
# def name():
#     print("Arun")
# def student():
#     name()
# def college():
#     student()
# college()

# # 125.
# def python():
#     print("Python")
# def course():
#     python()
# def training():
#     course()
# training()

# # 126. 
# def a():
#     print("A")
# def b():
#     a()
# def c():
#     a()
# b()
# c()

# # 127. 
# def name():
#     print("Anu")
# def city():
#     print("Kochi")
# def details():
#     name()
#     city()
# details()

# # 128. 
# def hello():
#     print("Hello")
# def bye():
#     print("Bye")
# def message():
#     hello()
#     bye()
# message()

# # 129. 
# def one():
#     print("One")
# def two():
#     print("Two")
# def numbers():
#     one()
#     two()
# numbers()

# # 130. 
# def python():
#     print("Python")

# def pandas():
#     print("Pandas")

# def topics():
#     python()
#     pandas()

# topics()


# # 131.
# def student(name, city):
#     print(name)
#     print(city)

# student("Albert", "Kochi")


# # 132.

# def student(name, city):
#     print(name)
#     print(city)

# student(name="Albert", city="Kochi")


# # 133. 

# def employee(name, department):
#     print(name)
#     print(department)

# employee("Albert", "IT")


# # 134.

# def employee(name, department):
#     print(name)
#     print(department)

# employee(name="Albert", department="IT")


# # 135.

# def course(name, duration):
#     print(name)
#     print(duration)

# course("Python", "3 Months")


# # 136.

# def course(name, duration):
#     print(name)
#     print(duration)

# course(name="Python", duration="3 Months")


# # 137.

# def person(name, city, age):
#     print(name)
#     print(city)
#     print(age)

# person("Albert", "Kochi", 21)


# # 138.

# def person(name, city, age):
#     print(name)
#     print(city)
#     print(age)

# person(name="Albert", city="Kochi", age=21)


# # 139. 

# def college(name, course, city):
#     print(name)
#     print(course)
#     print(city)

# college("VJCET", "AI", "Kochi")

# 27/09/26


# 140. Create `college(name, course, city)` and call it using keyword

# arguments.

def college(name, course, city):
    print(name)
    print(course)
    print(city)

college(name="VJCET", course="AI", city="Kochi")


# 141. Create `teacher(name, subject)` and call it using positional

# arguments.

def teacher(name, subject):
    print(name)
    print(subject)

teacher("Anu", "Python")


# 142. Create `teacher(name, subject)` and call it using keyword arguments.


def teacher(name, subject):
    print(name)
    print(subject)

teacher(name="Anu", subject="Python")


# 143. Create `company(name, location)` and call it using positional

# arguments.


def company(name, location):
    print(name)
    print(location)

company("TCS", "Kochi")


# 144. Create `company(name, location)` and call it using keyword arguments.

def company(name, location):
    print(name)
    print(location)

company(name="TCS", location="Kochi")


# 145. Create `book(title, author)` and call it using positional arguments. 

def book(title, author):
    print(title)
    print(author)

book("Python Programming", "John")

# 146. Create `book(title, author)` and call it using keyword arguments.

def book(title, author):
    print(title)
    print(author)

book(title="Python Programming", author="John")


# 147. Create `movie(name, language)` and call it using positional arguments. 

def movie(name, language):
    print(name)
    print(language)

movie("Drishyam", "Malayalam")

 # 148. Create `movie(name, language)` and call it using keyword arguments.

def movie(name, language):
    print(name)
    print(language)

movie(name="Drishyam", language="Malayalam")


# 149. Create `laptop(brand, model)` and call it using positional arguments.

def laptop(brand, model):
    print(brand)
    print(model)

laptop("Dell", "Inspiron")


# 150. Create `laptop(brand, model)` and call it using keyword arguments.

def laptop(brand, model):
    print(brand)
    print(model)
laptop(brand="Dell", model="Inspiron")
