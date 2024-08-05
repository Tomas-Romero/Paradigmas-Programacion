#include <iostream>
#include <string>
using namespace std;

//Se crea la clase de Temperatura
class Temperatura {
	private:
	    double valor; // Valor de la temperatura
    	char unidad;  // Unidad de la temperatura: C para Celsius, F para Fahrenheit, K para Kelvin
	public:
	    // Constructor basico
	    Temperatura() : valor(0.0), unidad('C') {}
	
	    // Constructor con valor y unidad de medida
	    Temperatura(double valorIngresado, char unidadIngresado) : valor(valorIngresado), unidad(unidadIngresado) {}
	
	    // Método para establecer la temperatura y unidad
	    void setTemperatura(double valorIngresado, char unidadIngresado) {
	        valor = valorIngresado;
	        unidad = unidadIngresado;
	    }
	
	    // Método para obtener la temperatura en Celsius
	    double getCelsius() const {
	        if (unidad == 'C'){
				return valor;}
	        else if (unidad == 'F'){
				return (valor - 32) * 5.0 / 9.0;}
	        else if (unidad == 'K'){
				return valor - 273.15;}
	        else{ 
			return 0;} // Retorno para el caso no definido o mal ingresado
		}
	    // Método para obtener la temperatura en Fahrenheit
	    double getFahrenheit() const {
	        if (unidad == 'C'){
				return (valor * 9.0 / 5.0) + 32;}
	        else if (unidad == 'F'){
				return valor;}
	        else if (unidad == 'K'){
					return (valor - 273.15) * 9.0 / 5.0 + 32;}
	        else{ 
			return 0;}//Retorno para el caso no definido
		}
	    // Método para obtener la temperatura en Kelvin
	    double getKelvin() const {
	        if (unidad == 'C'){
				return valor + 273.15;}
	        else if (unidad == 'F'){
				return (valor - 32) * 5.0 / 9.0 + 273.15;}
	        else if (unidad == 'K'){
				return valor;}
	        else{ 
				return 0;} // Caso no definido
	    }
	
	    // Método para obtener la unidad actual
	    char getUnidad() const {
	        return unidad;
	    }
	
	    // Método para imprimir la temperatura en la unidad por defecto
	    void imprimir() const {
	        if (unidad == 'C'){
				cout << valor << " °C"<<endl;}
	        else if (unidad == 'F'){
				cout << valor << " °F"<<endl;}
	        else if (unidad == 'K'){
				cout << valor << " K"<<endl;}
	    }
};

int main() {
    // Se crea una instancia de temperatura
    Temperatura temp1(25.0, 'C');
    cout << "Temperatura en Celsius: " << temp1.getCelsius() << " °C"<<endl;
    cout << "Temperatura en Fahrenheit: " << temp1.getFahrenheit() << " °F"<<endl;
    cout << "Temperatura en Kelvin: " << temp1.getKelvin() << " K"<<endl;

    //se cambia la temperatura a otras unidades
    temp1.setTemperatura(77.0, 'F');
    cout << "Nueva temperatura establecida."<<endl;
    cout << "Temperatura en Celsius: " << temp1.getCelsius() << " °C"<<endl;
    cout << "Temperatura en Fahrenheit: " << temp1.getFahrenheit() << " °F"<<endl;
    cout << "Temperatura en Kelvin: " << temp1.getKelvin() << " K"<<endl;

    return 0;
}
