#include <iostream>
#include <string>
using namespace std;

//Crea la clase para vehiculos
class Vehiculo {
private:
    string marca;
    string modelo;
    int anio;
    string color;

public:
    // Constructor por defecto
    Vehiculo() : marca(""), modelo(""), anio(0), color("") {};

    // Constructor con parámetros
    Vehiculo(string marcaIngresada, string modeloIngresado, int anioIngresado, string colorIngresado): marca(marcaIngresada), modelo(modeloIngresado), anio(anioIngresado), color(colorIngresado) {};

    // Getters
    string getMarca(){
        return marca;
    }

    string getModelo(){
        return modelo;
    }

    int getAnio(){
        return anio;
    }

    string getColor(){
        return color;
    }

    // Setters
    void setMarca(string marcaIngresado) {
        marca = marcaIngresado;
    }

    void setModelo(string modeloIngresado) {
        modelo = modeloIngresado;
    }

    void setAnio(int anioIngresado) {
        anio = anioIngresado;
    }

    void setColor(string colorIngresado) {
        color = colorIngresado;
    }

    // Método para mostrar información del vehículo
    void mostrarInfo(){
        cout << "Marca: " << marca << ", Modelo: " << modelo
             << ", Año: " << anio << ", Color: " << color << endl;
    }
};

// Función para ingresar los datos de un vehículo
Vehiculo ingresarVehiculo() {
    string marca;
	string modelo;
	string color;
    int anio;

    cout << "Ingrese la marca del vehículo: "<<endl;
    cin >> marca;
    cout << "Ingrese el modelo del vehículo: "<<endl;
    cin >> modelo;
    cout << "Ingrese el año del vehículo: "<<endl;
    cin >> anio;
    cout << "Ingrese el color del vehículo: "<<endl;
    cin >> color;

    return Vehiculo(marca, modelo, anio, color);
}

int main() {
    const int MAX_AUTOS = 10;
    Vehiculo autosFavoritos[MAX_AUTOS];
    Vehiculo autosOdiados[MAX_AUTOS];
    int cantidadFavoritos, cantidadOdiados;

    cout << "Ingrese la cantidad de autos favoritos a registrar (máximo " << MAX_AUTOS << "): ";
    cin >> cantidadFavoritos;
    //Condicionamos que si ingresan un numero mayor al maximo de la lista permitida, se cancele el ingresado y sea el maximo permitido
    if (cantidadFavoritos > MAX_AUTOS) {
		cantidadFavoritos = MAX_AUTOS;
	}
	//Se crean n cantidad de autos con la funcion de ingresar vehiculos y se agregan a la lista de autos favoritos
    for (int i = 0; i < cantidadFavoritos; ++i) {
        cout << "Ingrese los datos del auto favorito #" << i + 1 << ":" << endl;
        autosFavoritos[i] = ingresarVehiculo();
    }

    cout << "Ingrese la cantidad de autos odiados a registrar (máximo " << MAX_AUTOS << "): ";
    cin >> cantidadOdiados;
    //Condicionamos que la cantidad de autos odiados no sea mayor al permitido y lo seteamos distinto si lo ingresan mal
    if (cantidadOdiados > MAX_AUTOS) {
	cantidadOdiados = MAX_AUTOS;
	}
	//Se crean n cantidad de autos con la funcion de ingresar vehiculos y se agregan a la lista de autos odiados
    for (int i = 0; i < cantidadOdiados; ++i) {
        cout << "Ingrese los datos del auto odiado #" << i + 1 << ": " << endl;
        autosOdiados[i] = ingresarVehiculo();
    }
	//Se imprimen por cada elemento de los autos favoritos la informacion con el metodo del objeto
    cout << "\nAutos favoritos registrados:" << endl;
    for (int i = 0; i < cantidadFavoritos; ++i) {
        autosFavoritos[i].mostrarInfo();
    }
	//Se imprimen por cada elemento de los autos odiados la informacion con el metodo del objeto
    cout << "\nAutos odiados registrados:" << endl;
    for (int i = 0; i < cantidadOdiados; ++i) {
        autosOdiados[i].mostrarInfo();
    }

    return 0;
}
