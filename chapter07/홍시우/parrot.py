message = input("Tell me something, and I will repeat it back to you: ")
print(message)

prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

age = input("How old are you?") # 18
age = int(age)

if age >= 18 :
    print("True")   # True가 출력된다!

prompt = input("\nTell me something, and I will repeat it back to you: ")
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)