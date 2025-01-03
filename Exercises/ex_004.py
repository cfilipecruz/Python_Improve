value = input('Type a value: ')

#Verify wich type its the variable
print("The variable is always a", type(value))
# Verify if the variable is only text
print("Value is a string?", value.isalpha())
# Verify if the variable is only numbers
print("Value is a number?", value.isnumeric())
# Verify if the variable as text or numbers
print("Value is only numbers?", value.isalnum())
# Verify if the variable is only capital letters
print("Value is only capital case?", value.isupper())
# Verify if the variable is only lowercase letters
print("Value is only lower case?", value.islower())
# Verify if the variable can be a name of a variable falseex:1teste
print("Value is only punctuation?", value.isidentifier())
# Verify if the variable is printable falseex: @response.py\n@response.py
print("Value is only punctuation characters?", value.isprintable())
# Verify if the variable is only spaces
print("Value is only white space?", value.isspace())



