import rps
import dice

while True:
    print("\n------------------------------")
    print("        MAIN MENU")
    print("------------------------------")
    print("1. Play Stone-Paper-Scissors")
    print("2. Play Dice Roll Game")
    print("3. Exit")
    print("------------------------------")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == '1':
        rps.play_rps()
    elif choice == '2':
        dice.play_dice()
    elif choice == '3':
        print("Thanks for playing! Goodbye.")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
