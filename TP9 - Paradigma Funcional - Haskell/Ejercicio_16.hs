largoLista :: [a] -> Int
largoLista [] = 0
largoLista (_:listEjemplo) = 1 + largoLista listEjemplo
lista :: [Int]
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
