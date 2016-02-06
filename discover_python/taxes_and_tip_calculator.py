"""The Purpose of this Script
==========================
This program has been created to fulfill the discovering_python project at Holberton School. The purpose is to create a python script that will ask the user to input the value of the meal, the taxes, and the tip, and then return the total amount of money that they need to pay.

Author
======
This script is written by Gloria Bwandungi, a Software Engineer working on her skills at Holberton school. My current passion is Mixed Reality - a combination of Virtual Reality and Augmented Reality for the purpose of immersive story telling. But this is a means to an end. I really want to build starships and be a starship captain.

This first line prints out the title of the script.

"""

print "Welcome to the taxes and tip calculator!" #This is the welcome message of the script.
print "What is the price before tax?", #Asks the user for the price of the meal.
price = float(raw_input()) #The price is turned into a floating number and asigned to the 'price' variable.
print "What are the taxes? (in %)", #Asks the user to input the taxes to be paid on the meal.
tax = float(raw_input()) #Assigns the tax to the variable 'tax' as a floating number.
print "What do you want to tip? (in %)", #Asks the user to input the tip they are willing to pay.
tip1 = float(raw_input()) #Assigns the tip to the variable 'tip1' as a floating number.

meal = price + price * (tax/100) #Changes the tax to %, and adds the tax to the price of the meal, assigning it to the variable 'meal'. 
tip2 = meal * (tip1/100) #Changes the tip to % and calculates it based on the value of the 'meal' variable. Assigns it 
total = meal + tip2 #Adds the 'meal' and 'tip2' variables and assigns them to 'total' variable


print "The price you need to pay is: $%.6f" %(total) #Outputs the value of 'total' and formats it to have 6 decimal places.
