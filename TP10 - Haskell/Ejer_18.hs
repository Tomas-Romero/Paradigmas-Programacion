--Utilizando la primera forma por medio de Map
negativizar :: Int -> Int
negativizar x = x - x * 2

convertirNegativo :: [Int] -> [Int]
convertirNegativo lista = map doblar lista

--Utilizando funciones lambda
convertirNegativo2 :: [Int] -> [Int]
convertirNegativo2 lista = map (\x -> x - x * 2) lista