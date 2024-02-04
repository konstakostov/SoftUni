from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    INTEREST = 1.5
    AMOUNT = 2000
    INCREASE_INTEREST = 0.2

    def __init__(self):
        super().__init__(interest_rate=self.INTEREST, amount=self.AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += self.INCREASE_INTEREST
