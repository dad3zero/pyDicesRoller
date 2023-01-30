import tkinter as tk
from diceroller import roller


class DicesForm(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self._dices_var = tk.IntVar()
        self._sides_var = tk.IntVar()

        tk.Label(self, text="Dices").grid(column=0, row=0)
        tk.Label(self, text="Sides").grid(column=0, row=1)
        tk.Scale(self, from_=1, to=10, variable=self._dices_var,
                 orient="horizontal").grid(column=1, row=0)
        tk.Spinbox(self, values=(4, 6, 8, 10, 12, 20, 30, 100),
                   textvariable=self._sides_var, state="readonly").grid(column=1, row=1)

    def get_values(self):
        """
        Get the selected values

        :return: a tuple of the number of dices and sides per dice
        """
        return self._dices_var.get(), self._sides_var.get()


def roll_dices():
    print(f"dices rolled {roller.roll_dice(*form_frame.get_values())}")

window = tk.Tk()

form_frame = DicesForm(window)

form_frame.pack()
tk.Button(window, text="Roll", command=roll_dices).pack()
tk.Button(window, text="Close", command=window.quit).pack()

window.mainloop()
