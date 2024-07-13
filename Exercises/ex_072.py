text = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
        'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')

number = int(input('Type a number between 0 and 20: '))
while number < 0 or number > 20:
    print('That is not a valid number.')
    number = int(input('Type a number between 0 and 20: '))

print(f'You types the number {text[number]}')