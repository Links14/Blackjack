# Trevor Loth
# 2025-1-28

# This homes the function which may be used to determine the value of a given hand


# Param: Hand - any number of cards denoted by their card code
# (ie. CA would be an Ace of Clubs)
# Return: valueList - list of possible valid values for the hand
def calc_hand(hand):
    valueList = [0]

    # i is a string denoted by a letter then a number
    for i in hand:
        if "A" in i:
            for j in range(len(valueList)):
                if valueList[j] + 11 <= 21:
                    valueList.append(valueList[j] + 1) # add a copy of the current
                    valueList[j] += 11
                else:
                    valueList[j] += 1
        elif "J" in i or "Q" in i or "K" in i or "1" in i:
            for j in range(len(valueList)):
                valueList[j] += 10
        else:
            for j in range(len(valueList)):
                valueList[j] += int(i[1])
    
    valueList = sorted(valueList) 
    for i in range(len(valueList)-1, -1, -1):
        if valueList[i] > 21:
            valueList.pop(i)
        else: # sorted list means early exit
            break
    
    return valueList
