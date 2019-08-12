while True:
    where  = input('Where you are going?')
    if where == 'gym':
        print('bring:shoes,water and shorts')
        break
    elif where == 'school':
        print('bring:homework(avoid Mr.Riches)')
        break
    elif where == 'mall':
        print('bring:your mom\'s credit card for the mall')
        break
    else:
        print('only gym,school and mall')