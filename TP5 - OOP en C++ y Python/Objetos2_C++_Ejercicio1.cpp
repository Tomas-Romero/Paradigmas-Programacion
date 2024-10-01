#include <iostream>
#include <string>
using namespace std;


class Perro{
	private:
		string nombre_perro = "";
		int edad_perro = 0;
	public:
		//Constructor por defecto
		Perro(){}
		//Constructor con nombre
		Perro(string nombre): nombre_perro(nombre){};
		//Constructor por edad
		Perro(int edad): edad_perro(edad){};
		//Constructor por nombre y edad
		Perro(string nombre, int edad): nombre_perro(nombre), edad_perro(edad){};
		//Getters
		string getNombre(){
			return nombre_perro;
		}
		int getEdad(){
			return edad_perro;
		}
		//Metodos Setters
		void setNombre(string nuevo_nombre){
			this->nombre_perro = nuevo_nombre;
		}
		void setEdad(int nueva_edad){
			this->edad_perro = nueva_edad;
		}
		
};
int main(){
	
	Perro lista_perros[6];
	string nombre;
	int edad;
	//Bucle para cargar los 6 perros
	for (int i = 0; i<6;i++){
		cout << "Ingrese el nombre del perro "<< i+1 <<": ";
		cin >> nombre;
		cout << "ingrese la edad del perro "<< i+1 <<": ";
		cin >> edad;
		
		//Agregamos la instancia de perro a la lista con el indice para el objeto Perro
		lista_perros[i].setNombre(nombre);
		lista_perros[i].setEdad(edad);
	}
	
	//Vemos cual es el perro mas viejo
	Perro perroViejo = lista_perros[0];
	int sumaEdades = 0;
	for (int i = 0; i < 6; ++i){
		sumaEdades += lista_perros[i].getEdad();
		if (lista_perros[i].getEdad() > perroViejo.getEdad()){
			perroViejo = lista_perros[i];
		}
	}
	//Calculamos la edad promedio de los 6 perros
	float edadPromedio = sumaEdades / 6.0;
	
	//Imprimimos todos los resultados
	cout << "\nEl perro con mayor edad de todos es: "<<perroViejo.getNombre()<<"con"<<perroViejo.getEdad()<<" años de edad."<<endl;
	cout << "La edad promedio de los perros ingresados es: "<<edadPromedio<<"años."<<endl;
	
	
	return 0;
}