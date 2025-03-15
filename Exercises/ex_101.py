
def vote(bornin):
    from datetime import date
    year = date.today().year
    age = year - int(bornin)
    if int(age) < 18:
        return f'You are {age} years old, you cant Vote'
    elif 18 <= int(age) < 65:
        return f'You are {age} years old, you need to vote'
    elif int(age) >= 65:
        return f'You are {age} years old, you don\'t need to vote'
    else:
        return False

while True:
    #Main
    voted = vote(input('What year did you born? '))
    if not voted:
        print(f'Error, That is not a valid age, please type again')
    else:
        print(voted)
        break
