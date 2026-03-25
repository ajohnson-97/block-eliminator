#!/usr/bin/env python3

# Start by clicking the button with the lowest number & clicking the next lowest number until all the buttons have been clicked. 
# Try to finish the game in the shortest amount of time possible.

# Written by Anthony Johnson
# https://github.com/ajohnson-97

import random
import tkinter as tk
from tkinter import messagebox


def main():
    # Initialize variables
    random_int_list = []
    start_time = True
    time = 0
    count_disabled_buttons = 0

    # Instantiate window object
    window = tk.Tk()
    window.title("Block Eliminator")

    def random_int_generator():
        random_int = random.randint(1, 999)
        while random_int in random_int_list:
            random_int = random.randint(1, 999)

        random_int_list.append(random_int)
        return random_int

    def click(event):
        nonlocal start_time, count_disabled_buttons

        if start_time:
            start_time = False
            increment_time()

        button = event.widget.cget("text")

        if button == random_int_list[0]:
            event.widget.config(state="disabled")
            count_disabled_buttons += 1
            random_int_list.pop(0)

    def increment_time():
        nonlocal time

        time += 1
        timer_id = row5_col0.after(1000, increment_time)
        row5_col0.config(text=time)

        if count_disabled_buttons == 25:
            row5_col0.after_cancel(timer_id)
            messagebox.showinfo(
                "Game Finished",
                f"Congratulations!\nYou finished the game in {time} seconds."
            )

    # Create buttons (same as before)
    buttons = []
    for r in range(5):
        row = []
        for c in range(5):
            btn = tk.Button(text=random_int_generator(), width=10)
            btn.grid(row=r, column=c)
            row.append(btn)
        buttons.append(row)

    # Timer label
    row5_col0 = tk.Label(text=time, width=65)
    row5_col0.grid(row=5, column=0, columnspan=5)

    window.bind_all("<Button-1>", click)

    random_int_list.sort()

    window.mainloop()


if __name__ == "__main__":
    main()
