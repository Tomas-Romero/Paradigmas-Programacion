import java.util.Scanner;

//Estudiante Tomas Romero
//Trabajo Practico N°7 - Ejercicio N°10
public class TomasRomeroTp07Ejer10 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // Creamos un objeto Scanner para leer la entrada

        // Pedimos al usuario que ingrese una palabra
        System.out.print("Ingresa una palabra: ");
        String palabra = scanner.nextLine(); // Leemos la palabra ingresada

        // Llamamos a la función que obtiene las consonantes
        String consonantes = obtenerConsonantes(palabra); // Obtenemos las consonantes

        // Mostramos las consonantes una por línea
        System.out.println("Consonantes encontradas:");
        for (int i = 0; i < consonantes.length(); i++) {
            System.out.println(consonantes.charAt(i)); // Mostramos cada consonante
        }

        scanner.close(); // Cerramos el objeto Scanner
    }

    // Función que devuelve una cadena con las consonantes de la palabra ingresada
    public static String obtenerConsonantes(String palabra) {
        StringBuilder resultado = new StringBuilder(); // Usamos StringBuilder para construir la cadena de consonantes

        // Recorremos cada letra de la palabra
        for (int i = 0; i < palabra.length(); i++) {
            char letra = palabra.charAt(i); // Obtenemos cada letra

            // Verificamos si la letra es una consonante
            if (Character.isLetter(letra) && !esVocal(letra)) {
                resultado.append(letra); // Agregamos la consonante al resultado
            }
        }

        return resultado.toString(); // Devolvemos la cadena de consonantes
    }

    // Función que verifica si una letra es una vocal
    public static boolean esVocal(char letra) {
        // Convertimos la letra a minúscula para la comparación
        letra = Character.toLowerCase(letra);
        return letra == 'a' || letra == 'e' || letra == 'i' || letra == 'o' || letra == 'u'; // Comprobamos si es vocal
    }
}