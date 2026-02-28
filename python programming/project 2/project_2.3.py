"""
project_2.3.py

defines a BankAccount class with deposit and withdrawal methods.

author: christopher romo
created: 2023-07-05
"""


class BankAccount:
    """the BankAccount class creates a bank account object."""

    account_counter = 0

    def __init__(self) -> None:
        BankAccount.account_counter += 1
        self.account_number = BankAccount.account_counter
        self.balance = 0

    def deposit(self, deposit_amount: int) -> None:
        """
        deposits the given amount into the account.

        args:
            deposit_amount (int): the amount to deposit.
        """

        self.balance += deposit_amount
        print(
            f"Account Number: {self.account_number}, Deposit Amount: {deposit_amount}, Updated Balance: {self.balance}"
        )

    def withdrawal(self, withdrawal_amount: int) -> None:
        """
        withdraws the given amount from the account if sufficient funds exist.

        args:
            withdrawal_amount (int): the amount to withdraw.
        """

        if self.balance >= withdrawal_amount:
            self.balance = self.balance - withdrawal_amount
            print(
                f"Account Number: {self.account_number}, Withdrawal Amount: {withdrawal_amount}, Updated Balance: {self.balance}"
            )
        else:
            print(f"Error: Insufficient Funds in Account Number: {self.account_number}")

    def __str__(self) -> str:
        return f"Account Number: {self.account_number}, Current Balance: {self.balance}"


def main() -> None:
    """shows a demonstration of the BankAccount class."""

    # demonstration of the BankAccount class
    taylors_account = BankAccount()
    taylors_account.deposit(3000)
    taylors_account.withdrawal(1000)
    print(taylors_account.__str__())

    dannys_account = BankAccount()
    dannys_account.deposit(1000)
    dannys_account.withdrawal(2000)
    print(dannys_account.__str__())


if __name__ == "__main__":
    main()
