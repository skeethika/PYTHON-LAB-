#Pass or Fail
'''marks=int(input("enter marks:"))
if marks>=35:
    print("pass")
else:
    print("fail")
#voting eligibility
age=int(input("enter age:"))
if age>=18:
    print("eligible")
else:
    print("not eligible")

#shopping discount
bill=int(input("enter bill:"))
if bill>5000:
    print("discount=10%")
else:
    print("no discount")
bill = float(input("Enter bill amount: "))
if bill > 5000:
    bill = bill - (bill * 10 / 100)
print("Final Amount =", bill)
#password verification
password = "1234"
user = input("Enter password: ")
if user == password:
    print("Access Granted")
else:
    print("Wrong Password")
#Grade System
marks=int(input("enter marks:"))
if marks>=90:
    print("grade A")
elif marks>=75:
    print("grade B")
elif marks>=50:
    print("grade C")
else:
    print("fail")
#Simple Calculator
a=int(input("enter first number:"))
b=int(input("enter second number:"))
choice=input("enter +,-,*,/:")
if choice =="+":
    print(a+b)
elif choice =="-":
    print(a-b)
elif choice =="*":
    print(a*b)
elif choice =="/":
    print(a/b)
else:
    print("invaild choice")
#electricity bill
units=int(input("enter units:"))
if units<=100:
    bill=units*2
elif units <=200:
    bill=units*3
else:
    bill=units*5
print("bill=",bill)
#ticket fare
age=int(input("enter age:"))
if age<=5:
    print("free")
elif age<=12:
    print("fare =50")
else:
    print("fare=100")
#Loan Approval
salary=int(input("enter salary :"))
if salary >=30000:
    score=int(input("enter credit score:"))
    if score>=700:
        print("loan approved")
    else:
        print("loan rejected")
else:
    print("not eligible")
#College Admission
marks = int(input("Enter academic percentage: "))
if marks > 60:
    exam = int(input("Enter entrance score: "))
    if exam > 70:
        print("Admission Granted")
    else:
        print("Admission Rejected")
else:
    print("Not Eligible")
  
#Company Recruitment
degree = int(input("Enter degree percentage: "))
if degree > 65:
    aptitude = int(input("Enter aptitude score: "))
    if aptitude > 75:
        print("Selected")
    else:
        print("Not Selected")
else:
    print("Not Eligible")
#Scholarship
marks=int(input("enter marks percentage:"))
if marks>80:
    attendance=int(input("enter attendance:"))
    if attendance>75:
        print("scholarship awarded")
    else:
        print("attendance low")
else:
    print("not eligible")
#ATM Withdrawal
balance = int(input("Enter account balance: "))
amount = int(input("Enter withdrawal amount: "))
if balance >= amount:
    pin = input("Enter PIN: ")
    if pin == "1234":
        print("Withdrawal Successful")
    else:
        print("Wrong PIN")
else:
    print("Insufficient Balance")
#Secure Login
username = input("Enter username: ")
if username == "admin":
    password = input("Enter password: ")
    if password == "1234":
        otp = input("Enter OTP: ")
        if otp == "1111":
            print("Login Successful")
        else:
            print("Wrong OTP")
    else:
        print("Wrong Password")
else:
    print("Wrong Username")
#Hospital Appointment
doctor = input("Doctor available? (yes/no): ")
if doctor == "yes":
    slot = input("Slot available? (yes/no): ")
    if slot == "yes":
        print("Appointment Confirmed")
    else:
        print("No Slots Available")
else:
    print("Doctor Not Available")
#Cybersecurity Lab Access
registered = input("Registered? (yes/no): ")
if registered == "yes":
    fees = input("Fees Paid? (yes/no): ")
    if fees == "yes":
        print("Access Granted")
    else:
        print("Pay Fees First")
else:
    print("Not Registered")
#Employee Bonus
experience = int(input("Enter experience: "))
if experience >=3:
    rating = int(input("Enter rating: "))
    if rating >= 8:
        print("Bonus Eligible")
    else:
        print("Performance Low")
else:
    print("Not Eligible")
#Online Examination
hall = input("Hall Ticket Available? (yes/no): ")
if hall == "yes":
    fees = input("Fees Cleared? (yes/no): ")
    if fees == "yes":
        print("Exam Access Granted")
    else:
        print("Clear Fees First")
else:
    print("Hall Ticket Not Available")
#Hostel Room Allotment
selected = input("Selected for admission? (yes/no): ")
if selected == "yes":
    room = input("Room Available? (yes/no): ")
    if room == "yes":
        print("Room Allotted")
    else:
        print("No Rooms Available")
else:
    print("Admission Not Confirmed")'''
#Online Shopping Discount
member = input("Premium Member? (yes/no): ")
amount = float(input("Enter purchase amount: "))
if amount > 5000:
    if member == "yes":
        discount = amount * 20 / 100
    else:
        discount = amount * 10 / 100
else:
    discount = 0

print("Discount =", discount)
print("Final Amount =", amount - discount)



