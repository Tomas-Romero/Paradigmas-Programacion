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
    
	void adivinaNumero() {
	    srand(time(0));
	    int secreto = rand() % 5 + 1;
	    int intento;
	
	    cout << "Adivina el número secreto (entre 1 y 5): ";
	    cin >> intento;
	
	    if (intento == secreto) {
	        cout << "¡Adivinaste!" << endl;
	    } else {
	        cout << "¡Incorrecto! El número secreto era " << secreto << "." << endl;
	        if (intento < secreto) {
	            cout << "El número secreto era mayor." << endl;
	        } else {
	            cout << "El número secreto era menor." << endl;
	        }
	    }
	}
	adivinaNumero();
	
	
    cout<<"Ejercicio 20"<<endl;
    
    double nota_betty, nota_vilma;
    cout << "Ingrese la nota de Vilma: ";
    cin >> nota_vilma;

    cout << "Ingrese la nota de Betty: ";
    cin >> nota_betty;

    if (nota_betty >= 2 * nota_vilma) {
        cout << "Betty esta feliz." << endl;
    } else {
        cout << "Betty no esta feliz." << endl;
    }
    
    cout<<"Ejercicio 21"<<endl;
    
    int determinarMayor(int num1, int num2) {
	    if (num1 > num2) {
	        return num1;
	    } else {
	        return num2;
	    }
	}
	int numero1;
	int numero2;
	cout << "Ingrese el numero 1 para ver si es mayor: " <<endl;
	cin >> numero1;
	
	cout << "Ingrese el numero 2 para ver si es mayor al anterior ingresado: " << endl;
	cin >> numero2;
	
    determinarMayor(numero1, numero2);
    
    
    cout<<"Ejercicio 22"<<endl;
    
    char determinarNota(int porcentaje) {
	    if (porcentaje >= 90) {
	        return 'A';
	    } else if (porcentaje >= 80) {
	        return 'B';
	    } else if (porcentaje >= 70) {
	        return 'C';
	    } else if (porcentaje >= 60) {
	        return 'D';
	    } else {
	        return 'F';
	    }
	}
	
	int porcentaje;
    cout << "ingrese la nota en valor de porcentaje para ver la nota final: " << endl;
    cin >> porcentaje;
    cout << "La nota correspondiente es: " << determinarNota(porcentaje) << endl;
    
    
    cout<<"Ejercicio 23"<<endl;
    
	return 0;
}
//23

#include <iostream>

using namespace std;

bool esUnistico(int a, int b) {
    return (a + b + a * b) == 111;
}

int main() {
    
    int pares[4][2] = {
        {1, 55},
        {55, 1},
        {7, 13},
        {7, 14}
    };

    for (int i = 0; i < 4; ++i) {
        int a = pares[i][0];
        int b = pares[i][1];
        if (esUnistico(a, b)) {
            cout << "El par (" << a << ", " << b << ") es Unístico." << endl;
        } else {
            cout << "El par (" << a << ", " << b << ") no es Unístico." << endl;
        }
    }

    return 0;
}

//24

#include <iostream>
using namespace std;

void mostrarSecuencia(int n) {
    for (int i = 1; i <= n; ++i) {
        cout << i << endl;
    }
}

int main() {
    int n;
    cout << "Ingrese un número: ";
    cin >> n;
    mostrarSecuencia(n);
    return 0;
}

//25

#include <iostream>
using namespace std;

void sumaNumeros() {
    int numero, suma = 0;
    cout << "Ingrese números (0 para terminar): ";
    cin >> numero;
    while (numero != 0) {
        suma += numero;
        cin >> numero;
    }
    cout << "La suma es: " << suma << endl;
}

int main() {
    sumaNumeros();
    return 0;
}

//26

#include <iostream>
#include <string>
using namespace std;

void mostrarLetras(string frase) {
    for (char letra : frase) {
        if (letra != ' ') {
            cout << letra << endl;
        }
    }
}

int main() {
    string frase;
    cout << "Ingrese una frase: ";
    getline(cin, frase);
    mostrarLetras(frase);
    return 0;
}


//27

#include <iostream>
#include <string>
using namespace std;

void letrasPosicionesPares(string palabra) {
    for (int i = 0; i < palabra.length(); i += 2) {
        cout << palabra[i] << endl;
    }
}

