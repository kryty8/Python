# Day counter program - to calculate how many input days will be in input month in input year

import calendar

#function for inputs

def countdays(theyear, themonth, whichday):
    daycount = 0
    # from calendar, get information about days in month
    # days count form 0 to 6 because of list
    weeklist = calendar.monthcalendar(theyear, themonth)
    # make a loop to count how many times, chosen day was repeat
    for week in weeklist:
        if week[whichday] != 0:
            daycount += 1
    return daycount

print("--Day counter program--\n")

run = True
while(run):
    try:
        print("Which day You want to count? Select number: ")
        print("0: Mondays?")
        print("1: Tuesdays?")
        print("2: Wednesdays?")
        print("3: Thursdays?")
        print("4: Fridays?")
        print("5: Saturdays?")
        print("6: Sundays?")
        print("Or type 'exit' to quit")

        theday = input("? ")
        if theday == "exit":
            run = False
            break
        day = int(theday)

        yearstr = input("Enter year: ")
        year = int(yearstr)

        monthstr = input("Enter month: ")
        month = int(monthstr)

        result = countdays(year, month, day)
        print("there are: " + str(result) + " of those days in the month and year specified")
        print("--------\n")

    except Exception as e:
        print(e)
        print("Bad imput")
