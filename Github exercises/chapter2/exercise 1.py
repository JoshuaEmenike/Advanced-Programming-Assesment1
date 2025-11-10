import tkinter as tk
root=tk.Tk()
root.geometry("500x300")
root.resizable(False,False)
root.configure(bg="lightblue")
label=tk.Label(root,text="welcome", font=("Arial",16,"bold"))
label.pack()

root.mainloop()