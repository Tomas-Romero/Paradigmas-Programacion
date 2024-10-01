import java.util.Scanner;

//Estudiante Tomas Romero
//Trabajo Practico N°7 - Ejercicio N°13
public class TomasRomeroTp07Ejer13 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // Creamos el objeto Scanner

        // Pedimos al usuario que ingrese otra frase para limpiar
        System.out.print("Ingresa otra frase para limpiar: ");
        String fraseParaLimpiar = scanner.nextLine(); // Leemos la frase para limpiar

        // Limpiamos la frase de caracteres no alfabéticos
        String soloLetras = ParsearTexto.soloLetras(fraseParaLimpiar);
        System.out.println("Frase solo con letras: " + soloLetras);

        scanner.close(); // Cerramos el Scanner
    }
}