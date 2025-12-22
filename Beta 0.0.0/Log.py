import tkinter as tk
from Utils import actualizar_fondo


ventana = tk.Tk()
ventana.title("Deimos")
ventana.geometry("400x300")
Usario= tk.StringVar()
Contrasena= tk.StringVar()
UsuarioLb=tk.Label(ventana, text="Usuario:")
UsuarioLb.pack()
UsuarioEntry=tk.Entry(ventana, textvariable=Usario)
UsuarioEntry.pack()
ContrasenaLb=tk.Label(ventana, text="Contrasena:")
ContrasenaLb.pack()
ContrasenaEntry=tk.Entry(ventana, textvariable=Contrasena, show="*")
ContrasenaEntry.pack()
import Menu # Importamos el archivo destino
import sqlite3
from tkinter import messagebox

def verificar_login():
    usuario = Usario.get()
    contrasena = Contrasena.get()
    
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM usuarios WHERE usuario=? AND contrasena=?", (usuario, contrasena))
    usuario_encontrado = cursor.fetchone()
    
    conn.close()
    
    if usuario_encontrado:
        ventana.destroy()
        Menu.main()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

Inicio=tk.Button(ventana,text="ingresar", command=verificar_login)
Inicio.pack()
# Creamos el canvas
canvas = tk.Canvas(ventana, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Vinculamos el evento <Configure> (cambio de tamaño) a nuestra función
canvas.bind("<Configure>", actualizar_fondo)

ventana.mainloop()