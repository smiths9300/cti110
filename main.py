milesPerGallon = 0 # float
costPerGallon = 0 # float in $

# Ask the user for milesPerGallon
milesPerGallon = float(input())
# Ask the user for cost per gallon
costPerGallon = float(input())

# figure out the cost to drive 20 miles
# gallons burned in 20 miles is : 20 miles 7 mpg
gallonsUsedIn20 = 20 / milesPerGallon
costToDrive20 = gallonsUsedIn20 * costPerGallon

# print out the cost
# print(costToDrive20)
# TODO: also do 75 and 200 miles
gallonsUsedin75 = 75 / milesPerGallon
costToDrive75 = gallonsUsedin75 * costPerGallon
# print(costToDrive75)

gallonsUsedin500 = 500 / milesPerGallon
costToDrive500 = gallonsUsedin500 * costPerGallon
# print(costToDrive500)



# use f string to format for the grader
print(f'{costToDrive20:.2f} {costToDrive75:.2f} {costToDrive500:.2f}')