from datetime import date, time

name1 = input()
d1, m1, y1 = input().split("-")
name2 = input()
d2, m2, y2 = input().split("-")

d1, m1, y1, d2, m2, y2 = int(d1), int(m1), int(y1), int(d2), int(m2), int(y2)

def age(bday):
    today = date.today()
    age = today.year - bday.year - ((today.month, today.day) < (bday.month, bday.day))
    return age

age1 = age(date(y1, m1, d1))
age2 = age(date(y2, m2, d2))

if (age1>age2) :
    print(name2)
elif (age1<age2) :
    print(name1)
else:
    print("Both are equal in age")
