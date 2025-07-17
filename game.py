import random

# Global scores
USER_SCORE = 0
COMP_SCORE = 0

def choice_to_number(choice):
    return {'scissor': 0, 'paper': 1, 'rock': 2}[choice]

def number_to_choice(number):
    return {0: 'scissor', 1: 'paper', 2: 'rock'}[number]

def random_computer_choice():
    return random.choice(['scissor', 'paper', 'rock'])

def result(user_choice, comp_choice):
    global USER_SCORE, COMP_SCORE
    user = choice_to_number(user_choice)
    comp = choice_to_number(comp_choice)

    print(f"\nYou chose      : {user_choice}")
    print(f"Computer chose : {comp_choice}")

    if user == comp:
        print("Result         : It's a Tie!")
    elif (user - comp) % 3 == 1:
        print("Result         : You Win!")
        USER_SCORE += 1
    else:
        print("Result         : Computer Wins!")
        COMP_SCORE += 1

    print(f"\nYour Score     : {USER_SCORE}")
    print(f"Computer Score : {COMP_SCORE}")
    print("-" * 30)

def main():
    print("Welcome to Rock-Paper-Scissors Game by Diwas!")
    print("Type rock, paper, or scissor to play. Type exit to quit.\n")

    while True:
        user_choice = input("Enter your choice (rock/paper/scissor): ").strip().lower()
        if user_choice == "exit":
            print("\nThanks for playing!")
            break
        elif user_choice not in ['rock', 'paper', 'scissor']:
            print("Invalid input. Try again.\n")
            continue

        comp_choice = random_computer_choice()
        result(user_choice, comp_choice)

if __name__ == "__main__":
    main()
