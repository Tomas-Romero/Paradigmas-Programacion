import java.util.Scanner;
import java.util.Random;

//Estudiante Tomas Romero
//Trabajo Practico N°7 - Ejercicio N°8
public class TomasRomeroTp07Ejer08 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // Creamos un objeto Scanner para leer la entrada
        Random random = new Random(); // Creamos un objeto Random para generar números aleatorios

        System.out.print("Ingresa una frase (mínimo 10 caracteres): "); // Pedimos al usuario que ingrese una frase
        String frase = scanner.nextLine(); // Leemos la frase ingresada

        // Verificamos si la frase tiene al menos 10 caracteres
        if (frase.length() < 10) {
            System.out.println("La frase debe tener al menos 10 caracteres."); // Mensaje de error
        } else {
            System.out.println("Letras aleatorias:"); // Mensaje para mostrar letras aleatorias

            // Usamos un bucle para mostrar 6 letras
            for (int i = 0; i < 6; i++) {
                // Generamos una posición aleatoria entre 0 y la longitud de la frase menos 1
                int posicionAleatoria = random.nextInt(frase.length());

                // Mostramos la letra en la posición aleatoria
                System.out.println(frase.charAt(posicionAleatoria));
            }
        }

        scanner.close(); // Cerramos el objeto Scanner
    }
}