sumaLista :: [Int] -> Int
sumaLista [] = 0
sumaLista (a:listaEjemplo) = a + sumaLista listaEjemplo
--lista de Ejemplo
lista :: [Int]
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

