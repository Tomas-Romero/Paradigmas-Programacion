--Utilizando la primera forma por medio de Map
doblar :: Int -> Int
doblar x = x * 2

doblarNumeros :: [Int] -> [Int]
doblarNumeros lista = map doblar lista

--Utilizando funciones lambda
doblarNumeros2 :: [Int] -> [Int]
doblarNumeros2 lista = map (\x -> x * 2) lista
