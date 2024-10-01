import java.util.Scanner;
//Estudiante Tomas Romero
//Trabajo Practico N°7 - Ejercicio N°2
public class TomasRomeroTp07Ejer02 {
    public static double calcularPesoEnMarte(double masa) {

        // calcula el peso en Marte

        return masa * 3.71;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Ingrese tu masa en Kg: "); // le pedimos al usuario su masa
        double masa = scanner.nextDouble(); // guardamos el dato en la variable

        double peso = masa * 3.71; // calculamos el peso y lo guardamos en la variable

        System.out.println("Tu peso en Martes es: " + peso + " kg"); // mostramos el resultado

        // calcula el peso en Marte llamando a la función
        double pesoMarte = calcularPesoEnMarte(masa);

        // mostramos el resultado
        System.out.println("Tu peso en Marte es: " + pesoMarte + " kg");
        scanner.close();
    }
}