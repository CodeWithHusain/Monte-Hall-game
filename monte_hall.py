''''
psudo code
1.write the satring variable of the code 
2.assume one cup = price
3.jumble the cups/ variables
4.take input to choose one cups 
5.after choosing ask for swap or not swap
6.first show the user an empty cups then ask the user for swap or not swap 
7. if the user swap then show the user diffrent cups else show the user that cups that it have choosen 
8.then calculate the number of swap and non-swap  
9.show the final results 

'''
import random

# Initialize counters
swap = 0
non_swap = 0
swap_wins = 0
non_swap_wins = 0

while True:
    # Step 1: Setup cups
    cups = [0, 0, 0]
    reward_index = random.randint(0, 2)
    cups[reward_index] = "reward"

    print("\nCups are shuffled! (3 cups total)")

    # Step 2: User makes a choice
    user_choice = int(input("Which cup do you choose? (0/1/2): "))

    # Step 3: Host reveals an empty cup (not user's choice, not reward)
    possible_empty = []
    for i in range(3):
        if i != user_choice and cups[i] != "reward":
            possible_empty.append(i)

    shown_empty = random.choice(possible_empty)
    print(f"\nHost reveals an empty cup at position {shown_empty}.")

    # Step 4: Ask the user if they want to swap
    swap_input = input("Do you want to swap your choice? (y/n): ").strip().lower()

    # Step 5: Determine final choice and track results
    if swap_input == "y":
        swap += 1
        # Swap to the only cup that's not user_choice or shown_empty
        for i in range(3):
            if i != user_choice and i != shown_empty:
                final_choice = i
                break
        if final_choice == reward_index:
            print("🎉 You won the reward by swapping!")
            swap_wins += 1
        else:
            print("😢 You got an empty cup by swapping.")
    else:
        non_swap += 1
        final_choice = user_choice
        if final_choice == reward_index:
            print("🎉 You won the reward by staying!")
            non_swap_wins += 1
        else:
            print("😢 You got an empty cup by staying.")

    print(f"(Reward was in cup #{reward_index})")

    # Step 6: Ask to play again
    play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
    if play_again != "y":
        break

# Step 7: Show final statistics
print("\n🎯 Game Over!")
print(f"Total swaps: {swap}, Wins by swapping: {swap_wins}")
print(f"Total non-swaps: {non_swap}, Wins without swapping: {non_swap_wins}")
