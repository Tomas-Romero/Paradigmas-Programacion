import java.util.Random;
//Estudiante Tomas Romero
//Trabajo Practico N°7 - Ejercicio N°21

public class TomasRomeroTp07Ejer21 {
    public static void main(String[] args) {
        // Creamos una matriz de 20x20
        int[][] matriz = new int[20][20];
        Random random = new Random(); // Para generar números aleatorios

        // Llenamos la matriz con números aleatorios entre 0 y 100
        for (int i = 0; i < 20; i++) { // Recorremos las filas
            for (int j = 0; j < 20; j++) { // Recorremos las columnas
                matriz[i][j] = random.nextInt(101); // Generamos números del 0 al 100
            }
        }

        // Inicializamos el valor máximo con el primer elemento de la matriz
        int maximo = matriz[0][0];

        // Buscamos el valor máximo en la matriz
        for (int i = 0; i < 20; i++) { // Recorremos las filas
            for (int j = 0; j < 20; j++) { // Recorremos las columnas
                // Si encontramos un número mayor que el máximo actual, lo actualizamos
                if (matriz[i][j] > maximo) {
                    maximo = matriz[i][j]; // Actualizamos el máximo
                }
            }
        }

        // Mostramos la matriz
        System.out.println("Matriz 20x20:");
        for (int i = 0; i < 20; i++) {
            for (int j = 0; j < 20; j++) {
                System.out.print(matriz[i][j] + "\t"); // Imprimimos cada elemento con tabulación
            }
            System.out.println(); // Salto de línea después de cada fila
        }

        // Mostramos el valor máximo encontrado
        System.out.println("El valor máximo de la matriz es: " + maximo);
    }
}
