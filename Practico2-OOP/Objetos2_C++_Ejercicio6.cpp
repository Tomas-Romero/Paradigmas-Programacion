#include <iostream>
#include <string>

using namespace std;

class Celular {
private:
    string nombre; // Nombre del modelo del celular
    string marca;  // Marca del celular
    double precio; // Precio del celular

public:
    // Constructor
    Celular() : nombre(""), marca(""), precio(0.0) {}

    // Constructor con parámetros
    Celular(string nombre, string marca, double precio)
        : nombre(nombre), marca(marca), precio(precio) {}

    // Métodos getters
    string getNombre() const {
        return nombre;
    }

    string getMarca() const {
        return marca;
    }

    double getPrecio() const {
        return precio;
    }

    // Método para mostrar información del celular
    void mostrarInformacion() const {
        cout << "Modelo: " << nombre << ", Marca: " << marca << ", Precio: $" << precio << "\n";
    }
};

int main() {
    // Array de celulares disponibles en la tienda
    Celular tienda[6] = {
        Celular("Galaxy S21", "Samsung", 799.99),
        Celular("iPhone 12", "Apple", 999.99),
        Celular("Pixel 5", "Google", 699.99),
        Celular("Xperia 5", "Sony", 749.99),
        Celular("Mi 11", "Xiaomi", 599.99),
        Celular("P40 Pro", "Huawei", 649.99)
    };

    double presupuesto;
    cout << "Ingrese la cantidad de dinero que dispone: $";
    cin >> presupuesto;

    cout << "\nModelos disponibles dentro de su presupuesto:\n";
    bool modeloDisponible = false;
    for (int i = 0; i < 6; ++i) {
        if (tienda[i].getPrecio() <= presupuesto) {
            tienda[i].mostrarInformacion();
            modeloDisponible = true;
        }
    }

    if (!modeloDisponible) {
        cout << "No hay modelos disponibles dentro de su presupuesto.\n";
    }

    return 0;
}
