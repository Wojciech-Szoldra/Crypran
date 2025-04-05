import tkinter as tk
from tkinter import ttk

root = tk.Tk()
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10, fill="both", expand=True)

# Pole Entry wyśrodkowane (domyślnie)
entry1 = ttk.Entry(frame)
entry1.grid(row=0, column=0, padx=5, pady=5)

# Pole Entry przyklejone do lewej
entry2 = ttk.Entry(frame)
entry2.grid(row=1, column=0, padx=5, pady=5, sticky="w")

# Pole Entry przyklejone do prawej
entry3 = ttk.Entry(frame)
entry3.grid(row=2, column=0, padx=5, pady=5, sticky="e")

# Pole Entry rozciągnięte poziomo
entry4 = ttk.Entry(frame)
entry4.grid(row=3, column=0, padx=5, pady=5, sticky="we")

root.mainloop()