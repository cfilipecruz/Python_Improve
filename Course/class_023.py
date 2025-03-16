try:
    a = int(input('Type a number: '))
    b = int(input('Type another number: '))
    result = a / b
except (ValueError, TypeError):
    print(f'Wrong inserted data')
except KeyboardInterrupt:
    print('User cancelled')
except Exception as error:
    print(error)
except Exception as error:
    print(error.__class__.__name__)
else:
    print(result)
finally:
    print('This is the end of the program')