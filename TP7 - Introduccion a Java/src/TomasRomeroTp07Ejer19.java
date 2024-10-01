import java.util.Scanner;
import java.util.Random;

//Estudiante Tomas Romero
//Trabajo Practico N°7 - Ejercicio N°19
public class TomasRomeroTp07Ejer19 {
    public static void main(String[] args) {
        // Definimos una matriz de 6x6
        int[][] matriz = new int[6][6];
        Random random = new Random(); // Para generar números aleatorios

        // Llenamos la matriz con números aleatorios del 1 al 100
        for (int i = 0; i < 6; i++) { // Recorremos las filas
            for (int j = 0; j < 6; j++) { // Recorremos las columnas
                matriz[i][j] = random.nextInt(100) + 1; // Generamos números del 1 al 100
            }
        }

        // Variable para la suma de las filas pares y contador
        int sumaFilasPares = 0;
        int contador = 0;

        // Recorremos la matriz para calcular el promedio de las filas pares
        for (int i = 0; i < 6; i++) { // Recorremos las filas
            if (i % 2 == 0) { // Verificamos si la fila es par
                for (int j = 0; j < 6; j++) { // Recorremos las columnas
                    sumaFilasPares += matriz[i][j]; // Sumamos los elementos de la fila
                }
                contador++; // Aumentamos el contador de filas pares
            }
        }

        // Calculamos el promedio
        double promedio = (double) sumaFilasPares / (contador * 6); // Promedio de filas pares

        // Mostramos la matriz
        System.out.println("Matriz 6x6:");
        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 6; j++) {
                System.out.print(matriz[i][j] + "\t"); // Imprimimos cada elemento con tabulación
            }
            System.out.println(); // Salto de línea después de cada fila
        }

        // Mostramos el promedio de las filas pares
        System.out.println("El promedio de los números de las filas pares es: " + promedio);
    }
}