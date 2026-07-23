#easy level
#task 1
'''def hello():
    print("hello world")
hello()

#task2
def add(a,b):
    return a+b
print(add(10,50))

#task3
def subtract(a, b):
    return a - b
print(subtract(10, 5))

#task4
def multiply(a,b):
    return a*b
print(multiply(10,10))

#task 5
def divide(a,b):
    return a/b
print(divide(10,5))

#task 6
def square(n):
    return n*n
print(square(4))

#task7
def cube(n):
    return n*n*n
print(cube(3))

#task8
def even_odd(n):
    if n % 2==0:
        print("even")
    else:
        print("odd")
even_odd(7)

#task9
def largest(a,b):
    if a>b:
        print(a)
    else:
        print(b)
largest(10,39)

#task10
def area(length, width):
    return length * width

print(area(5, 4))

#Intermediate Level
#1 factorial
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        return fact
print(factorial(5))

# 2. Prime
def prime(n):
    if n < 2:
        return "Not Prime"
    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"
    return "Prime"
print(prime(7))

# 3. Fibonacci
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
print()
fibonacci(5)

# 4. Reverse String
def reverse(s):
    return s[::-1]
print(reverse("Python"))

# 5. Count Vowels
def vowels(s):
    count = 0
    for i in s.lower():
        if i in "aeiou":
            count += 1
    return count
print(vowels("Python"))

# 6. Palindrome
def palindrome(s):
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")
palindrome("madam")

# 7. Second Largest
def second_largest(lst):
    lst.sort()
    return lst[-2]
print(second_largest([10,20,30,40]))

# 8. Remove Duplicates
def remove_duplicates(lst):
    return list(set(lst))
print(remove_duplicates([1,2,2,3,3,4]))

# 9. Character Frequency
def frequency(s):
    for i in set(s):
        print(i, ":", s.count(i))
frequency("apple")

# 10. Sum of List
def total(lst):
    return sum(lst)
print(total([10,20,30]))


# LAMBDA


print((lambda a,b:a+b)(5,3))
print((lambda x:x*x)(4))
print((lambda x:x*x*x)(3))
print((lambda x:x%2==0)(8))
print((lambda a,b:a if a>b else b)(10,20))

students=[("A",20),("B",18)]
print(sorted(students,key=lambda x:x[1]))

marks=[("Ram",80),("Sam",60)]
print(sorted(marks,key=lambda x:x[1]))

words=["cat","elephant","dog"]
print(max(words,key=lambda x:len(x)))

discount=lambda x:x*0.9
print(discount(1000))

temp=lambda c:(c*9/5)+32
print(temp(30))

# =========================
# MAP()
# =========================

print(list(map(lambda x:x*x,[1,2,3,4])))
print(list(map(str.upper,["ram","sam"])))
print(list(map(lambda x:x+10,[1,2,3])))
print(list(map(lambda x:x*2,[1,2,3])))
print(list(map(lambda x:x**3,[1,2,3])))
print(list(map(lambda c:(c*9/5)+32,[20,30])))
print(list(map(lambda x:x+2000,[20000,30000])))
print(list(map(len,["python","java"])))
print(list(map(str.lower,["PYTHON","JAVA"])))
print(list(map(lambda x:x*1.18,[100,200])))


# FILTER()


print(list(filter(lambda x:x%2==0,[1,2,3,4])))
print(list(filter(lambda x:x%2!=0,[1,2,3,4])))
print(list(filter(lambda x:x>0,[-1,2,-3,4])))
print(list(filter(lambda x:x<0,[-1,2,-3,4])))
print(list(filter(lambda x:x>50,[20,60,80])))

nums=[2,3,4,5,7]
print(list(filter(lambda n: all(n%i!=0 for i in range(2,n)),nums)))
print(list(filter(lambda x:x>75,[60,80,90])))
print(list(filter(lambda x:x.startswith("A"),["Arun","Bala","Anu"])))
print(list(filter(lambda x:x>1000,[500,1200,1500])))
print(list(filter(lambda x:x>30000,[25000,35000,45000])))

# RECURSION


def print_num(n):
    if n>10:
        return
    print(n)
    print_num(n+1)
print_num(1)

def reverse_num(n):
    if n==0:
        return
    print(n)
    reverse_num(n-1)
reverse_num(10)

def sum_n(n):
    if n==1:
        return 1
    return n+sum_n(n-1)
print(sum_n(5))

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(5))

def name(n):
    if n==0:
        return
    print("Sakthipriya")
    name(n-1)
name(3)


# SCENARIO BASED


# Student Result
def result(mark):
    if mark>=75:
        print("Distinction")
    elif mark>=60:
        print("First Class")
    elif mark>=50:
        print("Second Class")
    else:
        print("Fail")
result(82)

# Employee Salary
def salary(s):
    print("Salary:",s+s*0.10)
salary(30000)

# Electricity Bill
def bill(units):
    print("Bill:",units*5)
bill(100)

# Voting
def vote(age):
    if age>=18:
        print("Eligible")
    else:
        print("Not Eligible")
vote(20)

# Shopping Cart
def shopping(amount):
    gst=amount*0.18
    print("Total:",amount+gst)
shopping(1000)

# Bank
balance=1000
def deposit(a):
    global balance
    balance+=a
    print(balance)
def withdraw(a):
    global balance
    balance-=a
    print(balance)
deposit(500)
withdraw(200)
print(balance)

# Attendance
def attendance(attended,total):
    print((attended/total)*100,"%")
attendance(90,100)

# Online Exam
def exam(m1,m2,m3):
    total=m1+m2+m3
    per=total/3
    print("Total:",total)
    print("Percentage:",per)
exam(80,90,70)

# Library Fine
def fine(days):
    print("Fine:",days*5)
fine(4)'''

# Movie Ticket
def ticket(seats):
    print("Total:",seats*150)
ticket(3)
