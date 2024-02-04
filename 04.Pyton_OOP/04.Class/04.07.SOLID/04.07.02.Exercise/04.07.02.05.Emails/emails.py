from abc import ABC, abstractmethod


class IContent(ABC):
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format_content(self):
        ...


class MyMl(IContent):
    def format_content(self):
        return '\n'.join(['<myML>', self.text, '</myML>'])


class HTML(IContent):
    def format_content(self):
        return '\n'.join(['<html>', self.text, '</html>'])


class IProtocol(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def format_protocol(self):
        ...


class MySender(IProtocol):
    def format_protocol(self):
        return ''.join(["I'm ", self.name])


class MyReceiver(IProtocol):
    def format_protocol(self):
        return ''.join(["I'm ", self.name])


class IEmail(object):
    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class Email(IEmail):
    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender: IProtocol):
        self.__sender = sender.format_protocol()

    def set_receiver(self, receiver: IProtocol):
        self.__receiver = receiver.format_protocol()

    def set_content(self, content: IContent):
        self.__content = content.format_content()

    def __repr__(self):
        template = f"Sender: {self.__sender}\n" \
                   f"Receiver: {self.__receiver}\n" \
                   f"Content:\n{self.__content}"

        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content)


myml = MyMl("Hello, there!")
email = Email('IM')
email.set_sender('qmal')
email.set_receiver('james')
email.set_content(myml)
print(email)
