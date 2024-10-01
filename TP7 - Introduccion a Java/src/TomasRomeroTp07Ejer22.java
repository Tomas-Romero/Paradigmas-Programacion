import java.util.Random;
import java.util.ArrayList;

//Estudiante Tomas Romero
//Trabajo Practico N°7 - Ejercicio N°22

public class TomasRomeroTp07Ejer22 {
    public static void main(String[] args) {
        // Declaramos y inicializamos un ArrayList de cadenas
        ArrayList<String> lista = new ArrayList<>();

        // Agregamos elementos a la lista
        lista.add("Hola");
        lista.add("Mundo");
        lista.add("Java");

        // Mostramos la lista
        System.out.println("Lista original: " + lista);

        // Reemplazamos un elemento
        lista.set(1, "Programación");
        System.out.println("Lista después de reemplazar: " + lista);

        // Eliminamos un elemento
        lista.remove("Hola");
        System.out.println("Lista después de eliminar: " + lista);

        // Mostramos el tamaño de la lista
        System.out.println("Tamaño de la lista: " + lista.size());

        // Verificamos si un elemento existe
        if (lista.contains("Java")) {
            System.out.println("La lista contiene 'Java'.");
        }

        // Limpiamos la lista
        lista.clear();
        System.out.println("Lista después de limpiar: " + lista);
    }
}