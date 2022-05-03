#Age Generator
#Guesses the age your are based on User Input
#User input Year, Month, Day born
import datetime
#Creating a dictiinary for every month
#Will have a key representing the month in numerical values
#Will have a key representing the month in an abbreviation
#Will have a key representing the full version of the month

Jan = { "value": 1 , "abbr": "Jan", "full":"January"}
Feb = {"value": 2 , "abbr" :"Feb", "full":"February"}
Mar = {"value": 3 , "abbr" : "Mar", "full":"March"}
April = {"value": 4 , "abbr": "Apr", "full": "April"}
May = {"value": 5, "full": "May"}
June = {"value" : 6,"full": "June"}
July = {"value": 7, "full": "July"}
Aug = {"value": 8, "abbr":"Aug", "full":"August"}
Sep = {"value": 9 , "abbr":"Sep", "full":"August"}
Oct = {"value": 10, "abbr":"Oct","full":"October"}
Nov = {"value": 11, "abbr": "Nov", "full":"November"}
Dec = {"value": 12, "abbr" : "Dec", "full":"Decemeber"}
Months = [Jan["full"],Feb["full"], Mar["full"], May["full"], June["full"], July["full"],
Aug["full"], Sep["full"], Oct["full"], Nov["full"], Dec["full"]]
abbr_Months = [Jan["abbr"],Feb["abbr"], Mar["abbr"],
Aug["abbr"], Sep["abbr"], Oct["abbr"], Nov["abbr"], Dec["abbr"]]

#work out current date
#represents the whole shabang (the date now in it's whole entirerity)
x = datetime.datetime.now()
currentYear = x.strftime("%Y")
currentYear = int(currentYear)
currentMonth = x.strftime("%m")
currentMonth = int(currentMonth)
currentDay = x.strftime("%d")
currentDay = int(currentDay)



user_yob = int(input("Enter(year of birth): "))
user_mon = input("Enter(month of birth): ")
user_day = int(input("Enter (day of birth): "))
#Converting User's birthday month to a number
basic_age = currentYear - user_yob
calc_age = 0

user_mon.capitalize()



if user_mon == Jan["full"] or Jan["abbr"]:
  user_mon = int(1)
elif user_mon == Feb["full"] or Feb["abbr"]:
  user_mon =  int(2)
elif user_mon == Mar["full"] or Mar["abbr"]:
  user_mon = int(3)
elif user_mon == April["full"]:
  user_mon = int(4)
elif user_mon == May["full"]:
  user_mon = int(5)
elif user_mon == June["full"]:
  user_mon = int(6)
elif user_mon == July["full"]:
     user_mon = int(7)
elif user_mon == Aug["full"] or Aug["abbr"]:
  user_mon = int(8)
elif user_mon == Sep["full"] or Sep["abbr"]:
  user_mon = int(9)
elif user_mon == Oct["full"] or Oct["abbr"]:
  user_mon = int(10)
elif user_mon == Nov["full"] or Nov["abbr"]:
  user_mon = int(11)
elif user_mon == Dec["full"] or Dec["abbr"]:
  user_mon = int(12)
def  Month():
 global user_mon
 global currentMonth
 global basic_age
 global calc_age
 if currentMonth > user_mon:
  calc_age = basic_age
 elif currentMonth < user_mon:
  calc_age = basic_age - 1

def Day():
 global user_day
 global currentDay
 global basic_age
 global calc_age
 if currentDay < user_day:
  calc_age = basic_age -1
 elif currentDay >= user_day:
  calc_age = basic_age
"""These statements are true
 currentDay< user_day yes basic age = basic_age - 1
 currentDay = user_day yes basic age = basic age
 current Day > user_day basic age = basic age"""

if user_mon == currentMonth:
 Day()
elif user_mon != currentMonth:
 Month()
print(calc_age)
input()


