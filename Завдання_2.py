def get_numbers_ticket(min, max, quantity): #function returning random numbers is selected range
    import random
    
    if min<1 or max>1000 or quantity<1 or quantity>max: #validating correctness of range and quantity
        return None
    else:
        lottery_list = range(min, max+1) #creating a list with range set by parameters
        lottery = random.sample(lottery_list, k=quantity) #generating unique random numbers from the range
        lottery.sort() #sorting the list
    return lottery #returning sorted list of numbers

lottery_numbers = get_numbers_ticket(1, 100, 22) #calling the function with specified parameters
print("Your lottery numbers: ", lottery_numbers)