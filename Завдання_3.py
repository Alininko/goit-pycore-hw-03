def normalize_phone(phone_number) -> str: #creating function for formatting phone numbers to the following example +380952345678
    import re
    pattern = r"\W"
    phone_number = re.sub(pattern, "", phone_number) #removing all spaces
    pattern2 = r"[A-Za-z]"
    phone_number = re.sub(pattern2, "", phone_number) #removing all letters
    
    if not re.search(r'(^38)', phone_number): #checking for phone numbers where 38 is missing 
        phone_number = "38" + phone_number #adding 38
    if not re.search(r"(^\+)", phone_number): #checking for phone numbers where + is missing
        phone_number = "+" + phone_number #adding +
    return phone_number #returning phone numbers with +38 at the start, followed by numbers only


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)