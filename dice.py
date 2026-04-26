import random

def play_dice():
    print("\n--- Dice Roll Game ---")
    print("Rolling the dice...")
    
    user_roll = random.randint(1, 6)
    computer_roll = random.randint(1, 6)
    
    print(f"\nYou rolled: {user_roll}")
    print(f"Computer rolled: {computer_roll}")
    
    if user_roll > computer_roll:
        print("Result: You win!")
    elif user_roll < computer_roll:
        print("Result: Computer wins!")
    else:
        print("Result: It's a tie!")
