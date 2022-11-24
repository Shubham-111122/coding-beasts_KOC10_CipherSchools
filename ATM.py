user_pin = 1234
user_balance = 10420.00
user_name = "Mr. John"
print("Welcome to your bank account", user_name, end="\n")

choice = 9
while True:
    print("\t0. Logout and Exit")
    print("\t1. View Account Balance")
    print("\t2. Withdraw Cash")
    print("\t3. Deposit Cash")
    print("\t4. Change PIN")
    choice = int(input("Enter number to proceed > "))
    print()
    if choice == 0:
        print("Exiting...")
        print("You have been logged out. Thank you!\n")
        break
    elif choice in (1, 2, 3, 4):
        num_of_tries = 3
        while num_of_tries != 0:
            input_pin = int(input("Please enter your 4-digit PIN > "))

            if input_pin == user_pin:
                print("Account authorized!\n")

                if choice == 1:
                    print("Loading Account Balance...")
                    print("Your current balance is Rs.", user_balance, end="\n\n")
                    break
                elif choice == 2:
                    print("Opening Cash Withdrawal...")

                    while True:
                        withdraw_amt = float(input("Enter the amount you wish to withdraw > "))

                        if withdraw_amt > user_balance:
                            print("Can't withdraw Rs.", withdraw_amt)
                            print("Please enter a lower amount!")
                            continue

                        else:
                            print("Withdrawing Rs.", withdraw_amt)
                            confirm = input("Confirm? Y/N > ")
                            if confirm in ('Y', 'y'):
                                user_balance -= withdraw_amt
                                if user_balance > 5000:
                                    print("Amount withdrawn - Rs.", withdraw_amt)
                                    print("Remaining balance - Rs.", user_balance, end="\n\n")
                                else:
                                    print("Low balance\n")
                                    print("Please enter a lower value\n")
                                break

                            else:
                                print("Cancelling transaction...")
                                print("Transaction Cancelled!\n")
                                break

                    break

                elif choice == 3:
                    print("Loading Cash Deposit...")

                    deposit_amt = float(input("Enter the amount you wish to deposit > "))
                    print("Depositing Rs.", deposit_amt)
                    confirm = input("Confirm? Y/N > ")
                    if confirm in ('Y', 'y'):
                        user_balance += deposit_amt
                        print("Amount deposited - Rs.", deposit_amt)
                        print("Updated balance - Rs.", user_balance, end="\n\n")
                    else:
                        print("Cancelling transaction...")
                        print("Transaction Cancelled!\n")

                    break
                elif choice == 4:
                    print("Loading PIN Change...")

                    pin_new = int(input("Enter your new PIN > "))

                    print("Changing PIN to", pin_new)
                    confirm = input("Confirm? Y/N > ")
                    if confirm in ('Y', 'y'):
                        user_pin = pin_new
                        print("PIN changed successfully! \n")
                    else:
                        print("Cancelling PIN change...")
                        print("Process Cancelled!\n")

                    break
            else:
                num_of_tries -= 1
                print("PIN incorrect! Number of tries left -", num_of_tries, end="\n")

        else:
            print("Exiting...")
            print("You have been logged out. Thank you!\n")
            break
    else:
        print("Invalid input!")
        print("\tEnter 0 to Logout and Exit!\n")
        continue
