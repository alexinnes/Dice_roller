import random
import tkinter as tk
import pdb

class Dice:
    def __init__(self, number_of_dice, sides):
        self.sides = sides
        self.number_of_dice = number_of_dice

    def roll_dice(self):
        dice_list = []
        i = self.number_of_dice
        while i > 0:
            dices = {'dice': i, 'dice_roll':random.randint(1,self.sides)}
            dice_list.append(dices)
            i-=1
        return dice_list


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.no_dice_input_label = tk.Label(self)
        self.no_dice_input_label["text"]= "Number of Dice"
        self.no_dice_input_label.pack(side="top")
        self.no_dice_input = tk.Entry(self)
        self.no_dice_input.pack(side="top")

        self.no_sides_input_label = tk.Label(self)
        self.no_sides_input_label["text"]= "Number of Sides"

        self.no_sides_input_label.pack(side="top")
        self.no_sides_input = tk.Entry(self)
        self.no_sides_input.pack(side="top")

        self.dicebutton = tk.Button(self)
        self.dicebutton["text"] = "Roll"
        self.dicebutton["command"] = self.roll_button
        self.dicebutton.pack(side="top")

    def roll_button(self):
        dice_input = int(self.no_dice_input.get())
        sides_input = int(self.no_sides_input.get())
        '''pdb.set_trace()'''
        dice = Dice(dice_input,sides_input)
        roll = dice.roll_dice()
        for x in roll:
            self.dice_output = tk.Label(self)
            self.dice_output.pack(side="bottom", expand=1)
            self.dice_output["text"] = "dice:{} Value:{}".format(x["dice"], x["dice_roll"])
        self.dicebutton["text"] = "Re-Roll"


root = tk.Tk()
app = Application(master=root)
app.mainloop()








