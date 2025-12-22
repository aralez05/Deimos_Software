import sqlite3

def crear_base_datos():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL UNIQUE,
            contrasena TEXT NOT NULL
        )
    ''')
    
    try:
        cursor.execute("INSERT INTO usuarios (usuario, contrasena) VALUES (?, ?)", ("admin", "1234"))
        print("Usuario 'admin' creado exitosamente.")
    except sqlite3.IntegrityError:
        print("El usuario 'admin' ya existe.")
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    crear_base_datos()
