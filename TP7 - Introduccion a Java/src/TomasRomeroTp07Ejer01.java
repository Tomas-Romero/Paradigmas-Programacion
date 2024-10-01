import java.util.Scanner;

public class TomasRomeroTp07Ejer01 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        // Se pide al usuario una palabra y se guarda en una variable.
        System.out.print("Ingrese una palabra: ");
        String palabra = scanner.nextLine();

        // Creamos un for que recorre la palabra y va mostrando letra por letra.
        for (int i = 0; i < palabra.length(); i++) {
            for(int j = 0; j < i; j++){
                // Creamos este for para ir imprimiendo por cada vez que se repita el
                // for inicial vaya agregando un espacio.
                System.out.print(" ");
            }
            System.out.println(palabra.charAt(i));
        }

        scanner.close();
    }
}