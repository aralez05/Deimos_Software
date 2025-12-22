import tkinter as tk

import Configurar


def main():
    ventana_menu = tk.Tk()
    ventana_menu.title("Menú Principal - Deimos")
    ventana_menu.geometry("500x400")

    
    label = tk.Label(ventana_menu, text="¡Bienvenido al sistema!", font=("Arial", 20))
    label.pack(pady=50)

    # Usamos la nueva función del Utils
    from Utils import crear_menu_lateral
    crear_menu_lateral(ventana_menu)
    
    ventana_menu.mainloop()

if __name__ == "__main__":
    main()
