import java.util.Scanner;

//Estudiante Tomas Romero
//Trabajo Practico N°7 - Ejercicio N°14
public class TomasRomeroTp07Ejer14 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Pedimos al usuario que ingrese una frase para generar el acrónimo
        System.out.print("Ingresa una frase para generar su acrónimo: ");
        String fraseAcronimo = scanner.nextLine(); // Leemos la frase para generar acrónimo

        // Generamos el acrónimo usando el método generarAcronimo
        String acronimo = ParsearTexto.generarAcronimo(fraseAcronimo);
        System.out.println("Acrónimo: " + acronimo);

        scanner.close();
    }
}