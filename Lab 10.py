#Lab 10
#Nabeel Khan
#Nabeel.khan24@myhunter.cuny.edu
#February 21, 2020
#This program asks for a string, prints the length, prints the GC- content, index of first G and index of first C

meep = input("Enter a DNA string: ")

print("Length is ", len(meep))

print("GC-content is ", (meep.count("G") + meep.count("C")) / len(meep))
    
print("First G found at position", meep.find("G"))

print("First C found at position", meep.find("C"))