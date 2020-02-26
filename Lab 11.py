#Lab 11
#Nabeel Khan
#Nabeel.khan24@myhunter.cuny.edu
#February 24, 2020
#This program takes in a noun and two verbs and forms a sentence

meep = "If it VERB1 like a NOUN and VERB2 like a NOUN, it probably is a NOUN."

noun = input("Enter a noun: ")
meep = meep.replace("NOUN", noun, 3)

verb1 = input("Enter a verb: ")
meep = meep.replace("VERB1", verb1)

verb2 = input("Enter another verb: ")
meep = meep.replace("VERB2", verb2)

print(meep)