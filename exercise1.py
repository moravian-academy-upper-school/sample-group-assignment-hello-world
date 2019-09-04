import datetime
print(datetime.datetime.now())
print('When is your birthday? ')
year= int(input('Year :'))
month= int(input('Month (put it in numerical form): '))
day= int(input('Day: '))

if month <= 9:
    startgrade= 5 + year
else:
    startgrade= 6 + year

currentYear = int(str(datetime.datetime.now())[:4])

if currentYear-startgrade > 12:
    print("You've graduated! yaaaaaaaaaaaaaaaay")
elif currentYear >= startgrade:
    print("Grade", currentYear-startgrade)
else:
    print("Has not started school")
