import random

def play_rps():
    print("\n--- Stone, Paper, Scissors ---")
    print("1. Stone")
    print("2. Paper")
    print("3. Scissors")
    
    user_input = input("Enter your choice (1-3): ")
    
    if user_input == '1':
        user_choice = "stone"
    elif user_input == '2':
        user_choice = "paper"
    elif user_input == '3':
        user_choice = "scissors"
    else:
        print("Invalid choice. Please try again.")
        return
        
    computer_input = random.randint(1, 3)
    if computer_input == 1:
        computer_choice = "stone"
    elif computer_input == 2:
        computer_choice = "paper"
    else:
        computer_choice = "scissors"
    
    print("\nYou chose: " + user_choice)
    print("Computer chose: " + computer_choice)
    
    if user_choice == computer_choice:
        print("Result: It's a tie!")
    elif user_choice == 'stone' and computer_choice == 'scissors':
        print("Result: You win!")
    elif user_choice == 'paper' and computer_choice == 'stone':
        print("Result: You win!")
    elif user_choice == 'scissors' and computer_choice == 'paper':
        print("Result: You win!")
    else:
        print("Result: Computer wins!")
