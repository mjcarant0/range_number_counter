# Given range:
# 1-10 = ?
# 11-20 = ?
# 21-30 = ?
# 31-40 = ?
# 41-50 = ?

#Use array to store the user's number
range_number = {
    "1-10": 0,
    "11-20": 0,
    "21-30": 0,
    "31-40": 0,
    "41-50": 0
}

#Use loop to ask the user to input their number from 1-50
while True:
    try:
        user_number = int(input("Choose a number from 1-50: "))
        
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
for range, value in range_number.items():
    print(f"{range}: {value}")