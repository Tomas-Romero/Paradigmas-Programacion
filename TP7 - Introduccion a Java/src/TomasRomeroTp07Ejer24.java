import java.util.ArrayList;

//Estudiante Tomas Romero
//Trabajo Practico N°7 - Ejercicio N°24

public class TomasRomeroTp07Ejer24 {
    // Metodo para repetir el array dinámico
    public static ArrayList<String> repetir(ArrayList<String> original, int veces) {
        ArrayList<String> resultado = new ArrayList<>(); // Nuevo ArrayList para guardar el resultado

        // Repetimos el array original 'veces' veces
        for (int i = 0; i < veces; i++) {
            for (String elemento : original) {
                resultado.add(elemento); // Agregamos cada elemento al nuevo array
            }
        }

        return resultado; // Devolvemos el nuevo ArrayList
    }

    public static void main(String[] args) {
        // Creamos un ArrayList original
        ArrayList<String> miArray1 = new ArrayList<>();
        miArray1.add("a");
        miArray1.add("b");
        miArray1.add("c");

        // Llamamos al metodo y guardamos el resultado
        ArrayList<String> arrayRepetido = repetir(miArray1, 3);

        // Mostramos el resultado
        System.out.println("Array original: " + miArray1);
        System.out.println("Array repetido: " + arrayRepetido);
    }
}

