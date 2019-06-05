cars = 100	#specify number of cars
space_in_a_car = 4.0	#specify average space in a car in floating no. style
drivers = 30	#specify number of drivers
passengers = 90		#specify number of passengers
cars_not_driven = cars - drivers	# calculates number of cars no driven
cars_driven = drivers	#cars that are driven
carpool_capacity = cars_driven * space_in_a_car		#specify carpool capacity in floating style
average_passengers_per_car = passengers / cars_driven 	#estimates average passenger per car


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,"in each car.")

# Study Drill

# car_pool_capacity is not initialised and while running code program
# doesn't know the value of the above variable and hence
# NameError is thrown

# 1

space_in_a_car = 4	#if it is 4 instead of 4.0
carpool_capacity = cars_driven * space_in_a_car
# carpool_capacity will be 120 instead of 120.0, hence it will be in int