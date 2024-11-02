--Definino la funcion como inLista y no in porque "in" ya esta reservada en Haskell
inLista :: Eq a => a -> [a] -> Bool
inLista _ [] = False
inLista elemento (x:listaEjemplo)
    | x == elemento = True
    | otherwise = inLista elemento listaEjemplo

lista :: [Char]
lista = "abcdefghijkl"
lista2 :: [Int]
lista2 = [1,2,3,4,5,6,7,8,9,0]