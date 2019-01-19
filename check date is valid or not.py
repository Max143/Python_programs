'''
Python Program to Check if a Date is Valid and Print the Incremented Date if it is

'''


date = input("Enter the date: ") # Here date is string type

dd, mm, yy = date.split('/')


# Turnin back into integer type 
mm = int(mm)
dd = int(dd)
yy = int(yy)

# Now, setting number of days in month
# Month which have 31 days
if (mm  == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12):
   days = 31
# Month which have 30 days
elif ( mm == 4 or mm == 6 or mm == 9 or mm == 11):
   days = 30
# Days of month of Feb depends on leap year
# So, checking the year for leap 
elif (yy%4==0 and yy%100!=0 or yy%400==0):
   days = 29
else:
   days = 28

# Assigning validation of date using if-else statement
if (mm < 1 or mm > 12):
   print("Date is invalid.")
elif (dd < 1 or dd > days):
   print("Date is invalid")
# while incrementing, when month is 12 then insted of incrementing to 13, we will assign month 1
# while incrementing, when days 31 or 30 or 28/29 then instead of incrementing t0 32 or 31 or 29/30 respectively. we will assign days 1
elif (dd == days and mm != 12):
   dd = 1
   mm += 1  # or write as mm = mm + 1
   print("The incremented date is {0}{1}{2}".format(dd,mm,yy))
elif (dd == 31  and mm == 12):
   dd = 1
   mm = 1
   yy += 1  # or write as yy = yy + 1
   print("The incremented date is {0}{1}{2}".format(dd,mm,yy))
else:
   dd += 1 # or write as dd = dd + 1
   print("The incremented date is {0}/{1}/{2}".format(dd,mm,yy))

   

   
   
   



















   
   
