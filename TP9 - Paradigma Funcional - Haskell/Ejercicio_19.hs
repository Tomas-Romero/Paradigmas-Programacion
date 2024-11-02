-- Función sumarUno
invertirLista :: [a] -> [a]
invertirLista [] = []
invertirLista (x:ejemplo) = invertirLista ejemplo ++ [x]

lista :: [Int]
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
