# Planning your trip
"""
wages
hotel night
plane ride cost
rental car cost
trip cost

"""

def wages(hourly_rate, hours):
    hourly_rate = 8.35
    return hourly_rate * hours




def hotel_cost(night):
    per_night = 140
    return (per_night * night)




def plane_ride_cost(city):
    if city == 'charlotte':
        print("So, You wanna move to charlotte ! Here the cost is :")
        return '$183'
    elif city == 'Tampa':
        print("So, You wanna move to Tampa ! Here the cost is :")
        return '$220'
    elif city == 'Pittsburgh':
        print("So, You wanna move to Pittsburgh ! Here the cost is :")
        return '$340'
    elif city == 'LA':
        print("So, You wanna move to Los Angles ! Here the cost is :")
        return '$500'




# rental car cost with 
def rental_car_cost(days):
    day_rate = 503
    total_cost = day_rate * days

    if days >= 7:
        return total_cost - 50
    elif days >= 3: 
        return total_cost - 25

    return total_cost

        




def trip_cost(days, city, night ):
    return rental_car_cost(days) + plane_ride_cost(city) + hotel_cost(night)

print(hotel_cost(int(input("No. of days for hotel booking  : "))))

print(plane_ride_cost(str(input("which city you are planning to move? we have three option charlotte, Tampa, Pittsburgh, LA . Choose one ! : "))))

print(rental_car_cost(int(input("No. days for renting a car : "))))






















