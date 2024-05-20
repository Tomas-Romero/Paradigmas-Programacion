#include <iostream>
#include <cstdio>
#include <string>
using namespace std;
int main(){
	string bienvenida = "Hola Pepe, tanto tiempo!";
	cout << "Ejercicio 1" << endl;
	cout << bienvenida << endl;
	cout << "Ejercicio 2" << endl;
	cout << "2.a- Resultado: "<< 3+5*(74-2) << endl;
	cout << "Se resuelve de izquierda a derecha separando los terminos por los + y - y priorizando los parentesis." << endl;
	cout << "2.b - No es lo mismo, ya que tendra distinta prioridad los operadores, aqui la diferencia: " << endl;
	cout << "Primera forma: " << 2*10+5 << endl;
	cout << "Segunda forma: " << 2*(10+5) << endl;
	double div_decimal = 5/2;
	cout << "2.c - Se puede ver que por mas que se declare la variable como un numero decimal, si ninguno de los numeros donde se realizan la operacion es dle tipo decimal de trunca el resultado, es decir que no se redondea, simplemente se elimina todos los datos luego de la coma del numero entero. Resultado: " << div_decimal << endl;
	cout << "2.d - Resultado: " << 5.0/2 << endl;
	cout << "2.e - Resultado: " << 5.0/2.0 << endl;
	cout << "2.f - Resultado: " << 5 + "helou" << endl;
	cout << 5 << "helou" << endl;
	cout << "Se puede observar que no se puede hacer el procedimiento con datos como numeros y luego texto, solo se podria 'concatenar' de la forma de imprimir primero uno y luego otro."<< endl;
	string hola = "Hola";
	string pepito = "Pepito";
	cout << "2.g - Resultado: " << hola + pepito << endl;
	cout << hola + "Pepito" <<endl;
	cout << "No se puede hacer operaciones con el texto en si dentro de una variable o para tirar el resultado automaticamente, pero si se puede asignar esos textos a variables y hacer la concatenacion de ambas variables o tambien agregarle a la variable texto posteriormente." << endl;
	cout << "Ejercicio 3"<<endl;
	int numero1_ej3 = 24;
	int numero2_ej3 = 786;
	int suma = numero1_ej3 + numero2_ej3;
	cout << "La suma resultante es: "<<suma<<endl;
	cout<<"Ejercicio 4"<<endl;
	cout<<"Tamaño de int: "<<sizeof(int)<<endl;
	cout<<"Tamaño de double: "<<sizeof(double)<<endl;
	cout<<"Tamaño de char: "<<sizeof(char)<<endl;
	cout<<"Tamaño de string: "<<sizeof(string)<<endl;
	cout<<"Tamaño de bool: "<<sizeof(bool)<<endl;
	cout <<"Ejercicio 5"<<endl;
	int a = 5;
	int b = 10;
	cout<<"Valores iniciales a y b: "<<a<<" y "<<b<<endl;
	int copia;
	copia = a;
	a = b;
	b = copia;
	cout<<"Valores finales a y b: "<<a<<" y "<<b<<endl;
	cout<<"Ingreso de Datos por el Usuario"<<endl;
	cout<<"Ejercicio 6"<<endl;
	
	return 0;
}