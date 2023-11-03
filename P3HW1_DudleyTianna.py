# I was supposed to put a comment here
# My Last Name


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod1 = input("Enter grade for Module 1: ")
 mod2 = input("Enter grade for Module 2: ")
mod3 = input("Enter grade for Module 3: ")
mod4 = input("Enter grade for Module 1: ")
mod5 = input("Enter grade for Module 5: ")
 mod6 = input("Enter grade for Module 6: ")

# add grades entered to a list

grades = [mod1, mod2, mod3, mod4, mod5, mod6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(Grades)
high = high(grades)
sum = sum(grades)
avg = avg(grades)

# determine letter grade for average
print("------------Results------------")
print("Lowest Grade: ", low)
print("Highest Grade: ", high)
print("Sum of Grade:", sum)
print("Average: ", avg)
print("----------------------------------------")
def grade(average):
if avg>= 90:
print("Your grade is: A")
elif average > 80:
print("Your grade is: B")
elif average > 70:
 print("Your grade is: C")
elif average > 55:
print("Your grade is: D")
elif average > 35:
print("Your grade is: E")
else:
print("Your grade is: F") 
return
grade(avg)
# TO DO: finish this
