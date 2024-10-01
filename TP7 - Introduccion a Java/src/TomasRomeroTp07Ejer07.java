import java.util.Scanner;
//Estudiante Tomas Romero
//Trabajo Practico N°7 - Ejercicio N°7
public class TomasRomeroTp07Ejer07 {
    public static void main(String[] args) {
        // Creamos un objeto Scanner para que el usuario ingrese la frase
        Scanner scanner = new Scanner(System.in);

        // Pedimos al usuario que ingrese una frase
        System.out.println("Ingrese una frase:");
        String frase = scanner.nextLine(); // Leemos toda la frase con espacios incluidos

        // Recorremos la frase letra por letra
        for (int i = 0; i < frase.length(); i++) {
            // Mostramos solo las letras en posiciones pares (0, 2, 4, etc.)
            if (i % 2 == 0) {
                System.out.print(frase.charAt(i)); // Imprimimos la letra sin cambiar de línea
            }
        }

        // Cerramos el Scanner
        scanner.close();
    }
}