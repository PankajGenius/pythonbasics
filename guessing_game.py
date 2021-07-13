
i=0
while(i<=9):
    n = int(input('Enter a number'))
    
    if i>=9:
        print('-'*20)
        print('-' * 20)
        print('game over')
        break
    if n == 25 :
       # print('you won')
        print('you won in {} attempts'.format(i+1))
        break
    elif n > 25:
        print('oops this number is greater')

    else:
        print('oops u r close, enter a larger number')


    i=i+1
#print("game over")