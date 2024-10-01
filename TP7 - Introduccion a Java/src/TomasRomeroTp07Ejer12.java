import java.util.Scanner;

//Estudiante Tomas Romero
//Trabajo Practico N°7 - Ejercicio N°12
// Clase principal
public class TomasRomeroTp07Ejer12 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // Creamos el objeto Scanner

        // Pedimos al usuario que ingrese una frase
        System.out.print("Ingresa una frase: ");
        String frase = scanner.nextLine(); // Leemos la frase

        // Utilizamos el método chauEspacios de la clase ParsearTexto
        String fraseSinEspacios = ParsearTexto.chauEspacios(frase);
        System.out.println("Frase modificada: " + fraseSinEspacios);

        // Pedimos al usuario que ingrese una palabra en kebab-case
        System.out.print("Ingresa una palabra en kebab-case: ");
        String kebab = scanner.nextLine(); // Leemos la palabra en kebab-case

        // Convertimos a camelCase usando el método kebabToCamel
        String camelCase = ParsearTexto.kebabToCamel(kebab);

        // Mostramos la palabra en camelCase
        System.out.println("Palabra en camelCase: " + camelCase);

        scanner.close(); // Cerramos el Scanner
    }
}