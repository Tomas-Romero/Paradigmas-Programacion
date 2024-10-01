import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

//Estudiante Tomas Romero
//Trabajo Practico N°7 - Ejercicio N°23

public class TomasRomeroTp07Ejer23 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // Para leer la entrada del usuario
        ArrayList<String> colores = new ArrayList<>(); // Lista para almacenar los colores de los autos
        String color;

        // Pedimos colores al usuario
        System.out.println("Ingrese los colores de los autos que ve durante su viaje (escriba 't' para terminar):");

        while (true) {
            color = scanner.nextLine(); // Leemos el color ingresado por el usuario

            // Verificamos si el usuario quiere terminar
            if (color.equalsIgnoreCase("t")) { // Comparamos ignorando mayúsculas
                break; // Salimos del bucle
            }

            // Agregamos el color a la lista
            colores.add(color);
        }

        // Mapa para contar la cantidad de veces que aparece cada color
        HashMap<String, Integer> contadorColores = new HashMap<>();

        // Contamos la frecuencia de cada color
        for (String c : colores) {
            contadorColores.put(c, contadorColores.getOrDefault(c, 0) + 1);
        }

        // Variable para encontrar el color más común
        String colorMasComun = null;
        int maxCount = 0;

        // Buscamos el color más común
        for (Map.Entry<String, Integer> entry : contadorColores.entrySet()) {
            if (entry.getValue() > maxCount) {
                maxCount = entry.getValue(); // Actualizamos el máximo
                colorMasComun = entry.getKey(); // Guardamos el color más común
            }
        }

        // Mostramos el resultado
        if (colorMasComun != null) {
            System.out.println("El color de auto más común que vio durante su viaje es: " + colorMasComun);
        } else {
            System.out.println("No se ingresaron colores.");
        }

        scanner.close(); // Cerramos el scanner
    }
}
