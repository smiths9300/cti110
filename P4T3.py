# P4PT3
# While loops
# Name
# 10/25

# Part 1 - repeat until the user says "yes"
answer = "no"
while answer != "yes":
  print ("I like you  do you like me yes or no?")
  answer = input()

# Part 2 - repeat five times
numbers = range (5)
for number in numbers:
  print ("Number:", number)

# Part 3 - adding numbers
numbers =  [2, 3, 4]
total = 0 # have to start the accumulatior at zero
for number in numbers:
  total = total + number 
  print ("Added", number)
print ("Total is:", total)

# Optinal - 99 bottles of beer
bottles = range (99, -1, -1)
for bottle in bottles:
  print (bottle, "bottles of beer ont the wall")
  
