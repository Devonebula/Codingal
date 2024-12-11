def plane_ride_cost(city):
    if city== "Saudi Arabia":
        return 700
    elif city== "Dubai":
        return 500
    elif city== "London":
        return 1000
def hotel_cost(days):
    cost=days*100
    if days>=7:
        cost=cost-cost*0.1
    elif days>=3:
        cost=cost-cost*0.05
    return cost
def car_cost(days):
    cost=days*20
    if days>=7:
        cost=cost-cost*0.1
    elif days>=3:
        cost=cost-cost*0.05
    return cost
def trip_cost(city, stays, days):
    print("The Plane cost is", plane_ride_cost(city))
    print("The Hotel cost is", hotel_cost(stays))
    print("The Car cost is", car_cost(days))
    print("The total cost is", plane_ride_cost(city)+hotel_cost(stays)+car_cost(days))
trip_cost("Saudi Arabia", 3, 7)