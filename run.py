import tkinter as tk
from tkinter import ttk
from BetaBuilder import *
from compData import compData

def deleta(text_area):
    text_area.delete("1.0", "end")

def show_text(text_area, text):
    text_area.insert(tk.INSERT, text)

root = tk.Tk()
root.title("BetaBuilder AI")
root.geometry("1000x700")


label = tk.Label(root, text = "Try-hardity")
label2 = tk.Label(root, text = "Variation")
slider = tk.Scale(root, from_=100, to_=300, orient="horizontal")
countSlide = tk.Scale(root, from_=100, to_=300, orient="horizontal")
drop = ttk.Combobox(root, values=[dataSet.get("xname") for dataSet in compData])
drop.pack()
label.pack()
slider.pack()
label2.pack()
countSlide.pack()
build = tk.Button(root, text="BUILD!", command=lambda: show_text(text, getTeam(drop.get(), slider, countSlide)))
clear = tk.Button(root, text="CLEAR", command=lambda: deleta(text))
text = tk.Text(root)
build.pack()
clear.pack()
text.pack()



root.mainloop()