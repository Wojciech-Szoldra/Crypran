import secrets
import string
import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip
from PIL import Image, ImageTk

# Generowanie hasła
def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for i in range(length))

# Widoczność hasła
def toggle_password_visibility():
    if entry_password.cget('show') == '•':
        entry_password.config(show='')
        btn_toggle.config(text='👁')
    else:
        entry_password.config(show='•')
        btn_toggle.config(text='🔒')

# Kliknięcie przycisku 'Generuj'
def on_generate():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError("Długość musi być większa od 0.")
        elif length > 50:
            raise ValueError("Długość nie może być większa niż 50.")
    except ValueError as ve:
        messagebox.showerror("Błąd", f"Niepoprawna wartość długości: {ve}")
        return
    pwd = generate_password(length)
    entry_password.config(state='NORMAL',show='•')
    entry_password.delete(0, tk.END)
    entry_password.insert(0, pwd)
    entry_password.config(state='readonly')
    btn_toggle.config(text='🔒')
    pyperclip.copy(pwd)
    lbl_status.config(text="Hasło skopiowane!")

# Tworzenie okna aplikacji
app = tk.Tk()
app.title("Crypran")
app.geometry("390x200")
app.resizable(False, False)

# Stylizacja
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5)
style.configure("TLabel", font=("Arial", 11))
style.configure("TEntry", font=("Arial", 11), padding=5)

# Tworzenie ramki
frame = ttk.Frame(app, padding=20)
frame.grid(row=0, column=0, sticky="nsew")

# Etykieta i pole do wpisania długości
lbl_length = ttk.Label(frame, text="Długość:")
lbl_length.grid(row=0, column=0, padx=5, pady=8, sticky='ew')
entry_length = ttk.Entry(frame, width=12)
entry_length.insert(0, "12")
entry_length.grid(row=0, column=1, padx=10, pady=8, sticky='ew')

# Przycisk generowania
btn_generate = ttk.Button(frame, text="Generuj", width=21, command=on_generate)
btn_generate.grid(row=1, column=1, padx=10, pady=8, sticky='e')

# Pole wyświetlające hasło
lbl_password = ttk.Label(frame, text="Hasło:")
lbl_password.grid(row=2, column=0, padx=5, pady=8, sticky="w")
entry_password = ttk.Entry(frame, state='readonly', show='•')
entry_password.grid(row=2, column=1, padx=10, pady=8, sticky='ew')

# Przycisk do podglądu hasła
btn_toggle = ttk.Button(frame, text='🔒', width=2, command=toggle_password_visibility)
btn_toggle.grid(row=2, column=2, padx=5, pady=8, sticky='e')

# Etykieta statusu
lbl_status = ttk.Label(frame, text="", foreground="green")
lbl_status.grid(row=3, column=0, columnspan=3)

# Ikona aplikacji
icon = ImageTk.PhotoImage(Image.open("C:/ścieżka/do/pliku/ikona.png"))
app.wm_iconphoto(True, icon)

# Uruchomienie pętli zdarzeń
app.mainloop()