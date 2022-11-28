print("Welcome to DaInvinc Bank. your comfort and security is our priority")
pinTrial = 3
UserPin = 4545
TotalBalance = 10000

while pinTrial != 0:
    pin = int(input("Please enter your four digit pin: "))
    if pin != UserPin:
        pinTrial -= 1
        print("Wrong pin! Please enter the correct pin", + pinTrial + "trial left")
    else:
        UserOption = input("Deposit or Withdrawal : ")
        if UserOption == "Deposit":
            Udeposit = int(
                input("Please the amount you would like to deposit: "))
            print(Udeposit, "$ have been deposited into your account")
        if UserOption == "Withdrawal":

            Uwithdraw = int((
                input("Enter the amount you would like to withdraw : ")))

            if Uwithdraw > TotalBalance:
                print(
                    "You do not have sufficient fund in your account for this transaction")
            else:
                print(Uwithdraw, "$ have been withdrawn from your account")

    exitOption = input(
        "Do you want to perform another transaction? Yes or No: ")

    if exitOption == "No":
        print("Thank you for your transaction")
        break
    else:
        continue
