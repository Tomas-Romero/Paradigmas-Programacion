import java.util.Scanner;
//Estudiante Tomas Romero
//Trabajo Practico N°7 - Ejercicio N°9
public class TomasRomeroTp07Ejer09 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // Creamos un objeto Scanner para leer la entrada

        // Pedimos al usuario que ingrese una palabra
        System.out.print("Ingresa una palabra: ");
        String palabra = scanner.nextLine(); // Leemos la palabra ingresada

        // Pedimos al usuario que ingrese una letra
        System.out.print("Ingresa una letra a reemplazar: ");
        String letra = scanner.nextLine(); // Leemos la letra ingresada

        // Verificamos que el usuario haya ingresado solo una letra
        if (letra.length() != 1) {
            System.out.println("Debes ingresar solo una letra."); // Mensaje de error
        } else {
            // Reemplazamos las ocurrencias de la letra por el símbolo de numeral
            String resultado = palabra.replace(letra.charAt(0), '#'); // Reemplazamos la letra por '#'

            // Mostramos el resultado
            System.out.println("Palabra modificada: " + resultado);
        }

        scanner.close(); // Cerramos el objeto Scanner
    }
}