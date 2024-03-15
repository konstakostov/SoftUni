from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    INTEREST = 3.5
    AMOUNT = 50000.0
    INCREASE_INTEREST = 0.5

    def __init__(self):
        super().__init__(interest_rate=self.INTEREST, amount=self.AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += self.INCREASE_INTEREST
