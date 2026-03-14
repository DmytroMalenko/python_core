balance = 1000

while True:
    try:
        amount = input("Write sum of money to withdraw: ")

        amount = int(amount)

        if amount <= 0:
            raise Exception("Amount must be greater than 0")

        if amount > balance:
            raise Exception("Not enough balance")

        if amount % 10 != 0:
            raise Exception("Amount must be a multiple of 10")

        print("Take your money:", amount)

    except ValueError:
        print("Incorrect number!")

    except Exception as ex:
        print(ex)

    finally:
        print("Завершення транзакції")

    break





