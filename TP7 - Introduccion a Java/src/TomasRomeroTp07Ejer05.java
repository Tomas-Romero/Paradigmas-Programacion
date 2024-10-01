import java.util.Scanner;
import java.util.Random;
//Estudiante Tomas Romero
//Trabajo Practico N°7 - Ejercicio N°5
public class TomasRomeroTp07Ejer05 {
    public static void main(String[] args) {
        // Crear un objeto Random para generar números aleatorios (simula los dados)
        Random random = new Random();

        // Creamos un array para guardar las 6 habilidades: fuerza, destreza, constitución, inteligencia, sabiduría, carisma
        int[] habilidades = new int[6];

        // Nombres de las habilidades para mostrarlas después
        String[] nombresHabilidades = {"Fuerza", "Destreza", "Constitución", "Inteligencia", "Sabiduría", "Carisma"};

        // Recorremos cada habilidad para asignarle un valor aleatorio
        for (int i = 0; i < 6; i++) {
            habilidades[i] = generarHabilidad(random);
        }

        // Mostrar las habilidades generadas
        System.out.println("Habilidades del personaje:");
        for (int i = 0; i < 6; i++) {
            System.out.println(nombresHabilidades[i] + ": " + habilidades[i]);
        }

        // Calcular la salud (HP) del personaje
        int saludInicial = 10;
        int modificadorConstitucion = (int) Math.floor((habilidades[2] - 10) / 2.0); // habilidades[2] es la Constitución
        int saludFinal = saludInicial + modificadorConstitucion;

        // Mostrar la salud final del personaje
        System.out.println("Salud (HP): " + saludFinal);
    }

    // Función que genera una habilidad tirando 4 dados de 6 caras y sumando los 3 mayores
    public static int generarHabilidad(Random random) {
        // Array para guardar los valores de los 4 dados
        int[] dados = new int[4];

        // Tiramos 4 dados (números aleatorios entre 1 y 6)
        for (int i = 0; i < 4; i++) {
            dados[i] = random.nextInt(6) + 1; // Genera un número entre 1 y 6
        }

        // Encontrar el dado menor para descartarlo
        int menor = dados[0];
        for (int i = 1; i < 4; i++) {
            if (dados[i] < menor) {
                menor = dados[i];
            }
        }

        // Sumar los 3 dados mayores (restando el menor)
        int suma = 0;
        for (int i = 0; i < 4; i++) {
            suma += dados[i];
        }
        suma -= menor; // Quitamos el menor de la suma

        // Devolvemos la suma final
        return suma;
    }
}