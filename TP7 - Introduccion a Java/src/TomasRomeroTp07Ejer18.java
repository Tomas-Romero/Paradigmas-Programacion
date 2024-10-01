import java.util.Scanner;

//Estudiante Tomas Romero
//Trabajo Practico N°7 - Ejercicio N°18
public class TomasRomeroTp07Ejer18 {
    public static void main(String[] args) {
        // Definimos una matriz de 10x10
        int[][] matriz = new int[10][10];

        // Variable para guardar la suma de los elementos de la diagonal
        int sumaDiagonal = 0;

        // Recorremos la matriz
        for (int i = 0; i < 10; i++) { // Recorremos las filas
            for (int j = 0; j < 10; j++) { // Recorremos las columnas
                // Verificamos si estamos en la diagonal principal
                if (i == j) {
                    // Asignamos el número i a la diagonal
                    matriz[i][j] = i;
                    // Sumamos el valor a la suma de la diagonal
                    sumaDiagonal += matriz[i][j];
                } else {
                    // En el resto de la matriz ponemos ceros (ya está por defecto)
                    matriz[i][j] = 0;
                }
            }
        }

        // Mostramos la matriz
        System.out.println("Matriz 10x10:");
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                System.out.print(matriz[i][j] + "\t"); // Imprimimos cada elemento con tabulación
            }
            System.out.println(); // Salto de línea después de cada fila
        }

        // Mostramos la suma de los elementos de la diagonal
        System.out.println("La suma de los elementos de la diagonal es: " + sumaDiagonal);
    }
}