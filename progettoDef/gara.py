import tkinter as tk
from tkinter import scrolledtext
import random
import time

class GaraGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Stato della Gara")

        self.log_text = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=50, height=20)
        self.log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.gara_durata()

    def gara_durata(self):
        statoTelaioPosteriore = 100
        statoMotore = 350
        alaNuova = 4
        for secondo in range(1, 101):
            numeroTelaioAnteriore = random.randint(1, 100)
            numeroTelaioPosteriore = random.randint(1, 100)
            numeroMotore = random.randint(1, 5)

            if numeroTelaioAnteriore <= 2:
                self.log_text.insert(tk.END, "Il pilota sostituisce l'ala anteriore\n")
                alaNuova -= 1
                self.log_text.insert(tk.END, f"Il numero di ali nuove rimaste è {alaNuova}\n\n")

            if alaNuova == 0:
                self.log_text.insert(tk.END, "Hai finito i ricambi!! Gara terminata\n\n")
                break

            if numeroTelaioPosteriore <= 1:
                self.log_text.insert(tk.END, "Gara finita! Telaio posteriore rotto\n\n")
                break

            elif 5 < numeroTelaioPosteriore <= 15:
                statoTelaioPosteriore -= 5
                self.log_text.insert(tk.END, f"Il telaio posteriore è al {statoTelaioPosteriore}\n\n")

            if statoTelaioPosteriore == 0:
                self.log_text.insert(tk.END, "Il telaio è rotto! Gara finita\n\n")
                break

            statoMotore -= numeroMotore

            if statoMotore <= 5:
                self.log_text.insert(tk.END, "Motore rotto, gara finita\n\n")
                break

            else:
                self.log_text.insert(tk.END, f"\nIl motore è al {statoMotore}%\n")

            self.log_text.insert(tk.END, f"il telaio è al {statoTelaioPosteriore}%\n\n")
            self.log_text.insert(tk.END, f"La gara è al {secondo}%\n")
            self.log_text.update()
            time.sleep(1)
            self.log_text.delete(1.0, tk.END)
        else:
            self.log_text.insert(tk.END, "La gara è stata completata senza problemi.\n\n")
            self.log_text.insert(tk.END, f"Stato telaio posteriore: {statoTelaioPosteriore}\n")
            self.log_text.insert(tk.END, f"Stato motore: {statoMotore}\n")


root = tk.Tk()
app = GaraGUI(root)