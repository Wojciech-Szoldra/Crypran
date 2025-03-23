import secrets
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

def on_generate():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError("Długość musi być większa od 0.")
    except ValueError as ve:
        messagebox.showerror("Błąd", f"Niepoprawna wartość długości: {ve}")
        return
    pwd = generate_password(length)
    entry_password.delete(0, tk.END)
    entry_password.insert(0, pwd)

app = tk.Tk()
app.title("ysnp (you_shall_not_pass)")
app.geometry("350x150")
app.resizable(False, False)

label_length = tk.Label(app, text="Długość hasła:")
label_length.pack(pady=5)

entry_length = tk.Entry(app)
entry_length.insert(0, "12")
entry_length.pack(pady=5)

btn_generate = tk.Button(app, text="Generuj hasło", command=on_generate)
btn_generate.pack(pady=10)

entry_password = tk.Entry(app, width=40)
entry_password.pack(pady=5)

app.mainloop()