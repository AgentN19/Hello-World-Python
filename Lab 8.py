#Lab 8
#Nabeel Khan
#Nabeel.khan24@myhunter.cuny.edu
#February 19, 2020
#This program takes in a string and prints it backwards

meep = input('Enter a message: ')
meep2 = ""

for i in range(1,len(meep) + 1):
    meep2 += meep[-i]

print(meep2)