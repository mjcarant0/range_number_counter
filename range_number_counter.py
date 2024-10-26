# Given range:
# 1-10 = ?
# 11-20 = ?
# 21-30 = ?
# 31-40 = ?
# 41-50 = ?

import colorama #adding color for text
from colorama import Fore, Back, Style

#Use array to store the user's number
range_number = { #this is for the range
    "1-10": 0,
    "11-20": 0,
    "21-30": 0,
    "31-40": 0,
    "41-50": 0
}

user_input = {} #this is to store the inputted numbers and to track

#Use loop to ask the user to input their number from 1-50
while True:
    try:
        user_number = int(input(f"Choose a number from {Fore.BLUE}{Style.BRIGHT}1-50{Style.RESET_ALL}: "))
        
        #Adding a condition for invalid inputs
        if user_number < 1 or user_number > 50: #will stop if the number is less than 1 or greater than 5
            print(f"{Fore.RED}Invalid number.{Style.RESET_ALL}") 
            break
        
        if user_number in user_input: #will stop if the number is already used
            print(f"{Fore.RED}You already used this number.{Style.RESET_ALL}")
            break
        
        user_input[user_number] = True
        
        #Adding 1 in range_number's value in every input of the user
        if user_number >= 1 and user_number <= 10:
            range_number["1-10"] += 1
        if user_number >= 11 and user_number <= 20:
            range_number["11-20"] += 1
        if user_number >= 21 and user_number <= 30:
            range_number["21-30"] += 1
        if user_number >= 31 and user_number <= 40:
            range_number["31-40"] += 1
        if user_number >= 41 and user_number <= 50:
            range_number["41-50"] += 1

    except:
        break
    
#Print the result of how many inputted numbers are there in the given range
print(f"{Back.GREEN}{Fore.BLACK}Count of inputted numbers in each range{Style.RESET_ALL}")
for range, value in range_number.items():
    print(f"{Fore.CYAN}{range}{Style.RESET_ALL}: {value}")