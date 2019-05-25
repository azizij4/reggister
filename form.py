star = True
while star == True:
    print('''
                  STUDENT REGISTRATION FORM
    ''')
    print('''
                 Are you already registered??? 

                   YES         or        No                  

                  ''')
    decision=str(input(":..."))
    while decision!=int:
        if decision == 'yes':
            print('Check your credentials here')
            star = True
            break
        elif decision == 'no':
            star = True 
            while star == True:
                 print('\t\t\tREGISTRATION FORM')
                 first_name=str(input(  'First name:....'))
                 second_name=str(input( 'Second name:...'))
                 last_name=str(input(   'Last name:.....'))
                 email_addr=str(input(  'Email address:.'))
                 phone_number=int(input('Phone number:..'))
                 Reg=str,int(input(     'ID number:.....'))
                 print('''

                            Do you want to
                      SUBMIT     or     RESET

                      ''')
                 reg=str(input(':...'))
                 while reg!=int:
                     if reg == 'submit':
                         print('congratulation your STUDENT REGISTRATION FORM is submitted')
                         star = True
                         break
                     elif reg == 'reset':
                         print('RESET YOUR FORM (Re-register again)')
                         break
                     else:
                         print('Invalid choise Re- register again')
                         break





            star = False
            break
        else:
            print('Please choose again')
            break


