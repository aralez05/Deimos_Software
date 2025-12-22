import tkinter as tk
from Utils import actualizar_fondo

def main():
    ventana = tk.Tk()
    ventana.title("Deimos - Configuración")
    ventana.geometry("400x300")
    
    label = tk.Label(ventana, text="¡Configuración!", font=("Arial", 20))
    label.pack(pady=50)
    
    # Creamos el canvas
    canvas = tk.Canvas(ventana, highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    # Vinculamos el evento <Configure> (cambio de tamaño) a nuestra función
    canvas.bind("<Configure>", actualizar_fondo)

    # Agregamos la barra lateral
    from Utils import crear_menu_lateral
    crear_menu_lateral(ventana)

    ventana.mainloop()

if __name__ == "__main__":
    main()
