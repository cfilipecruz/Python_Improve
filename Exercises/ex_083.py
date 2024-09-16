expression = str(input('Type an expression: '))
values = []

for i in expression:
    if i == '(':
        values.append(i)
    elif i == ')':
        if len(values) > 0:
            values.pop()
        else:
            values.append(i)

if len(values) == 0:
    print('The parenthesis are correct')
else:
    print('The parenthesis are incorrect')