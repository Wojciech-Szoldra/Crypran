import secrets
import string
import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip

def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def on_generate():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError("Długość musi być większa od 0.")
    except ValueError as ve:
        messagebox.showerror("Błąd", f"Niepoprawna wartość długości: {ve}")
        return
    pwd = generate_password(length)
    entry_password.config(state=tk.NORMAL)
    entry_password.delete(0, tk.END)
    entry_password.insert(0, pwd)
    entry_password.config(state='readonly')
    pyperclip.copy(pwd)
    lbl_status.config(text="Hasło skopiowane!")

# Tworzenie okna aplikacji
app = tk.Tk()
app.title("Password Generator")
app.geometry("400x180")
app.resizable(False, False)

# Stylizacja
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5)
style.configure("TLabel", font=("Arial", 11))
style.configure("TEntry", font=("Arial", 11), padding=5)

# Układ interfejsu
frame = ttk.Frame(app, padding=20)
frame.grid(row=0, column=0, sticky="nsew")

# Etykieta i pole do wpisania długości
lbl_length = ttk.Label(frame, text="Długość hasła:")
lbl_length.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_length = ttk.Entry(frame, width=10)
entry_length.insert(0, "12")
entry_length.grid(row=0, column=1, padx=5, pady=5)

# Przycisk generowania
btn_generate = ttk.Button(frame, text="Generuj", command=on_generate)
btn_generate.grid(row=0, column=2, padx=10, pady=5)

# Pole wyświetlające hasło
entry_password = ttk.Entry(frame, width=32, state='readonly')
entry_password.grid(row=1, column=1, columnspan=3, padx=5, pady=10)

# Etykieta statusu
lbl_status = ttk.Label(frame, text="", foreground="green")
lbl_status.grid(row=2, column=0, columnspan=3, pady=5)

app.mainloop()