#Lab 9
#Nabeel Khan
#Nabeel.khan24@myhunter.cuny.edu
#February 20, 2020
#This program takes in a string and encodes it by a shift of 16

meep = input("Enter a word: ")
meep2 = ""

for i in range(len(meep)):
    if(ord(meep[i]) + 16 > 122):
        meep2 += chr(ord(meep[i]) - 10)
    else:
        meep2 += chr(ord(meep[i]) + 16)
    
print(meep2)