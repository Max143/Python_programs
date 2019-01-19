# convert all units of time into seconds

days = int(input("days : "))
def days_second():
    return days*3600*24
print(days_second())


hours = int(input("hours : "))
def hours_second():
    return hours * 3600
print(hours_second())




minutes = int(input("minutes : "))
def minutes_second():
    return minutes*60
print(minutes_second())




seconds = int(input("seconds : "))
def seconds_second():
    return seconds
print(seconds_second())

"""
In this way also, we can calculate the same above problem
"""

fuck = int(input("fuck : "))
fuck2 = fuck*1
print(fuck2)

total_seconds = days*3600*24 + hours*3600 + minutes*60 + seconds + fuck2

print("Total seconds of given time is : %d" % (total_seconds))








