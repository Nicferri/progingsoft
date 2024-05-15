import tkinter as tk


class post_race:

    from gara import statoTelaioPosteriore
    from gara import statoMotore
    from gara import alaNuova



    root = tk.Tk()
    root.title("situazione auto postgara")


    label_telaioPosteriore = tk.Label(root, text=f"stato telaio anteriore {statoTelaioPosteriore}%")
    label_motore = tk.Label(root, text=f"lo stato del motore è {statoMotore}%")
    label_alaNuova = tk.Label(root, text= f"il numero di ali rimaste è {alaNuova}")
    label_space1 = tk.Label(root, text= "           ")



    # Posizionamento dei widget
    label_telaioPosteriore.grid(row=0, column=0)
    label_motore.grid(row=2, column=0)
    label_alaNuova.grid(row=4, column= 0)
    label_space1.grid(row=4, column=3)
    label_space1.grid(row=5, column=3)


