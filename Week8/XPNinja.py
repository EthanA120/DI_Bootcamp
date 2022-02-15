# TASK: Call History
class Phone:
    """
        1. Create a class called Phone. This class takes a parameter called phone_number.
            When instantiating an object create an attribute called call_history which value is an empty list.

        2. Add a method called call that takes both self and other_phone (i.e. another Phone object) as parameters.
            The method should print a string stating who called who, and add this string to the phone’s call_history.

        3. Add a method called show_call_history. This method should print the call_history.

        4. Add another attribute called messages to your __init__() method which value is an empty list.

        5. Create a method called send_message which is similar to the call method.
            Each message should be saved as a dictionary with the following keys:
            "to"
            "from"
            "content"

        6. Create the following methods:
            show_outgoing_messages(self)
            show_incoming_messages(self)
            show_messages_from(self)

        7. Test your code !!!
    """

    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other_phone):
        self.call_history.append([other_phone.phone_number, "Outgoing"])
        other_phone.call_history.append([self.phone_number, "Incoming"])
        print(f"You've just called {other_phone.phone_number}: Outgoing")

    def show_call_history(self):
        print("Call history:")
        [print(f"{call[0]}: {call[1]}") for call in self.call_history]

    def send_message(self, other_phone, message):
        self.messages.append({"to": other_phone.phone_number, "from": self.phone_number, "content": message})
        other_phone.messages.append({"to": other_phone.phone_number, "from": self.phone_number, "content": message})

    def show_outgoing_messages(self):
        print("Outgoing messages:")
        for message in self.messages:
            if self.phone_number != message["to"]:
                print(f"{message['from']}: {message['content']}")

    def show_incoming_messages(self):
        print("Incoming messages:")
        for message in self.messages:
            if self.phone_number != message["from"]:
                print(f"{message['from']}: {message['content']}")

    def show_messages_from(self, other_phone):
        for message in self.messages:
            if other_phone.phone_number == message["from"]:
                print(f"{message['from']}: {message['content']}")


ethan = Phone(123)
adir = Phone(456)
ravid = Phone(789)

ethan.call(adir)
ethan.show_call_history()
adir.show_call_history()
ethan.send_message(adir, "How are you?")
ravid.send_message(adir, "What's up?")
ethan.show_outgoing_messages()
adir.show_incoming_messages()
print("Messages from Ethan:")
adir.show_messages_from(ethan)
print("Messages from Ravid:")
adir.show_messages_from(ravid)


