import math


class Annuity:
    def __init__(self, interest):
        self.interest = interest / 1200

    def no_monthly_payments(self, pay, principal):
        if pay == principal:
            print("It will take 1 month to repay this loan!")
        else:
            period = math.ceil(math.log(pay / (pay - self.interest * principal), 1 + self.interest))
            years, months = divmod(period, 12)
            if 1 < period < 13:
                print("It will take {} months to repay this loan!".format(period))
            elif months == 0:
                print("It will take {} years to repay this loan!".format(years))
            else:
                print("It will take {} years and {} months to repay this loan!\n".format(math.floor(years), months))
            overpayment = round((pay * period) - principal)
            print("Overpayment =", overpayment)

    def principal(self, pay, months):
        denominator = (self.interest * math.pow(1 + self.interest, months)) / (math.pow(1 + self.interest, months) - 1)
        principal = math.floor(pay / denominator)
        print("Your credit principal =", principal)
        print()
        overpayment = round((pay * months) - principal)
        print("Overpayment =", overpayment)

    def annuity_pay(self, period, principal):
        annuity_pay = math.ceil(principal * ((self.interest * ((1 + self.interest) ** period)) /
                                             (((1 + self.interest) ** period) - 1)))
        print("Your annuity payment = {}!\n".format(annuity_pay))
        overpayment = round((annuity_pay * period) - principal)
        print("Overpayment =", overpayment)


def diff_payments(principal, month, interest):
    interest /= 1200
    total = 0
    for i in range(1, month + 1):
        diff_pay = math.ceil((principal / month) + interest * (principal - (principal * (i - 1) / month)))
        total += diff_pay
        print("Month {}: payment is {}".format(i, diff_pay))
    print("\nOverpayment =", round(total - principal))
