class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
data = input()

while data != "Stop":
    sender, receiver, content = data.split()
    email = Email(sender, receiver, content)
    emails.append(email)

    data = input()

sent_emails_indexes = [int(idx) for idx in input().split(", ")]

for index, email in enumerate(emails):
    if index in sent_emails_indexes:
        emails[index].send()
    print(f"{email.sender} says to {email.receiver}: "
          f"{email.content}. Sent: {email.is_sent}")
