# script checks if a number is a valid cameroon phone number

txt=input("Enter the number: ")

message = 'call me at +237677084145 or 672158900'

found_numbers = []

def is_phone_number(text: str):
    if text.startswith("+237"):
        text = text.removeprefix("+237")
    elif text.startswith("6"):
        pass
    else:
        return False

    if len(text) != 9:
        return False
    
    return text.isdecimal()


for i in range(len(message)):
    segment1 = message[i: i + 9]
    segment2 = message[i:i + 13]
    if is_phone_number(segment2):
        found_numbers.append(segment2)
        print(len(segment2))
    elif is_phone_number(segment1):
        print(len(segment1))
        found_numbers.append(segment1)
    
    
print(found_numbers)
