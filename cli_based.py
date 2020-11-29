from main import Annuity, diff_payments
from time import sleep


def main():
    while True:
        print("What type of loan you have?\ntype 'annuity' for annuity payment,"
              "\ntype 'diff' for differentiated payment:")
        stage1 = input()
        sleep(2)
        if stage1 == "annuity":
            print('What do you want to calculate?\ntype "n" for number of monthly payments (period of loan),')
            stage2 = input('type "a" for annuity monthly payment amount,\ntype "p" for loan principal:\n')
            try:
                if stage2 == "n":
                    principal = int(input("Enter the Principal Amount: "))
                    pay = int(input("Enter the Monthly Payment Amount: "))
                    interest = float(input("Enter the Interest Applicable (should be specified without a '%' sign): "))
                    if principal > 0 and pay > 0 and interest > 0:
                        Annuity(interest).no_monthly_payments(pay, principal)
                        print()
                        sleep(3)
                    else:
                        print("You have enter incorrect value(s)\nPlease try again\n-\n")
                        sleep(1)
                elif stage2 == "a":
                    principal = int(input("Enter the Principal Amount: "))
                    period = int(input("Enter the number of months needed to repay the loan: "))
                    interest = float(input("Enter the interest applicable (should be specified without a '%' sign): "))
                    if principal > 0 and period > 0 and interest > 0:
                        Annuity(interest).annuity_pay(period, principal)
                        print()
                        sleep(3)
                    else:
                        print("You have enter incorrect value(s)\nPlease try again\n-\n")
                        sleep(1)
                elif stage2 == "p":
                    pay = float(input("Enter the Monthly Payment Amount: "))
                    period = int(input("Enter the number of months needed to repay the loan: "))
                    interest = float(input("Enter the interest applicable (should be specified without a '%' sign): "))
                    if period > 0 and pay > 0 and interest > 0:
                        Annuity(interest).principal(pay, period)
                        print()
                        sleep(3)
                    else:
                        print("You have enter incorrect value(s)\nPlease try again\n-\n")
                        sleep(1)
                else:
                    print("Incorrect input!!!\nTry Again\n-\n")
                    sleep(3)
            except ValueError:
                print("I expected numbers!\nLet's try again\n-\n-\n")
                sleep(1)
        elif stage1 == "diff":
            try:
                principal = int(input("Enter the Principal Amount: "))
                period = int(input("Enter the number of months needed to repay the loan: "))
                interest = float(input("Enter the interest applicable (should be specified without a '%' sign): "))
                if principal > 0 and period > 0 and interest > 0:
                    diff_payments(principal, period, interest)
                    print()
                    sleep(3)
                else:
                    print("You have enter incorrect value(s)\nPlease try again\n-\n")
                    sleep(1)
            except ValueError:
                print("I expected numbers!\nLet's try again\n-\n-\n")
                sleep(1)
        else:
            print("Incorrect input!!!\nTry Again\n-\n")
            sleep(3)


if __name__ == '__main__':
    print("Credit Calculator")
    main()
