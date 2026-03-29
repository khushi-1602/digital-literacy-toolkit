Here is a Digital Literacy Toolkit.
This Digital Literacy Toolkit has a things that can help people.
We have Digital Literacy Toolkit that can teach people about phishing.
We have Digital Literacy Toolkit that can check password strength.
We have Digital Literacy Toolkit that can give people privacy tips.
To use the Digital Literacy Toolkit you have to follow these steps.
First you have to look at the menu for the Digital Literacy Toolkit.
The menu for the Digital Literacy Toolkit has an options.
* The first option is about phishing awareness.
* The second option is about password strength checker.
* The third option is about privacy tips.
* The fourth option is to exit the Digital Literacy Toolkit.
When you use the Digital Literacy Toolkit it will keep asking you what you want to do.
You have to enter the number of the option you want.
If you enter the number one the Digital Literacy Toolkit will teach you about phishing
awareness.
If you enter the number two the Digital Literacy Toolkit will check your password strength.
If you enter the number three the Digital Literacy Toolkit will give you privacy tips.
If you enter the number four the Digital Literacy Toolkit will say thank you and exit.
If you enter anything the Digital Literacy Toolkit will say that is not a valid choice.
Here is what the menu for the Digital Literacy Toolkit looks like.
The menu for the Digital Literacy Toolkit says
1. Phishing Awareness
2. Password Strength Checker
3. Privacy Tips
4. Exit
The Digital Literacy Toolkit is here to help people.
The Digital Literacy Toolkit wants people to stay online.
The Digital Literacy Toolkit has a symbol that's a lock it is .
From modules.phishing import phishing_awareness
from modules.passwords import password_checker
from modules.privacy import privacy_tips
def show_menu():
print("\n=== Digital Literacy Toolkit ===")
print("1. Phishing Awareness")
print("2. Password Strength Checker")
print("3. Privacy Tips")
print("4. Exit")
main():
while True:
show_menu()
choice = input("Enter your choice (1-4): ").strip()
if choice == "1":
phishing_awareness()
elif choice == "2":
password_checker()
elif choice == "3":
privacy_tips()
elif choice == "4":
print("Thank you for using the Digital Literacy Toolkit. Stay safe online! ")
break
else:
print("Invalid choice. Please try again.")
if __name__ == "__main__":
main()
