#include <cstdlib> // Necesario para 'system'
#include <iostream>

int
    std::cout << "Iniciando interfaz gráfica..." << std::endl;
    
    int status = system("python3 Log.py");

    if (status == 0) {
        std::cout << "El programa finalizó correctamente." << std::endl;
    } else {
        std::cout << "Ocurrió un error al ejecutar el script." << std::endl;
    }

    return 0;
}
