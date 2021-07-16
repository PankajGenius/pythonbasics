#pankaj ka code chk kro harry sir shi bnaya hai ya ni
n=int(input("Enter no of rows\n "))
choose = int(input('Enter the value 0 or 1\n'))
if  choose == 0:
    for i in range(1, n+1):
        print('*' * i)
else:
    for i in range(n,0,-1):
        print(i*'*')