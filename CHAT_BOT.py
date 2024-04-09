import re

print("+++++++++++++++++++++++++++++++++++++++++\n"
      "|     Welcome To Harsha Residency       |\n"
      "+++++++++++++++++++++++++++++++++++++++++")


class ChatBot:
    def __init__(self):
        self.enquiries = [
            (r"hii|hai|hey", "Hello Sir/Madam, How can i help you"),
            (r"how are you", "Fine how are you sir/ Madam, How can i help you?"),
            (r"book a room|i want room|i want rooms|do you have any rooms", "Sure! Which day would you like to check in and check out?"),
            (r"on (sunday|monday|tuesday|wednesday|thursday|friday|saturday)", "ok sir,\n you want more details type 'Details' and\n You want to Address type 'Address'\n You need contact no. type 'Contact'"),
            (r"details of your hotel", "Ask anything you want sure i help you"),
            (r"address|give me the address|location|give me location", "Yes sure!, It is in Koramangala 3rd cross\n You need contact no. type 'Contact'"),
            (r"room available", "Yes Sir/Madam rooms are available which type of room you want?\n you can Type details"),
            (r"contact", "91+ 7582400879"),
            (r"details of room|details", "We have 4 types of rooms like\n 1.Single room\n 2.Double rooms\n 3.Medium room\n 4.premium rooms are available"),
            (r"single room|cost of single room|single room cost", "Single room cost is: 2000\n You want to book Type 'Book single'"),
            (r"double room|double rooms cost|cost of double room", "Double room cost is 5000\n You want to book Type 'Book double'"),
            (r"medium room|medium rooms cost|cost of medium room", "Medium room cost is 8000\n You want to book Type 'Book medium'"),
            (r"premium room|premium rooms cost|cost of premium room", "Medium room cost is 10000\n You want to book Type 'Book premium'"),
            (r"alright|Thanks for rooms", "Ok Sir/Madam which type rooms you want"),
            (r"is the room air conditioned", "All our rooms are centrally air-conditioned."),
            (r"book single|book double|book medium|book premium", "Ok sir/madam, Please tell me the payment methode sir/madam\n *Card\n *UPI\n *Cash"),
            (r"upi|cash|card", "Ok Sir/Madam\n If you complete the payment \n please type 'Payment completed'"),
            (r"payment completed|i payed", "Ok sir/Madam your room is booked"),
            (r"ok thank you|ok", "Ok Sir/Madam bye")
        ]

    def respond(self, user_input):
        for enquiry, response in self.enquiries:
            match = re.search(enquiry, user_input.lower())
            if match:
                return response

        return "Sorry!, I do not Understand that. Please ask something else related to our Residency"


chat_bot = ChatBot()

while True:
    user_input = input("\nYou: ")
    if user_input.lower() == "exit":
        print("Thank for coming, Good bye ")
        break
    if user_input.lower() == "bye":
        print("\nThank You For Choosing 'Harsha Residency', Bye\n\t ***** Have A Nice Day ***** ")
        break
    response = chat_bot.respond(user_input)
    print("\nChat Bot:", response)
