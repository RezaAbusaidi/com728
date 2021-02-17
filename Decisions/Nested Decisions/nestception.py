print('where should I look?')
lookfirst = input('')

if lookfirst.strip() == 'in the bedroom':
    print('where in the bedroom?')
    bedroom = input()
    if bedroom == 'under the bed':
        print('Found some shoes but no battery')
    else:
        print('Found some mess but no battery.')

if lookfirst == 'in the bathroom':
    print('Where in the bathroom should I look?')
    bathroom = input()
    if bathroom == 'in the bathtub':
        print('Found a rubber duck but no battery')
    else:
        print('Found a wet surface but no battery.')

if lookfirst == 'in the lab':
    print('Where in the lab should I look?')
    lab=input()
    if lab == 'on the table':
        print('Yes! I found my battery!')
    else:
        print('Found some tools but no battery.')
else:
    print('I do not know where that is but I will keep looking')
    
