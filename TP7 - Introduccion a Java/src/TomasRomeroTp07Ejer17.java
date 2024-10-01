import java.util.Scanner;

//Estudiante Tomas Romero
//Trabajo Practico N°7 - Ejercicio N°17
public class TomasRomeroTp07Ejer17 {
    public static void main(String[] args) {
        // Definimos la matriz cuadrada de 4x4
        int[][] matriz = {
                {9, 5, 0, -3},
                {7, -2, 8, 1},
                {3, 5, 7, 8},
                {6, 3, 0, -1}
        };

        // Variable para guardar la suma de los elementos
        int suma = 0;

        // Recorremos la matriz con dos bucles anidados
        for (int i = 0; i < 4; i++) { // Recorremos las filas
            for (int j = 0; j < 4; j++) { // Recorremos las columnas
                // Verificamos si estamos en la diagonal principal
                if (i != j) {
                    // Si no estamos en la diagonal principal, sumamos el elemento
                    suma += matriz[i][j];
                }
            }
        }

        // Mostramos el resultado
        System.out.println("La suma de los elementos que no están en la diagonal principal es: " + suma);
    }
}