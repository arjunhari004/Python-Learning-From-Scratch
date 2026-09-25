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

#39.
def company_details(company="ABC",city="Kochi"):
    print(company)
    print(city)
company_details()

#40.
def student_details(name="anu",course="python",city="kochi"):
    print(name)
    print(course)
    print(city)
student_details()


#41
def student(name, city):
    print(name)
    print(city)
student(name="anu",city="kochi")


#42
def employee(name, department):
    print(name)
    print(department)
employee(name="Tom",department="IT")


#43
def course(name, duration):
    print(name)
    print(duration)
course(name="python",duration="2 months")

#44
def person(name, city, age):
    print(name)
    print(city)
    print(age)
person(name="Alan",city="Kochi",age=22)


#45
def college(name, course, city):
    print(name,course,city)
college(name="ABC",course="It",city="Kochi")

#46
def teacher(name, subject):
    print(name)
    print(subject)
teacher(name="anu",subject="It")

#47
def company(name, location):
    print(name)
    print(location)
company(name="TCS",location="Kochi")


#48
def book(title, author):
    print(title)
    print(author)
book(title="UNKNOWN",author="Albert")

#49
def movie(name, language):
    print(name)
    print(language)
movie(name="RRR",language="Kanada")

#50.
def laptop(brand, model):
    print(brand)
    print(model)
laptop(brand="ACER",model="Aspire")

#51
def address(city, state):
    print(city)
    print(state)
address(city="Kochi",state="Kerala")

#52
def job(role, company):
     print(role)
     print(company)
job(role="Developer",company="Tcs")

#53
def food(name, type):
    print(name)
    print(type)
food(name="Biriyani",type="veg")

#54
def profile(name, city, course):
    print(name)
    print(city)
    print(course)
profile(name="Alan",city="Kochi",course="It")

#55
def student(name, course, city):
    print(name)
    print(city)
    print(course)
student(name="Alan",course="Python",city="Kochi")

#56
def employee(name, department, city):
    print(name)
    print(department)
    print(city)
employee(name="tom",department="It",city="Kochi")

#57
def teacher(name, subject, city):
    print(name)
    print(subject)
    print(city)
teacher(name="Anu",subject="Python",city="Kochi")

# 58.
def company(name, location, department):
    print("Name:", name)
    print("Location:", location)
    print("Department:", department)
company(name="Google", location="Bangalore", department="IT")


# 59.
def details(name, age, city, course):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)
    print("Course:", course)
details(name="Rahul", age=20, city="Kochi", course="Python")


# 60.
def student_details(name, course, college, city):
    print("Name:", name)
    print("Course:", course)
    print("College:", college)
    print("City:", city)
student_details(city="Kochi", college="ABC College", name="Anu", course="BCA")


#-----Varabile postional length aruguments-----

# 61.
def students(*names):
    print(names)
students("Anu", "Rahul", "Arun")


# 62.
def cities(*cities):
    print(cities)
cities("Kochi", "Tvm", "Idukki")


# 63.
def courses(*courses):
    print(courses)
courses("Python", "Java", "C++")


# 64.
def subjects(*subjects):
    print(subjects)
subjects("Maths", "Science", "English")


# 65.
def friends(*names):
    print(names)
friends("Akhil", "Amal", "Vishnu")


# 66.
def colors(*colors):
    print(colors)
colors("Red", "Blue", "Green")


# 67.
def foods(*foods):
    print(foods)
foods("Pizza", "Burger", "Biryani")


# 68. 
def languages(*languages):
    print(languages)
languages("Python", "Java", "C")


# 69.
def companies(*companies):
    print(companies)
companies("Google", "Microsoft", "Apple")
