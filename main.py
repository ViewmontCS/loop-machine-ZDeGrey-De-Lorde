import random
import time
import os

print("Welcome to Zaben's definitely NOT rigged Slot Machine!")
print("you have 100 starting credits")
credits = 100
slots = [[1,2,3], [4,5,6], [7,8,9]]
payouts = [5, 25, 50, 45, 56, 50, 100, 43, 67]
top_row_mod = 1
mid_row_mod = 3
bot_row_mod = 5

def clear():
    os.system('cls')

def spin_slots():
    return [[random.randint(1, 9) for _ in range(3)] for _ in range(3)]

def calculate_payout(slots):
    payout = 0
    for row in slots:
        if row[0] == row[1] == row[2]:
            payout += payouts[row[0] - 1]
    if slots[0][0] == slots[1][1] == slots[2][2]:
        payout += payouts[slots[0][0] - 1]
    if slots[0][2] == slots[1][1] == slots[2][0]:
        payout += payouts[slots[0][2] - 1]
    return payout

def print_grid(grid):
    for row in grid:
        print("|".join(str(num) for num in row))

def animate_and_spin(final_delay=0.12, frames=28):
    for i in range(frames):
        frame = spin_slots()
        clear()
        print("Spinning...")
        print_grid(frame)
        t = i / max(1, frames - 1)
    final = spin_slots()
    clear()
    print_grid(final)
    return final
while True:
    input("Press Enter to spin the slots.")
    slots = animate_and_spin()
    payout = calculate_payout(slots)
    if payout > 0:
        print(f"Congratulations! You won {payout} credits!")
        credits += payout
        print(f"You now have {credits} credits.")
        again = input("Press Enter to begin again.").strip().lower()
    else:
        print("You gained nothing and lost 10 credits.")
        credits -= 10
        print(f"You now have {credits} credits.")
        if credits <= 0:
            print("You're out of credits. Game over.")
            break
