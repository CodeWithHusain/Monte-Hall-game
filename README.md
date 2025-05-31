# 🎩 Monte Hall Game (Monty Hall Problem Simulator)

A fun simulation of the famous **Monty Hall Problem**, where your decision to **swap or not** determines your chance of winning a reward hidden under one of three cups.

---

## 📜 Game Rules

- There are **3 cups** — one contains a **reward**, the others are empty.
- The player picks **one** cup.
- The host then reveals **an empty cup** from the two remaining ones (never the reward).
- The player is asked: **Do you want to swap your cup?**
- The chosen cup is opened and the result is shown.
- The game repeats until the player chooses to stop.
- At the end, **statistics** show your results based on swap and non-swap choices.

---

## 🧠 Monty Hall Strategy Insight

- **Swapping** gives you a **2/3** chance to win.
- **Staying** gives you only a **1/3** chance.
- Over many rounds, **swapping wins far more often** — the simulation proves it!

---

## 🚀 How to Run

1. Make sure you have **Python 3** installed.
2. Save the script in a file (e.g. `monty_hall.py`)
3. Run the script from terminal or any Python IDE:

```bash
python monty_hall.py

Cups are shuffled! (3 cups total)
Which cup do you choose? (0/1/2): 0

Host reveals an empty cup at position 2.

Do you want to swap your choice? (y/n): y
🎉 You won the reward by swapping! (Reward was in cup #1)

Do you want to play again? (y/n): n

🎯 Game Over!
Total swaps: 1, Wins by swapping: 1
Total non-swaps: 0, Wins without swapping: 0



