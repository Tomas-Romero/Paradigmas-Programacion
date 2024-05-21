#include <iostream>
#include <cstdio>
#include <string>
#include <cstdlib>
#include <ctime>
#define PI 3.1416
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
	double num1, num2;
    
    cout << "Ingrese el primer número: ";
    cin >> num1;
    
    cout << "Ingrese el segundo número: ";
    cin >> num2;
    
    double suma6 = num1 + num2;
    double multiplicacion6 = num1 * num2;
    
    cout << "La suma de los números es: " << suma6 <<endl;
    cout << "La multiplicación de los números es: " << multiplicacion6 <<endl;
    
	cout<<"Ejercicio 7"<<endl;
	
	double valor_dolar, monto_dolares;
    
    cout << "Ingrese el valor del dólar hoy: ";
    cin >> valor_dolar;
    
    cout << "Ingrese el monto en dólares: ";
    cin >> monto_dolares;
    
    double monto_pesos = valor_dolar * monto_dolares;
    cout << "El monto en pesos es: " << monto_pesos <<endl;
    
    cout<<"Ejercicio 8"<<endl;
    double radio, altura;
    
    cout << "Ingrese el radio del cono: ";
    cin >> radio;
    
    cout << "Ingrese la altura del cono: ";
    cin >> altura;
    
    double volumen = (1.0/3.0) * PI * radio * radio * altura;
    
    cout << "El volumen del cono es: " << volumen <<endl;
    
    cout<<"Ejercicio 9"<<endl;
    double diametro;
    
    cout << "Ingrese el diámetro de la esfera: ";
    cin >> diametro;
    
    double radio = diametro / 2.0;
    
    double volumen = (4.0/3.0) * PI * radio * radio * radio;
    
    cout << "El volumen de la esfera es: " << volumen <<endl;
    
    cout<<"Ejercicio 10"<<endl;
    double lado;
    cout << "Ingrese la longitud de un lado del cubo: ";
    cin >> lado;
    
    double volumen = lado * lado * lado;
    cout<< "El volumen del cubo es: " << volumen <<endl;
    
    cout<<"Ejercicio 11"<<endl;
    double distancia;
    
    cout << "Ingrese la distancia en metros: ";
    cin >> distancia;
   
    double pulgadas = distancia * 39.37; // 1 metro = 39.37 pulgadas
    double pies = distancia * 3.281; // 1 metro = 3.281 pies
    double millas = distancia * 0.000621; // 1 metro = 0.000621 millas
    
    cout << "Distancia en pulgadas: " << pulgadas << endl;
    cout << "Distancia en pies: " << pies << endl;
    cout << "Distancia en millas: " << millas << endl;
    
    
    cout<<"Ejercicio 12"<<endl;
    string palabra;
    
    cout << "Ingrese una palabra: ";
    cin >> palabra;
    
    int longitud = palabra.length();
    cout << "La palabra tiene " << longitud << " caracteres." <<endl;
    
    
    cout<<"Ejercicio 13"<<endl;
    string palabra13;
    
    cout << "Ingrese una palabra (de al menos 5 letras): ";
    cin >> palabra13;
    
    char primera = palabra13[0];
    char tercera = palabra13[2];
    char cuarta = palabra13[3];
    
    cout << "Primera letra: " << primera <<endl;
    cout << "Tercera letra: " << tercera <<endl;
    cout << "Cuarta letra: " << cuarta <<endl;
    
    
    cout<<"Ejercicio 14"<<endl;
    string palabra14;
    
    cout << "Ingrese una palabra: ";
    cin >> palabra14;
    
    char primera14 = palabra14[0];
    char ultima14 = palabra14[palabra14.length() -1];
    
    cout << "Primera letra: " << primera14 <<endl;
    cout << "Ultima letra: " << ultima14 <<endl;
    
    
    cout<<"Ejercicio 15"<<endl;
    int numero15;
    cout << "Ingrese un número: ";
    cin >> numero15;

    if (numero15 > 0) {
        cout << "El número es positivo." <<endl;
    } else if (numero15 < 0) {
        cout << "El número es negativo." <<endl;
    } else {
        cout << "El número es cero." <<endl;
    }
    
    
    cout<<"Ejercicio 16"<<endl;
    double dividendo, divisor, resultado;

    cout << "Ingrese el dividendo: ";
    cin >> dividendo;

    cout << "Ingrese el divisor: ";
    cin >> divisor;

    if (divisor != 0) {
        resultado = dividendo / divisor;
        cout << "El resultado de la división es: " << resultado <<endl;
    } else {
        cout << "Error: no se puede dividir por cero." <<endl;
    }
    
    cout<<"Ejercicio 17"<<endl;
    int numero17;
    cout << "Ingrese un número: ";
    cin >> numero17;

    if (numero17 % 2 != 0) {
        cout << "El número es impar." <<endl;
    } else {
        cout << "El número es par." <<endl;
    }
    
    cout<<"Ejercicio 18"<<endl;
    void restaPositiva() {
	    int a, b;
	    cout << "Ingrese dos números: ";
	    cin >> a >> b;

	    int resta = b - a;
	    if (resta < 0) {
	        resta = -resta;
	    }
		
	    cout << "La resta es: " << resta << endl;
    restaPositiva();
    
    cout<<"Ejercicio 19"<<endl;
    cout<<"Ejercicio 20"<<endl;
    cout<<"Ejercicio 21"<<endl;
    cout<<"Ejercicio 22"<<endl;
    cout<<"Ejercicio 23"<<endl;
    
	return 0;
}