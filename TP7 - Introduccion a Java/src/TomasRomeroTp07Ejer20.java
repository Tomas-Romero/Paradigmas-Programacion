import java.util.Scanner;
import java.util.Arrays;

//Estudiante Tomas Romero
//Trabajo Practico N°7 - Ejercicio N°20
public class TomasRomeroTp07Ejer20 {
    public static void main(String[] args) {
        // Ejercicio 1: Suma de números del 0 al 499
        int suma = 0; // Variable para la suma
        int i = 0; // Inicializamos el contador para el bucle while
        while (i < 500) { // Condición del bucle
            suma = suma + i; // Sumamos el valor de i
            System.out.println(suma + " " + i); // Mostramos la suma y el índice
            i++; // Incrementamos el contador
        }

        // Ejercicio 2: Contar sillas ocupadas en un arreglo
        int[] arraySillas = {1, 0, 1, 1, 0, 0, 1}; // Ejemplo de arreglo de sillas (1 = ocupada, 0 = libre)
        int sillas = 0; // Variable para contar sillas ocupadas
        int j = 0; // Inicializamos el contador para el bucle while
        while (j < arraySillas.length) { // Condición del bucle
            if (arraySillas[j] == 1) { // Verificamos si la silla está ocupada
                sillas = sillas + 1; // Contamos la silla ocupada
            }
            j++; // Incrementamos el contador
        }
        System.out.println("Número de sillas ocupadas: " + sillas); // Mostramos el total de sillas ocupadas
    }
}
