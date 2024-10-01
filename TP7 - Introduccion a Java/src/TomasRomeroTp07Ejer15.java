import java.util.Scanner;

//Estudiante Tomas Romero
//Trabajo Practico N°7 - Ejercicio N°15
public class TomasRomeroTp07Ejer15 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // Creamos el objeto Scanner
        String[] palabras = new String[6]; // Creamos un arreglo para almacenar 6 palabras

        // Pedimos al usuario que ingrese 6 palabras
        System.out.println("Por favor, ingresa 6 palabras:");

        for (int i = 0; i < 6; i++) {
            System.out.print("Palabra " + (i + 1) + ": ");
            palabras[i] = scanner.nextLine(); // Guardamos la palabra en el arreglo
        }

        // Pedimos al usuario que ingrese otra palabra para buscar
        System.out.print("Ingresa una palabra para verificar si existe en el vector: ");
        String palabraABuscar = scanner.nextLine(); // Leemos la palabra a buscar

        // Variable para saber si encontramos la palabra
        boolean encontrado = false;

        // Verificamos si la palabra existe en el arreglo
        for (String palabra : palabras) {
            if (palabra.equalsIgnoreCase(palabraABuscar)) { // Comparamos sin importar mayúsculas
                encontrado = true; // Marcamos como encontrado
                break; // Salimos del bucle
            }
        }

        // Mostramos el resultado
        if (encontrado) {
            System.out.println("La palabra '" + palabraABuscar + "' existe en el vector.");
        } else {
            System.out.println("La palabra '" + palabraABuscar + "' NO existe en el vector.");
        }

        scanner.close(); // Cerramos el Scanner
    }
}