def get_upcoming_birthdays(users):

    from datetime import datetime, timedelta, date
    today = datetime.today().date()
    future_date = today + timedelta(days=7)  # Adding 7 days to current date
    upcoming_birthdays = [] #creating empty list

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date() #converting sttring into date
        birthday = date(today.year, birthday.month, birthday.day) #adjusting birthday date to current year for further comparison logic

        if birthday < today:
            birthday = date(birthday.year +1, birthday.month, birthday.day) #if the date is before current date add 1 year to get it included into the list next year

        if today <= birthday <= future_date and birthday.weekday() < 5:
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": birthday.strftime("%Y.%m.%d") }) #if birthday is on a weekday - add it to upcoming_birthdays list with congratulation_date

        if today <= birthday <= future_date and birthday.weekday() == 5: 
            birthday = birthday + timedelta(days=2) #if birthday is on Saturday, shift the date to Monday
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": birthday.strftime("%Y.%m.%d") }) #add Monday to upcoming_birthdays list with comgratulation date

        if today <= birthday <= future_date and birthday.weekday() == 6:
            birthday = birthday + timedelta(days=1) #if birthday is on Sunday, shift the date to Monday
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": birthday.strftime("%Y.%m.%d") }) #add Monday to upcoming_birthdays list with comgratulation date
            
            return upcoming_birthdays #return a full list 


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Alice White", "birthday": "2010.03.12"},
    {"name": "Kate", "birthday": "2026.01.01"},
    {"name": "Mike", "birthday": "2020.02.13"},
    {"name": "Sam", "birthday": "1999.02.08"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)