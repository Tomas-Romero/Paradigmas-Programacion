//1

#include <iostream>
#include <string>

int main() {
    std::string mensaje = "Hola Pepe, tanto tiempo!";
    std::cout << mensaje << std::endl;
    return 0;
}

//2

#include <iostream>
#include <string>

using namespace std;

int main() {
    int resultado_a = 3 + 5 * (74 - 2);
    cout << "a) 3 + 5(74 - 2) = " << resultado_a << endl;

    int resultado_b1 = 2 * 10 + 5;
    int resultado_b2 = 2 * (10 + 5);
    cout << "b) 2 * 10 + 5 = " << resultado_b1 << endl;
    cout << "   2 * (10 + 5) = " << resultado_b2 << endl;

    int resultado_c = 5 / 2;
    cout << "c) 5/2 = " << resultado_c << endl;

    float resultado_d = 5.0 / 2;
    cout << "d) 5.0/2 = " << resultado_d << endl;

    float resultado_e = 5.0 / 2.0;
    cout << "e) 5.0/2.0 = " << resultado_e << endl;

    string resultado_g = "hola" + "Pepito";
    cout << "g) \"hola\" + \"Pepito\" = " << resultado_g << endl;

    return 0;
}

//3

#include <iostream>

int main() {
    int a = 24;
    int b = 786;
    int suma = a + b;
    std::cout << "La suma de " << a << " y " << b << " es: " << suma << std::endl;
    return 0;
}

//4

#include <iostream>

int main() {
    std::cout << "Tamaño de int: " << sizeof(int) << " bytes" << std::endl;
    std::cout << "Tamaño de float: " << sizeof(float) << " bytes" << std::endl;
    std::cout << "Tamaño de double: " << sizeof(double) << " bytes" << std::endl;
    std::cout << "Tamaño de char: " << sizeof(char) << " bytes" << std::endl;
    return 0;
}

//5

#include <iostream>

int main() {
    int a = 5;
    int b = 8;
    std::cout << "Valores iniciales: a = " << a << ", b = " << b << std::endl;
    
    int temp = a;
    a = b;
    b = temp;
    
    std::cout << "Valores intercambiados: a = " << a << ", b = " << b << std::endl;
    return 0;
}

//6

#include <iostream>

int main() {
    double num1, num2;
    
    std::cout << "Ingrese el primer número: ";
    std::cin >> num1;
    
    std::cout << "Ingrese el segundo número: ";
    std::cin >> num2;
    
    double suma = num1 + num2;
    double multiplicacion = num1 * num2;
    
    std::cout << "La suma de los números es: " << suma << std::endl;
    std::cout << "La multiplicación de los números es: " << multiplicacion << std::endl;
    
    return 0;
}

//7

#include <iostream>

int main() {
    double valor_dolar, monto_dolares;
    
    std::cout << "Ingrese el valor del dólar hoy: ";
    std::cin >> valor_dolar;
    
    std::cout << "Ingrese el monto en dólares: ";
    std::cin >> monto_dolares;
    
    double monto_pesos = valor_dolar * monto_dolares;
    
    std::cout << "El monto en pesos es: " << monto_pesos << std::endl;
    
    return 0;
}

//8

#include <iostream>
#define PI 3.1416

int main() {
    double radio, altura;
    
    cout << "Ingrese el radio del cono: ";
    cin >> radio;
    
    cout << "Ingrese la altura del cono: ";
    cin >> altura;
    
    double volumen = (1.0/3.0) * PI * radio * radio * altura;
    
    cout << "El volumen del cono es: " << volumen <<endl;
    
    return 0;
}

//9

#include <iostream>
#define PI 3.1416

int main() {
    double diametro;
    
    std::cout << "Ingrese el diámetro de la esfera: ";
    std::cin >> diametro;
    
    double radio = diametro / 2.0;
    
    double volumen = (4.0/3.0) * PI * radio * radio * radio;
    
    std::cout << "El volumen de la esfera es: " << volumen << std::endl;
    
    return 0;
}

//10

#include <iostream>

int main() {
    double lado;
    
    std::cout << "Ingrese la longitud de un lado del cubo: ";
    std::cin >> lado;
    
    double volumen = lado * lado * lado;
    
    std::cout << "El volumen del cubo es: " << volumen << std::endl;
    
    return 0;
}

//11

#include <iostream>

