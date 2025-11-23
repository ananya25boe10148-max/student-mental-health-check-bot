 # ---------------------------------------------------------
# Student Mental Health Check Bot
# Simple version for first-semester students
# ---------------------------------------------------------

def greeting():
    print("Hello! I'm your Student Mental Health Check Bot.")
    print("I'm here to help you reflect on how you're feeling today.")
    print("Please remember: I'm not a professional, but I can offer support and guidance.")
    print("-" * 50)

def ask_feelings():
    print("\nHow are you feeling today?")
    print("1. Happy")
    print("2. Stressed")
    print("3. Sad")
    print("4. Anxious")
    print("5. Tired")

    choice = input("Choose a number (1–5): ")
    return choice

def respond(choice):
    if choice == "1":
        print("\nI'm glad to hear you're feeling good today. I hope the rest of your day stays positive.")
    
    elif choice == "2":
        print("\nIt's completely normal to feel stressed sometimes.")
        print("Try taking a small break or organizing your tasks into smaller steps. It might help.")

    elif choice == "3":
        print("\nI'm sorry that you're feeling sad.")
        print("Talking to someone you trust or writing down what you're feeling can bring some relief.")

    elif choice == "4":
        print("\nFeeling anxious can be overwhelming.")
        print("Try some slow, deep breathing or take a moment to focus on things around you.")

    elif choice == "5":
        print("\nIt sounds like you’re feeling tired.")
        print("If possible, take some rest, drink water, or relax your mind for a few minutes.")

    else:
        print("\nThat doesn't seem like a valid option, but it's okay. Let's continue.")

def offer_support():
    print("\nWould you like some simple tips to help you feel better?")
    ans = input("Type yes or no: ").lower()

    if ans == "yes":
        print("\nHere are a few suggestions that might help:")
        print("- Take short breaks while studying.")
        print("- Talk to someone you trust about how you're feeling.")
        print("- Try keeping a small to-do list.")
        print("- Make sure to rest when you need it.")
        print("- Ask for help whenever you feel overwhelmed.")
    else:
        print("\nNo problem. I'm here anytime you want to talk again.")

def main():
    greeting()
    choice = ask_feelings()
    respond(choice)
    offer_support()
    print("\nTake care of yourself. You're doing your best, and that matters.")

main()
