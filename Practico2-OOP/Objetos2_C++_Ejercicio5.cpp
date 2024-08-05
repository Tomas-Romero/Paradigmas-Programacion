#include <iostream>
#include <string>

using namespace std;

class Empleado {
	private:
	    string nombre;
	    double horasTrabajadas;
	    double tarifaPorHora;

	public:
	    // Constructor por defecto
	    Empleado() : nombre(""), horasTrabajadas(0.0), tarifaPorHora(0.0) {}
	
	    // Constructor con parámetros
	    Empleado(string nombre, double horas, double tarifa)
	        : nombre(nombre), horasTrabajadas(horas), tarifaPorHora(tarifa) {}
	
	    // Métodos getters
	    string getNombre() const {
	        return nombre;
	    }
	
	    double getHorasTrabajadas() const {
	        return horasTrabajadas;
	    }
	
	    double getTarifaPorHora() const {
	        return tarifaPorHora;
	    }
	
	    // Métodos setters
	    void setNombre(string nombre) {
	        this->nombre = nombre;
	    }
	
	    void setHorasTrabajadas(double horas) {
	        horasTrabajadas = horas;
	    }
	
	    void setTarifaPorHora(double tarifa) {
	        tarifaPorHora = tarifa;
	    }
	
	    // Método para calcular el salario
	    double calcularSalario() const {
	        return horasTrabajadas * tarifaPorHora;
	    }
	
	    // Método para mostrar información del empleado
	    void mostrarInformacion() const {
	        cout << "Nombre: " << nombre << endl;
	        cout << "Horas trabajadas: " << horasTrabajadas << endl;
	        cout << "Tarifa por hora: $" << tarifaPorHora << endl;
	        cout << "Salario: $" << calcularSalario() << endl;
	    }
};

int main() {
    // Crear una instancia de Empleado
    Empleado empleado1("Juan Pérez", 40, 15.5);

    // Mostrar información del empleado
    empleado1.mostrarInformacion();

    // Cambiar las horas trabajadas y recalcular el salario
    empleado1.setHorasTrabajadas(45);
    cout << "\nActualización de horas trabajadas: "<<endl;
    empleado1.mostrarInformacion();

    return 0;
}
