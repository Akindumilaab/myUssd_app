                    # ussd application
user = input('input USSD code: ')
if user == '*312#':
    print('Welcome to my USSD application')
    ussd = input('''
            1. Buy data plans
            2. Buy Airtime
            3. Borrow Airtime or Data 
            4. Share data
            0. Exit
  choice: ''')
    if ussd == '1':
        print('''
        1. daily plan
        2. weekly plan
        ''')
        plan = input('choose plan: ')
        if plan == '1':
         print('daily plan activated')
        elif plan == '2':
         print('Weekly plan activated')
        else:
         print('Invalid choose. try again.')
    elif ussd == '2':
        print('Airtime purchased')
    elif ussd == '3':
        print('''
        1.Borrow Airtime
        2.Borrow Data
        ''')
        Borrow = input('choose : ')
        if Borrow == '1':
            print('Airtime borrowed successfully')
        elif Borrow == '2':
            print('data borowed successfully')
        else:
            print('Invalid. Check your code')
    elif ussd == '4':
        print('Data shared')
    elif ussd == '0':
        print('Thank you for your time👍.')
        exit()
    else:
        print('Invaild USSD code.Try again...... ')
else:
    print('Invalid USSD code. Dail *312# to continue this plan;-)')