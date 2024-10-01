import java.util.Scanner;

//Estudiante Tomas Romero
//Trabajo Practico N°7 - Ejercicio N°11
class ParsearTexto {
    // Método público que reemplaza los espacios por guiones bajos
    public static String chauEspacios(String frase) {
        // Reemplazamos todos los espacios por guiones bajos
        return frase.replace(" ", "_");
    }
    public static String kebabToCamel(String kebab) {
        // Separar la cadena en partes usando el guion como delimitador
        String[] partes = kebab.split("-");

        // Empezamos con la primera parte en minúsculas
        StringBuilder resultado = new StringBuilder(partes[0].toLowerCase());

        // Procesamos las siguientes partes
        for (int i = 1; i < partes.length; i++) {
            // Convertimos la primera letra a mayúscula y añadimos el resto de la palabra
            resultado.append(partes[i].substring(0, 1).toUpperCase()); // Primera letra en mayúscula
            resultado.append(partes[i].substring(1).toLowerCase()); // Resto en minúsculas
        }

        return resultado.toString(); // Convertimos el StringBuilder a String y lo devolvemos
    }
    public static String soloLetras(String frase) {
        StringBuilder resultado = new StringBuilder(); // Usamos StringBuilder para construir la nueva cadena

        // Recorremos cada carácter de la frase
        for (int i = 0; i < frase.length(); i++) {
            char caracter = frase.charAt(i); // Obtenemos el carácter en la posición actual
            // Verificamos si el carácter es una letra
            if (Character.isLetter(caracter)) {
                resultado.append(caracter); // Si es letra, lo añadimos a resultado
            }
        }

        return resultado.toString(); // Devolvemos la cadena solo con letras
    }
    // Metodo que genera un acrónimo a partir de una frase
    public static String generarAcronimo(String frase) {
        String[] palabras = frase.split(" "); // Separar la frase en palabras usando espacio
        StringBuilder acronimo = new StringBuilder(); // Usamos StringBuilder para construir el acrónimo

        // Recorremos cada palabra
        for (String palabra : palabras) {
            if (!palabra.isEmpty()) { // Verificamos que la palabra no esté vacía
                acronimo.append(palabra.charAt(0)); // Agregamos la primera letra de la palabra
            }
        }

        return acronimo.toString().toUpperCase(); // Convertimos a mayúsculas y devolvemos
    }
}

// Clase principal
public class TomasRomeroTp07Ejer11 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // Creamos el objeto Scanner

        // Pedimos al usuario que ingrese una frase
        System.out.print("Ingresa una frase: ");
        String frase = scanner.nextLine(); // Leemos la frase

        // Utilizamos el método chauEspacios de la clase ParsearTexto
        String fraseSinEspacios = ParsearTexto.chauEspacios(frase);

        // Mostramos la frase modificada
        System.out.println("Frase modificada: " + fraseSinEspacios);

        scanner.close(); // Cerramos el Scanner
    }
}