from datetime import datetime #Importing datetime module to work with dates


def get_days_from_today(date): 
    """Calculate number of days days from today to the given date.
    Checking correctness of the date format"""
    
    try:
        my_date = datetime.strptime(date, "%Y-%m-%d") #Converting inout string to date format
        now = datetime.today() 
        difference = now - my_date #getting the difference between today and the given date
        return difference
    
    except ValueError: #Handling incorrect date format
        print(f"{date} - Неправильний формат дати. Будь ласка, використовуйте формат РРРР-ММ-ДД.") #Error message
        return None
    

date = input("Введіть дату у форматі РРРР-ММ-ДД: ") #Date input from the user

result = get_days_from_today(date) #Calling the function with user input


if result is not None: 
    print(result.days) #Printing result in number of days