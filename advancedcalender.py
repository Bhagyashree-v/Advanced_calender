#BHAGYASHREE V
from datetime import date
import calendar
import time
import re
import sys

def display(year, month, date1):
    print("=" * 30)
    cal = calendar.month(year, month)
    rday = ('\\b' + date1 + '\\b').replace('\\b ', '\\s')
    rdayc = "\033[7m" + date1 + "\033[0m"
    print(re.sub(rday, rdayc, cal))


def readvalue():
    try:
        a = int(input("Enter a number between -12 to 12 :"))
        assert (a >= -12) and (a <= 12)
    except ValueError:
        print("Enter integer value only")
        a = int(input("Enter a number between -12 to 12 :"))
    except AssertionError:
        print("Entered value is not in range")
        a = int(input("Enter a number between -12 to 12 :"))

    return a


def date_manipulate(date1, new_month, new_year):
    if (date1 == '31') and (new_month in (4, 6, 9, 11)):
        new_date = '30'
    elif (new_month == 2) and (date1 in ['29', '30', '31']):
        if ((new_year % 400 == 0)) or ((new_year % 4 == 0) and (new_year % 100 != 0)):
            new_date = '29'
        else:
            new_date = '28'
    else:
        new_date = date1
    return str(new_date)

#set firstday of calender to sunday   
calendar.setfirstweekday(calendar.SUNDAY)
if len(sys.argv) > 1:
#  for i in L:
#    if len(i)<=2 and i.isdigit():
#     date1=i
#    elif len(i) == 4 and i.isdigit():
#      year=int(i)
#    elif i.isalpha() or 
#      month=i
  date1 = str(sys.argv[1])
  month = int(sys.argv[2])
  year = int(sys.argv[3])
  print(date1, month, year)
else:
  today = date.today()
  year = today.year
  month = today.month
  date1 = today.day.__str__().rjust(2)
    #print(date,today,year,month)
print(year, month, date1)
print("current calender")
display(year, month, date1)
a = readvalue()

new_month = month + a
new_year = year

if (-12 < new_month) and (new_month <= 0):
    while (new_month <= 0):
        new_month = new_month + 12
        new_year = new_year - 1

elif (0 < new_month) and (new_month <= 12):
    new_month = new_month
    new_year = new_year

elif (new_month > 12) and (new_month <= 24):
    while (new_month > 12):
        new_month = new_month - 12
        new_year = new_year + 1
        #print(new_year,new_month)

new_date = date_manipulate(date1,new_month,new_year)

if a > 0:
    print("\nCalender after", a, "month")
elif a < 0:
    print("\nCalender before ", a, "month")
else:
    print("Calender without change")
    
display(new_year, new_month, new_date)