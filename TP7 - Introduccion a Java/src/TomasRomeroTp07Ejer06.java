import java.util.Scanner;
//Estudiante Tomas Romero
//Trabajo Practico N°7 - Ejercicio N°6
public class TomasRomeroTp07Ejer06 {
    public static void main(String[] args) {
        // Creamos un objeto Scanner para que el usuario pueda ingresar datos desde el teclado
        Scanner scanner = new Scanner(System.in);

        // Pedimos al usuario que ingrese la longitud de la base de la pirámide
        System.out.println("Ingrese un número impar para la base de la pirámide:");
        int base = scanner.nextInt();

        // Verificamos que el número ingresado sea impar, si no, lo pedimos de nuevo
        if (base % 2 == 0) {
            System.out.println("Debe ingresar un número impar. Intente de nuevo.");
        } else {
            // Recorremos desde 1 hasta la base (solo los números impares)
            for (int i = 1; i <= base; i += 2) {
                // Imprimimos los caracteres 'X' de la línea actual
                for (int j = 0; j < i; j++) {
                    System.out.print("X"); // Imprime las 'X' sin cambiar de línea
                }
                System.out.println(); // Cambio de línea después de imprimir cada fila
            }
        }

        // Cerramos el Scanner (buena práctica)
        scanner.close();
    }
}