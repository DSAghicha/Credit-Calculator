import argparse
from main import Annuity, diff_payments


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Credit Calculator")
    parser.add_argument("--type", help="Indicates the type of payment: 'annuity' or 'diff'(differentiated)")
    parser.add_argument("--payment", help="Monthly payment amount", type=int)
    parser.add_argument("--principal", help="Principal Amount", type=int)
    parser.add_argument("--periods", help="The number of months needed to repay the loan", type=int)
    parser.add_argument("--interest", help="Interest applicable (should be specified without a percent sign)",
                        type=float)
    args = parser.parse_args()
    # Checking for Errors
    if args.type not in ['annuity', 'diff'] or (args.type == "diff" and args.payment is not None) or \
            args.interest is None or len(vars(args)) < 5:
        print("Incorrect parameters.")
    else:
        # Calculating period in annuity
        if args.type == 'annuity' and args.periods is None:
            # noinspection PyTypeChecker
            if args.interest > 0 and args.payment > 0 and args.principal > 0:
                Annuity(args.interest).no_monthly_payments(args.payment, args.principal)
            else:
                print("Incorrect parameters.")
        # Calculating principal in annuity
        elif args.type == 'annuity' and args.principal is None:
            # noinspection PyTypeChecker
            if args.interest > 0 and args.payment > 0 and args.periods > 0:
                Annuity(args.interest).principal(args.payment, args.periods)
            else:
                print("Incorrect parameters.")
        # Calculating annuity
        elif args.type == 'annuity' and args.payment is None:
            if args.interest > 0 and args.principal > 0 and args.periods > 0:
                Annuity(args.interest).annuity_pay(args.periods, args.principal)
            else:
                print("Incorrect parameters.")
        # Calculating differentiated payments
        elif args.type == 'diff':
            diff_payments(args.principal, args.periods, args.interest)
