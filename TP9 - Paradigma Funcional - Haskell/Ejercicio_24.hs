duplicarPrimerItem :: [a] -> [a]
duplicarPrimerItem [] = []
duplicarPrimerItem (x:listaEjemplo) = x : x : listaEjemplo

lista :: [Char]
lista = "abcdefghijkl"
lista2 :: [Int]
lista2 = [1,2,3,4,5,6,7,8,9,0]