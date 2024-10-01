import java.util.Scanner;
import java.util.Random;
import java.util.Arrays;

//Estudiante Tomas Romero
//Trabajo Practico N°7 - Ejercicio N°16
public class TomasRomeroTp07Ejer16 {
    public static void main(String[] args) {
        int[] numeros = new int[20]; // Creamos un arreglo de 20 elementos

        // Llenamos el arreglo con 0s y 1s de manera aleatoria
        Random random = new Random();
        for (int i = 0; i < numeros.length; i++) {
            numeros[i] = random.nextInt(2); // Generamos 0 o 1 aleatoriamente
        }

        // Mostramos el arreglo original
        System.out.println("Arreglo original: " + Arrays.toString(numeros));

        // Llamamos al metodo para ordenar el arreglo
        ordenarCerosYUnos(numeros);

        // Mostramos el arreglo ordenado
        System.out.println("Arreglo ordenado: " + Arrays.toString(numeros));
    }

    // Metodo para ordenar el arreglo, poniendo ceros a la izquierda y unos a la derecha
    public static void ordenarCerosYUnos(int[] arreglo) {
        int contadorCeros = 0; // Contador para los ceros

        // Contamos la cantidad de ceros en el arreglo
        for (int numero : arreglo) {
            if (numero == 0) {
                contadorCeros++;
            }
        }

        // Llenamos el arreglo con ceros
        for (int i = 0; i < contadorCeros; i++) {
            arreglo[i] = 0; // Asignamos ceros a las primeras posiciones
        }

        // Llenamos el resto del arreglo con unos
        for (int i = contadorCeros; i < arreglo.length; i++) {
            arreglo[i] = 1; // Asignamos unos a las posiciones restantes
        }
    }
}