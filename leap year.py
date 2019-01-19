# Check whether the entered year is leap year

year = int(input("Enter the year to check whether the year is leap or not !"))

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("%d is a leap year" % year)
        else:
            print("%d is not leap year" % year)
    else:
        print("%d is a leap year" % year)
else:
    print("%d is not a leap year" % year)
