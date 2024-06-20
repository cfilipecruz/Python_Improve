price = float(input('What was the price? '))
print('-=-'* 10)
print('Payment Forms')
print('[ 1 ] Pay Cash')
print('[ 2 ] Pay with Card')
print('[ 3 ] Pay 2x card')
print('[ 4 ] Pay 3x+ card')

option = int(input('Which payment option would you like? '))
if option == 1:
    print('You will pay {} with a discount'.format(price*0.9))
elif option == 2:
    print('You will pay {}'.format(price))
elif option == 3:
    installment =  price * 1.5
    print('You will pay {} in installments of {} per month'.format(installment, installment/2))
elif option == 4:
    installment = price * 2
    numberInstallments = int(input('How many installments would you like? '))
    print('You will pay {} in installments of {} per month'.format(installment, installment/numberInstallments))
else:
    print('Invalid option, please type a number on the list')