int main() {
    string palabra;
    cout << "Ingrese una palabra: ";
    cin >> palabra;
    letrasPosicionesPares(palabra);
    return 0;
}

//28

#include <iostream>
#include <vector>
using namespace std;

int productoVector(const vector<int>& vec) {
    int producto = 1;
    for (int num : vec) {
        producto *= num;
    }
    return producto;
}

int main() {
    vector<int> numeros = {1, 2, 3, 4, 5, 6, 7, 8};
    int producto = productoVector(numeros);
    cout << "El producto de los números en el vector es: " << producto << endl;
    return 0;
}

//29

#include <iostream>
#include <vector>
using namespace std;

double productoEscalar(const vector<double>& vec1, const vector<double>& vec2) {
    double producto = 0;
    for (int i = 0; i < vec1.size(); ++i) {
        producto += vec1[i] * vec2[i];
    }
    return producto;
}

int main() {
    vector<double> vec1 = {1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.1};
    vector<double> vec2 = {10.1, 9.9, 8.8, 7.7, 6.6, 5.5, 4.4, 3.3, 2.2, 1.1};
    double producto = productoEscalar(vec1, vec2);
    cout << "El producto escalar de los vectores es: " << producto << endl;
    return 0;
}

//30

#include <iostream>
#include <vector>
#include <cstdlib> 
#include <ctime> 

using namespace std;

int numeroAleatorio(int min, int max) {
    return min + rand() % (max - min + 1);
}


    vector<int> valores(25);
    
    srand(time(0));

    
    for (int i = 0; i < 25; ++i) {
        valores[i] = numeroAleatorio(1, 100);
    }

    
    cout << "Primer valor: " << valores.front() << endl;
    cout << "Valor del medio: " << valores[valores.size() / 2] << endl;
    cout << "Último valor: " << valores.back() << endl;


//31

    int matriz[6][8];
    int sumaDiagonal = 0;

    
    for (int i = 0; i < 6; ++i) {
        for (int j = 0; j < 8; ++j) {
            matriz[i][j] = numeroAleatorio(1, 100);
            
            if (i == j) {
                sumaDiagonal += matriz[i][j];
            }
        }
    }
    return sumaDiagonal;
}

//32
vector<int> ejercicio32() {
    int matriz[8][12];
    vector<int> sumaFilas(8, 0);

    
    for (int i = 0; i < 8; ++i) {
        for (int j = 0; j < 12; ++j) {
            matriz[i][j] = numeroAleatorio(1, 100);
            sumaFilas[i] += matriz[i][j];
        }
    }
    return sumaFilas;
}

//33

void ejercicio33(string frase) {
    
    string palabra;
    vector<string> palabras;
    stringstream ss(frase);
    while (ss >> palabra) {
        palabras.push_back(palabra);
    }

    
    if (palabras.size() < 3) {
        cout << "La frase debe contener al menos 3 palabras." << endl;
        return;
    }

    string palabraDelMedio = palabras[palabras.size() / 2];
    int longitud = palabraDelMedio.length();

    cout << "Palabra del medio: " << palabraDelMedio << endl;
    cout << "Longitud: " << longitud << endl;
}

//34
void ejercicio34(string nombreCompleto) {
    size_t posicionEspacio = nombreCompleto.find(' ');
    if (posicionEspacio == string::npos) {
        cout << "Formato incorrecto. Debe ingresar nombre y apellido separados por un espacio." << endl;
        return;
    }

    string nombre = nombreCompleto.substr(0, posicionEspacio);
    string apellido = nombreCompleto.substr(posicionEspacio + 1);

    cout << apellido << ", " << nombre << endl;
}

int main() {
    ejercicio30();

    int sumaDiagonal = ejercicio31();
    cout << "Suma de los elementos de la diagonal: " << sumaDiagonal << endl;

    vector<int> sumaFilas = ejercicio32();
    cout << "Suma de los valores de cada fila:" << endl;
    for (int i = 0; i < sumaFilas.size(); ++i) {
        cout << "Fila " << i + 1 << ": " << sumaFilas[i] << endl;
    }

    string frase;
    cout << "Ingrese una frase: ";
    getline(cin, frase);
    ejercicio33(frase);

    string nombreCompleto;
    cout << "Ingrese nombre y apellido: ";
    getline(cin, nombreCompleto);
    ejercicio34(nombreCompleto);

    return 0;
}