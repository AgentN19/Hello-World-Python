#Lab 18
#Nabeel Khan
#Nabeel.khan24@myhunter.cuny.edu
#March 4, 2020
#This program takes in the number of cents and outputs the number of coins

cents = int(input('Enter the number of cents'))

quarters = cents / 25
cents = cents % 25

dimes = cents / 10
cents = cents % 10

nickels = cents / 5
cents = cents % 5

print("Quarters: ", quarters)
print("Dimes: ", dimes)
print("Nickels: ", nickels)
print("Cents :", cents)