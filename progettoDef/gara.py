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

        global statoTelaioPosteriore
        global statoMotore
        global alaNuova

        alaNuova = 4
        statoTelaioPosteriore = 100
        statoMotore = 150

        for secondo in range(1, 10):
            numeroTelaioAnteriore = random.randint(1, 100)
            numeroTelaioPosteriore = random.randint(1, 100)
            numeroMotore = random.randint(1, 5)

            if numeroTelaioAnteriore <= 2:
                self.log_text.insert(tk.END, "Il pilota sostituisce l'ala anteriore\n")
                alaNuova -= 1
                self.log_text.insert(tk.END, f"Il numero di ali nuove rimaste è {alaNuova}\n\n")

            if alaNuova == 0:
                self.log_text.insert(tk.END, "Hai finito i ricambi!! Gara terminata\n\n")
                return

            if numeroTelaioPosteriore <= 1:
                self.log_text.insert(tk.END, "Gara finita! Telaio posteriore rotto\n\n")
                statoTelaioPosteriore= 0
                return

            elif 5 < numeroTelaioPosteriore <= 15:
                statoTelaioPosteriore -= 5
                self.log_text.insert(tk.END, f"Il telaio posteriore è al {statoTelaioPosteriore}\n\n")

            if statoTelaioPosteriore == 0:
                self.log_text.insert(tk.END, "Il telaio è rotto! Gara finita\n\n")
                statoTelaioPosteriore= 0
                return

            statoMotore -= numeroMotore

            if statoMotore <= 5:
                self.log_text.insert(tk.END, "Motore rotto, gara finita\n\n")
                statoMotore=0

                return

            else:
                self.log_text.insert(tk.END, f"Il motore è al {statoMotore}%\n")

            self.log_text.insert(tk.END, f"Il telaio posteriore è al {statoTelaioPosteriore}%")
            self.log_text.insert(tk.END, f"\nIl numero di ali rimanenti è {alaNuova}\n\n")
            self.log_text.insert(tk.END, f"La gara è al {secondo}%\n")
            self.log_text.update()
            time.sleep(1)
            self.log_text.delete(1.0, tk.END)

        self.log_text.insert(tk.END, "La gara è stata completata senza problemi.\n\n")
        self.log_text.insert(tk.END, f"Stato telaio posteriore: {statoTelaioPosteriore}\n")
        self.log_text.insert(tk.END, f"Stato motore: {statoMotore}\n")






root = tk.Tk()
app = GaraGUI(root)





