import java.util.Scanner;
//Estudiante Tomas Romero
//Trabajo Practico N°7 - Ejercicio N°3
public class TomasRomeroTp07Ejer03 {
    public static double calcularDias(int edad) {

        // calcula el peso en Marte

        return edad * 365;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Ingrese tu edad: "); // le pedimos al usuario su edad
        int edad = scanner.nextInt(); // guardamos el dato en la variable


        // calcula los dias
        double edadDias = calcularDias(edad);

        // mostramos el resultado
        System.out.println("Tienes: " + edadDias + " dias");
        scanner.close();
    }
}
