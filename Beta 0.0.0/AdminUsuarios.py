import sqlite3

def conectar():
    return sqlite3.connect("users.db")

def agregar_usuario():
    print("\n--- AGREGAR USUARIO ---")
    usuario = input("Nombre de usuario: ")
    contrasena = input("Contraseña: ")
    
    conn = conectar()
    try:
        conn.execute("INSERT INTO usuarios (usuario, contrasena) VALUES (?, ?)", (usuario, contrasena))
        conn.commit()
        print(f"¡Usuario '{usuario}' agregado exitosamente!")
    except sqlite3.IntegrityError:
        print(f"Error: El usuario '{usuario}' ya existe.")
    conn.close()

def ver_usuarios():
    print("\n--- LISTA DE USUARIOS ---")
    conn = conectar()
    cursor = conn.execute("SELECT id, usuario, contrasena FROM usuarios")
    for flia in cursor:
        print(f"ID: {flia[0]} | Usuario: {flia[1]} | Clave: {flia[2]}")
    conn.close()

def borrar_usuario():
    print("\n--- BORRAR USUARIO ---")
    usuario = input("Nombre de usuario a borrar: ")
    
    conn = conectar()
    cursor = conn.execute("DELETE FROM usuarios WHERE usuario = ?", (usuario,))
    conn.commit()
    
    if cursor.rowcount > 0:
        print(f"Usuario '{usuario}' eliminado.")
    else:
        print(f"No se encontró al usuario '{usuario}'.")
    conn.close()

def menu():
    while True:
        print("\n=== GESTIÓN DE BASE DE DATOS ===")
        print("1. Agregar usuario")
        print("2. Ver todos los usuarios")
        print("3. Borrar usuario")
        print("4. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            agregar_usuario()
        elif opcion == "2":
            ver_usuarios()
        elif opcion == "3":
            borrar_usuario()
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
