def actualizar_fondo(event):
    
    canvas=event.widget
    ancho = event.width
    alto = event.height
    
   
    canvas.delete("gradient")
    
   
    for i in range(alto):
        
        ratio = i / alto
        
      
        r = int(173 + (70 - 173) * ratio)
        g = int(216 + (130 - 216) * ratio)
        b = int(230 + (180 - 230) * ratio)
        color = f"#{r:02x}{g:02x}{b:02x}"
        
    
        canvas.create_line(0, i, ancho, i, fill=color, tags="gradient")


import tkinter as tk

def crear_menu_lateral(ventana_actual):
    sidebar = tk.Frame(ventana_actual, bg="#2c3e50")
    sidebar.place(x=0, y=0, relheight=1, width=150)
    
    # Importamos aquí para evitar errores de referencia circular
    import Menu
    import Configurar

    # Funciones de navegación
    def ir_a_menu():
        ventana_actual.destroy()
        Menu.main()
        
    def ir_a_configurar():
        ventana_actual.destroy()
        Configurar.main()

    
    tk.Button(sidebar, text="Inicio", bg="#34495e", fg="white", relief="flat", 
              command=ir_a_menu).pack(fill=tk.X, pady=10, padx=10)
              
    tk.Button(sidebar, text="Configuración", bg="#34495e", fg="white", relief="flat", 
              command=ir_a_configurar).pack(fill=tk.X, pady=10, padx=10)
              
    tk.Button(sidebar, text="Salir", bg="#c0392b", fg="white", relief="flat", 
              command=ventana_actual.destroy).pack(side=tk.BOTTOM, fill=tk.X, pady=10, padx=10)
