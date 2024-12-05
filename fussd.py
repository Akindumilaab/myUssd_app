import time as tm

class Ussd:
    def __init__(self):
        self.network = 'Bims network'
    def dashbord(self):
        print('Hello...')
        tm.sleep(1)
        user = input('Input ussd: ')
        if user == '*312#':
            print(f'Welcome to {self.network} service🙌.')
            ussd = input('''
            1. DATA PLAN
            2. AIRTIME
            3. BORROW AIRTIME
            4. CHECK BALANCE
            5. EXIT
            CHOOSE:-  ''')
             
            if ussd == '1':
                self.DATAPLAN()
            elif ussd == '2':
                self.AIRTIME()
            elif ussd == '3':
                self.BORROW_AIRTIME()
            elif ussd == '4':
                self.CHECK_BALANCE()
            elif ussd == '5':
                self.EXIT()
                
            else:
                print("Invalid code.")
                print('Dail *312# to iniate a transaction')
                self.dashbord()
        else:  
            print('Inavlid code') 
            self.dashbord ()   
    def DATAPLAN(self):
        choose_plan = input('''
        1. weekly plan
        2. monthly plan
        3. daily plan
        0. exit
                            
   choose:- ''')
        if choose_plan == '1':
            print('weekly plan activated')
            self.DATAPLAN()
        elif choose_plan == '2':
             print('Montly plan activated')
             self.DATAPLAN()
        elif choose_plan == '3':
             print('Daily plan activated')
             self.DATAPLAN()
        elif choose_plan == '0':
            print('Thank you for your time👍')
            exit()
        else:
            print('Check that your inputing the right code')
            self.dashbord()

    def AIRTIME(self):
        amount = int(input('Input amount: '))
        user = input('''
        1. self
        2. Thrid party
        0. exit
 choose:- ''')
        if amount < 5000 and user == '1':
            print('Account recharged sucessfully')
            self.AIRTIME()

        elif amount > 2000 and user == '2':
            print('Thrid party was credited successfully')
            self.AIRTIME()
            
        elif user == '0':
            print('Thank you for your time')
            exit()
        else:
            print('Wrong input')
            self.dashbord()

    def BORROW_AIRTIME(self):
        borrow = input('input amount: ')
        if borrow  >= 500:
            print('You are not eligible for this amount')
            self.BORROW_AIRTIME()
        elif borrow < 500:
            print(f'Your new balance is {borrow}')
            self.BORROW_AIRTIME()
            
        else:
            print('Wrong input. Would you like to perform another transcation?')
            self.dashbord()

    def CHECK_BALANCE(self):
        print('Your account balnce is -------')
        self.dashbord()

    def EXIT(self):
        print('loading........')
        tm.sleep(1)
        print(f'Thank you for using {self.network}👍')
        

app = Ussd()
app.dashbord()