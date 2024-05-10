import tkinter as tk
from tkinter import messagebox


def controlla_credenziali():
    username = username_entry.get()
    password = password_entry.get()

    # Verifica delle credenziali
    if username == "gara" and password == "gara":
        import gara
        gara.GaraGUI

    if username == "reparti" and password == "reparti":
        messagebox.showinfo("Accesso consentito", "Accesso effettuato con successo!")

    else:
        messagebox.showerror("Accesso negato", "Credenziali non valide.")

# Creazione della finestra principale
root = tk.Tk()
root.title("Gestione Credenziali di Accesso")

# Creazione dei widget
label_username = tk.Label(root, text="Username:")
label_password = tk.Label(root, text="Password:")
username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")

# Posizionamento dei widget
label_username.grid(row=0, column=0)
label_password.grid(row=1, column=0)
username_entry.grid(row=0, column=1)
password_entry.grid(row=1, column=1)

# Pulsante per il controllo delle credenziali
login_button = tk.Button(root, text="Accedi", command=controlla_credenziali)
login_button.grid(row=2, columnspan=2)

# Esecuzione del loop principale
root.mainloop()
