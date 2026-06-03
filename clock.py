import tkinter as tk
from datetime import datetime as dat
ty=tk.Tk()
i=False
tlp=tk.Label(
    ty,
    font=("Arial",80,"bold"),
    bg="black",
    fg="cyan",
)
tlp.pack()
ttp=tk.Label(
    ty,
    font=("Arial",40,"bold"),
    bg="black",
    fg="white",
)
tllp=tk.Label(
    ty,
    font=("Arial",40,"bold"),
    bg="black",
    fg="green",
)
tllp.pack()
ttp.pack()
ty.title("Digital Clock")
ty.geometry("2000x400")
ty.configure(bg="black")
def ho():
    global i
    i = not i
def update():
    if i:
        ope=dat.now().strftime("%H:%M:%S")
        tlp.config(text=ope)
    else:
        opeo=dat.now().strftime("%I:%M:%S %p")
        tlp.config(text=opeo)
    oppp=dat.now().strftime("%d:%B:%Y")
    ttp.config(text=oppp)
    opo=dat.now().strftime("%A")
    tllp.config(text=opo)
    ty.after(1000,update)
ko=tk.Label(
    ty,
    font=("Arial",40,"bold"),
    bg="black",
    text="Press the button to change clock format",
    fg="cyan",
)
ko.pack()
btn=tk.Button(ty,text="12hr clock / 24 hr clock",command=ho)
btn.pack()
update()
ty.mainloop()
