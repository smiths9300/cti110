# CTI 110
# P4HW1 - Grade list
# smiths
# 11/1/11

# Ask the user for 6 grades for the 6 modules.
# Add them to a list.

grades = []


for grade in range(6):
    grade = int(input("Enter grade: "))
    grades.append(grade)

print("The grades are: ", grades)
# max(grades) and min (grades)
# to show lowest and highest in the list
print("Highest grade: ", max(grades))
print("Lowest grade: ", min(grades))

#now the average - divide the sum by the lenght (count)
total = sum(grades)
count = len(grades)
average = total / count
print("Total is: ", total)
print("Average is: ", average)
