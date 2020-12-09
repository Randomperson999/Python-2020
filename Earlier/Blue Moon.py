#Caleb Keller
#10/5/2020
#Blue Moon Project
print("(This is case sensitive and has to be spelled correctly)\n")
blueMoon = input("Is there a blue moon tonight? (Yes/No)? ")
weekDay = input("What is the day of the week (Monday-Sunday)? ")
dayOfMonth = int(input("What is the day of the month (1-31)? "))
if (blueMoon == "Yes"):
    print("Play song: 'Once in a Blue Moon'")
elif (weekDay == "Monday")and(dayOfMonth ==1):
    print("Play song 'Manic Monday'")
elif (weekDay == "Tuesday")and(dayOfMonth ==2):
    print("Play song 'Tuesday's Gone'")
elif (weekDay == "Wednesday")and(dayOfMonth ==3):
    print("Play song 'Just Wednesday'")
elif (weekDay == "Thursday")and(dayOfMonth ==4):
    print("Play song 'Sweet Thursday'")
elif (weekDay == "Friday")and(dayOfMonth ==5):
    print("Play song 'Friday I'm in Love'")
elif (weekDay == "Saturday")and(dayOfMonth ==6):
    print("Play song 'Saturday in the Park'")
elif (weekDay == "Sunday")and(dayOfMonth ==7):
    print("Play song 'Lazing on a Sunday Afternoon'")
elif (weekDay == "Monday") and (dayOfMonth == 20):
    print("Play song 'Day Dream Believer'")
else:
    print("Play song 'Days of the Week'")

