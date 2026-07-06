#break
#Task1
'''for i in range(1,101):
    if i ==51:
        break
    print(i)
#Task2
while True:
    password=input("enter password:")
    if password=="admin123":
        print("correct password")
        break
    else:
        print("wrong password")
#Task3
names=['keerthi','sakthi','harini']
search=input("enter name:")
for name in names:
    if name in name==search:
        print("name found")
        break

#continue
#Task4
for i in range (1,51):
    if i %3==0:
        continue
    print(i)
#Task5
for i in range(1,51):
    if i %2==0:
        continue
    print(i)
    
#Task6
text=input("enter a word:")
for ch in text:
    if ch in "aeiouAEIOU":
        continue
    print(ch)
#pass
#task7
def display():
    pass
#task8
class student:
    pass
#task9
for i in range(1,6):
    if i ==3:
        pass
    print(i)

i=1
while i <=100:
    if i ==51:
        break
    print(i)
    i+=1
while True:
    pwd = input("Enter Password: ")
    if pwd == "1234":
        print("Correct Password")
        break
names = ["jothi", "harini", "sakthi", "Keerthika"]
search = input("Enter Name: ")
i = 0
while i < len(names):
    if names[i] == search:
        print("Name Found")
        break
    i += 1
i = 1
while i <= 20:
    if i % 3 == 0:
        i += 1
        continue
    print(i)
    i += 1
i=1
while i <=50:
    if i %2==0:
        i+=1
        continue
    print(i)
    i+=1
word = input("Enter Word: ")
i = 0
while i < len(word):
    if word[i] in "aeiouAEIOU":
        i += 1
        continue
    print(word[i])
    i += 1
i=1
while i<=5:
    if i ==3:
        pass
    print(i)
    i+=1

'''
#while loop
#1 print numbers from 1-10
'''
i=1
while i<=10:
    print(i)
    i+=1
#2 print numbers from 10-1
i=10
while i >=1:
    print(i)
    i-=1
#3print even numbe1111rs from 1-20
i=2
while i<=20:
    print(i)
    i+=2
#4print odd num 1-20
i=1
while i<=20:
    print(i)
    i+=2
#5sum num 1-50
i=1
s=0
while i <=50:
    s+=i
    i+=1
print(s)
#6 multiplication table
n=int(input())
i=1
while i<=10:
    print(n*i)
    i+=1
#7 count digits
n=int(input())
count=0
while n>0:
    count+=1
    n//=10
print(count)
#8 reverse num
a=int(input("enter a n:"))
rev=0
t=a
while t>0:
    d=t%10
    rev=(rev*10)+d
    t=t//10
print(rev)
if rev==a:
    print("rev")
#9palindrome
a=int(input("enter a n:"))
b=0
t=a
while t>0:
    d=t%10
    b=(b*10)+d
    t=t//10
print(b)
if b==a:
    print("palindrome")
else:
    print(" not a palindrome")
#10 spy num
a=int(input("enter n:"))
b=0
c=1
t=a
while t>0:
    d=t%10
    b+=d
    c*=d
    t=t//10
print(b)
print(c)
if b==c:
    print("spy num")
else:
    Print("not spy num")
#11 sum of digits
num=1234
sum=0
while num>0:
    d=num%10
    sum=sum+d
    num=num//10
print("sum:",sum)
#12 Product of digits
n = int(input())
p = 1
while n > 0:
    p *= n % 10
    n //= 10
#13 Armstrong Number
n = int(input())
temp = n
s = 0
while n > 0:
    d = n % 10
    s += d ** 3
    n //= 10
if temp == s:
    print("Armstrong")
else:
    print("Not Armstrong")
#14 Largest digit
n = int(input())
large = 0
while n > 0:
    d = n % 10
    if d > large:
        large = d
    n //= 10
print(large)
#15Smallest digit
n = int(input())
small = 9
while n > 0:
    d = n % 10
    if d < small:
        small = d
    n //= 10
print(small)
#16fibonacci series
n=6
a=0
b=1
for i in range (n):
    print(a,end="")
    c=a+b
    a=b
    b=c'''
# 17. Factorial
n = int(input())
fact = 1
while n > 0:
    fact *= n
    n -= 1
print(fact)
