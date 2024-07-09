phrase = str(input('Type a string: ')).upper().strip()

inversed = phrase[::-1]

if phrase == inversed:
    print('The string {} is a palindrome {}'.format(phrase, inversed))
else:
    print('The string {} is not a palindrome {}'.format(phrase, inversed))
