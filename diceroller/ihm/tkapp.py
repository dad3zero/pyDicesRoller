import tkinter as tk
from diceroller import roller

window = tk.Tk()


def rolle_dices():
    print(f"dices rolled {roller.roll_dice(dices_var.get(), sides_var.get())}")


form_frame = tk.Frame(window)

dices_var = tk.IntVar()
sides_var = tk.IntVar()

tk.Label(form_frame, text="Dices").grid(column=0, row=0)
tk.Label(form_frame, text="Sides").grid(column=0, row=1)
tk.Scale(form_frame, from_=1, to=10, variable=dices_var,
         orient="horizontal").grid(column=1, row=0)
tk.Spinbox(form_frame, values=(4, 6, 8, 10, 12, 20, 30, 100),
           textvariable=sides_var, state="readonly").grid(column=1, row=1)

form_frame.pack()
tk.Button(window, text="Roll", command=rolle_dices).pack()
tk.Button(window, text="Close", command=window.quit).pack()

window.mainloop()