int main() {
    double distancia;
    
    std::cout << "Ingrese la distancia en metros: ";
    std::cin >> distancia;
   
    double pulgadas = distancia * 39.37; // 1 metro = 39.37 pulgadas
    double pies = distancia * 3.281; // 1 metro = 3.281 pies
    double millas = distancia * 0.000621; // 1 metro = 0.000621 millas
    
    std::cout << "Distancia en pulgadas: " << pulgadas << std::endl;
    std::cout << "Distancia en pies: " << pies << std::endl;
    std::cout << "Distancia en millas: " << millas << std::endl;
    
    return 0;
}

//12

#include <iostream>
#include <string>

int main() {
    std::string palabra;
    
    std::cout << "Ingrese una palabra: ";
    std::cin >> palabra;
    
    int longitud = palabra.length();
    
    std::cout << "La palabra tiene " << longitud << " caracteres." << std::endl;
    
    return 0;
}

//13

#include <iostream>
#include <string>

int main() {
    std::string palabra;
    
    std::cout << "Ingrese una palabra (de al menos 5 letras): ";
    std::cin >> palabra;
    
    char primera = palabra[0];
    char tercera = palabra[2];
    char cuarta = palabra[3];
    
    std::cout << "Primera letra: " << primera << std::endl;
    std::cout << "Tercera letra: " << tercera << std::endl;
    std::cout << "Cuarta letra: " << cuarta << std::endl;
    
    return 0;
}

//14

#include <iostream>
#include <string>

int main() {
    std::string palabra;
    
    std::cout << "Ingrese una palabra: ";
    std::cin >> palabra;
    
    char primera = palabra[0];
    char ultima = palabra[palabra.length() - 1];
    
    std::cout << "Primera letra: " << primera << std::endl;
    std::cout << "Última letra: " << ultima << std::endl;
    
    return 0;
}

//15

#include <iostream>

int main() {
    int numero;

    std::cout << "Ingrese un número: ";
    std::cin >> numero;

    if (numero > 0) {
        std::cout << "El número es positivo." << std::endl;
    } else if (numero < 0) {
        std::cout << "El número es negativo." << std::endl;
    } else {
        std::cout << "El número es cero." << std::endl;
    }

    return 0;
}

//16

#include <iostream>

int main() {
    double dividendo, divisor, resultado;

    std::cout << "Ingrese el dividendo: ";
    std::cin >> dividendo;

    std::cout << "Ingrese el divisor: ";
    std::cin >> divisor;

    if (divisor != 0) {
        resultado = dividendo / divisor;
        std::cout << "El resultado de la división es: " << resultado << std::endl;
    } else {
        std::cout << "Error: no se puede dividir por cero." << std::endl;
    }

    return 0;
}

//17
#include <iostream>

int main() {
    int numero;

    std::cout << "Ingrese un número: ";
    std::cin >> numero;

    if (numero % 2 != 0) {
        std::cout << "El número es impar." << std::endl;
    } else {
        std::cout << "El número es par." << std::endl;
    }

    return 0;
}

//18

#include <iostream>
using namespace std;

void restaPositiva() {
    int a, b;
    cout << "Ingrese dos números: ";
    cin >> a >> b;

    int resta = b - a;

    if (resta < 0) {
        resta = -resta;
    }

    cout << "La resta es: " << resta << endl;
}

int main() {
    restaPositiva();
    return 0;
}

//19

#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

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

int main() {
    adivinaNumero();
    return 0;
}

//20
#include <iostream>

using namespace std;

bool bettyFeliz(int notaBetty, int notaVilma) {
    return notaBetty >= 2 * notaVilma;
}

//21

int determinarMayor(int num1, int num2) {
    if (num1 > num2) {
        return num1;
    } else {
        return num2;
    }
}

//22

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

int main() {
    //20
    int notaBetty, notaVilma;
    cout << "Ingrese la nota de Betty: ";
    cin >> notaBetty;
    cout << "Ingrese la nota de Vilma: ";
    cin >> notaVilma;
    if (bettyFeliz(notaBetty, notaVilma)) {
        cout << "¡Betty está feliz!" << endl;
    } else {
        cout << "Betty no está feliz :(" << endl;
    }

    //21
    int num1, num2;
    cout << "Ingrese el primer número: ";
    cin >> num1;
    cout << "Ingrese el segundo número: ";
    cin >> num2;
    cout << "El número mayor es: " << determinarMayor(num1, num2) << endl;

    //22
    int porcentaje;
    cout << "Ingrese el porcentaje sacado en el examen: ";
    cin >> porcentaje;
    cout << "La nota correspondiente es: " << determinarNota(porcentaje) << endl;

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


