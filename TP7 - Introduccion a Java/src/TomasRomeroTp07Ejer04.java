import java.util.Scanner;
//Estudiante Tomas Romero
//Trabajo Practico N°7 - Ejercicio N°4
public class TomasRomeroTp07Ejer04 {
    public static void main(String[] args) {
        // Creamos un scanner para que el usuario ingrese un número
        Scanner scanner = new Scanner(System.in);

        // Le pedimos al usuario que ingrese un número y lo guardamos
        System.out.print("Ingrese un número: ");
        int numero = scanner.nextInt();

        // Guardamos el número original para compararlo después
        int numeroOriginal = numero;

        // Variable para guardar la cantidad de dígitos
        int cantidadDeDigitos = 0;

        // Hacemos una copia del número para contar sus dígitos
        int temp = numero;
        while (temp != 0) {
            // Por cada dígito, dividimos el número por 10 para eliminar el último dígito
            temp /= 10;
            // Sumamos 1 al contador de dígitos
            cantidadDeDigitos++;
        }

        // Reiniciamos la variable 'temp' para empezar de nuevo con el número original
        temp = numero;

        // Variable para almacenar la suma de los dígitos elevados a la cantidad de dígitos
        int suma = 0;

        // Recorremos cada dígito del número
        while (temp != 0) {
            // Obtenemos el último dígito usando el operador de resto
            int digito = temp % 10;

            // Elevamos el dígito a la cantidad de dígitos y lo sumamos
            suma += Math.pow(digito, cantidadDeDigitos);

            // Eliminamos el último dígito dividiendo por 10
            temp /= 10;
        }

        // Verificamos si la suma es igual al número original
        if (suma == numeroOriginal) {
            // Si la suma es igual al número, entonces es un número de Armstrong
            System.out.println(numeroOriginal + " es un Número de Armstrong.");
        } else {
            // Si no es igual, entonces no es un número de Armstrong
            System.out.println(numeroOriginal + " no es un Número de Armstrong.");
        }

        // Cerramos el scanner
        scanner.close();
    }
}