# main-0.py
import sys
from bank_account import BankAccount

def print_usage():
    print("Usage: python main-0.py <command>[:amount]")
    print("Commands:")
    print("  deposit:<amount>   - deposit amount into account")
    print("  withdraw:<amount>  - withdraw amount from account")
    print("  display             - show current balance")
    print("Examples:")
    print("  python main-0.py deposit:50")
    print("  python main-0.py withdraw:20")
    print("  python main-0.py display")

def main():
    # You may change the starting balance here or accept it from an environment/arg
    initial_balance = 100.0
    account = BankAccount(initial_balance)

    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    arg = sys.argv[1]
    if ':' in arg:
        command, param = arg.split(':', 1)
    else:
        command, param = arg, None

    command = command.lower()

    try:
        if command == "deposit" and param is not None:
            amount = float(param)
            if amount < 0:
                print("Amount must be non-negative.")
                sys.exit(1)
            new_balance = account.deposit(amount)
            print("Deposited: ${:.2f}".format(amount))
            account.display_balance()
        elif command == "withdraw" and param is not None:
            amount = float(param)
            if amount < 0:
                print("Amount must be non-negative.")
                sys.exit(1)
            success = account.withdraw(amount)
            if success:
                print("Withdrew: ${:.2f}".format(amount))
                account.display_balance()
            else:
                print("Insufficient funds.")
                account.display_balance()
        elif command == "display":
            account.display_balance()
        else:
            print_usage()
            sys.exit(1)
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        sys.exit(1)

if __name__ == "__main__":
    main()
