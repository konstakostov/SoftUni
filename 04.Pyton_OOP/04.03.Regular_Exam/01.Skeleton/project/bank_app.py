from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOANS = ["StudentLoan", "MortgageLoan"]
    VALID_CLIENTS = ["Student", "Adult"]

    def __find_client_by_id(self, client_id: str):
        for client in self.clients:
            if client.client_id == client_id:
                return client

    def __find_first_loan_by_type(self, loan_type: str):
        loan = next(filter(lambda l: l.__class__.__name__ == loan_type, self.loans), None)
        return loan

    def __init__(self, capacity: int):
        self.capacity: int = capacity

        self.loans: list = []
        self.clients: list = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_LOANS:
            raise Exception("Invalid loan type!")

        new_loan = None
        if loan_type == "StudentLoan":
            new_loan = StudentLoan()

        elif loan_type == "MortgageLoan":
            new_loan = MortgageLoan()

        self.loans.append(new_loan)

        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENTS:
            raise Exception("Invalid client type!")

        if len(self.clients) >= self.capacity:
            return f"Not enough bank capacity."

        new_client = None
        if client_type == "Student":
            new_client = Student(client_name, client_id, income)

        elif client_type == "Adult":
            new_client = Adult(client_name, client_id, income)

        self.clients.append(new_client)

        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = self.__find_client_by_id(client_id)
        loan = self.__find_first_loan_by_type(loan_type)

        if type(client).__name__ == "Student" and type(loan).__name__ != "StudentLoan":
            raise ValueError("Inappropriate loan type!")
        elif type(client).__name__ == "Adult" and type(loan).__name__ != "MortgageLoan":
            raise ValueError("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)

        print(type(client).__name__)
        print(type(loan).__name__)

        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = self.__find_client_by_id(client_id)

        if not client:
            raise Exception("No such client!")

        if len(client.loans) > 0:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)

        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        loans_increased = 0

        for loan in self.loans:
            if type(loan).__name__ == loan_type:
                loan.increase_interest_rate()

                loans_increased += 1

        return f"Successfully changed {loans_increased} loans."

    def increase_clients_interest(self, min_rate: float):
        interests_increased = 0

        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()

                interests_increased += 1

        return f"Number of clients affected: {interests_increased}."

    def get_statistics(self):
        granted = 0
        for client in self.clients:
            for loan in client.loans:
                if type(loan).__name__ == "StudentLoan":
                    granted += 2000
                else:
                    granted += 50000

        not_granted = 0
        for loan in self.loans:
            if type(loan).__name__ == "StudentLoan":
                not_granted += 2000
            else:
                not_granted += 50000

        avg_interest_rate = 0
        if len(self.clients) != 0:
            avg_interest_rate += sum([client.interest for client in self.clients]) / len(self.clients)

        total_clients_count = len(self.clients)
        total_clients_income = sum([client.income for client in self.clients])
        loans_count_granted_to_clients = sum([len(client.loans) for client in self.clients])
        granted_sum = granted
        loans_count_not_granted = len(self.loans)
        not_granted_sum = not_granted
        avg_client_interest_rate = avg_interest_rate

        result = f"Active Clients: {total_clients_count}\n"
        result += f"Total Income: {total_clients_income:.2f}\n"
        result += f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}\n"
        result += f"Available Loans: {loans_count_not_granted}, Total Sum: {not_granted_sum:.2f}\n"
        result += f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"

        return result
