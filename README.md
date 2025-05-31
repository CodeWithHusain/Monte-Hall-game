# Monte-Hall-game
📜 Game Rules:
There are 3 cups.

One cup contains a reward (the other two are empty).

The player picks one cup.

The host reveals an empty cup from the remaining two (never showing the reward).

The player is given the choice to swap or stay with their original cup.

The cup is opened and the outcome (win/loss) is displayed.

The game repeats until the player chooses to stop.

Stats for swaps and wins are shown at the end.

🧠 Monty Hall Strategy Insight:
Swapping gives you a 2/3 chance to win.

Staying gives you only a 1/3 chance.

Over many plays, you'll see swapping wins far more often!

🚀 How to Run
Make sure you have Python 3 installed.

Save the script in a file, e.g. monty_hall.py

Run the script from terminal or your IDE:

bash
Copy
Edit
python monty_hall.py
🧾 Example Gameplay
pgsql
Copy
Edit
Cups are shuffled! (3 cups total)
Which cup do you choose? (0/1/2): 0

Host reveals an empty cup at position 2.

Do you want to swap your choice? (y/n): y
🎉 You won the reward by swapping!
(Reward was in cup #1)

Do you want to play again? (y/n): n

🎯 Game Over!
Total swaps: 1, Wins by swapping: 1
Total non-swaps: 0, Wins without swapping: 0
🛠 Features
Interactive gameplay via terminal

Randomized reward position

Host always shows an empty cup

Tracks total number of:

Swaps

Non-swaps

Wins from each strategy

📌 Want to Simulate Automatically?
You can modify the code to run the game 1000 times without user input to statistically prove the Monty Hall theory. Let me know if you want help with that version!

📚 License
This project is free to use and modify for educational purposes.
