import phonenumbers

text = input("Enter the number:")
num = phonenumbers.parse(text, "US")

if (phonenumbers.is_possible_number(num) == True):
    print("Formatted Number: " + phonenumbers.format_number(num, phonenumbers.PhoneNumberFormat.E164))

else:
    print("Not a valid Number")