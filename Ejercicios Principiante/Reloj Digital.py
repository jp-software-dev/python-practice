import tkinter as tk
from time import strftime

def actualizar_hora():
    cadena_hora = strftime('%H:%M:%S %p')
    etiqueta.config(text = cadena_hora)
    etiqueta.after(1000, actualizar_hora)

ventana = tk.Tk()
ventana.title("Reloj Digital")
ventana.geometry("450x150")
ventana.configure(bg="#0f0f0f")
ventana.resizable(False, False)

etiqueta = tk.Label (
    ventana,
    font = ('consolas', 50, 'bold'), 
    background='#0f0f0f', 
    foreground="#ffffff"
)

etiqueta.pack(anchor='center', expand=True)
actualizar_hora()
ventana.mainloop()