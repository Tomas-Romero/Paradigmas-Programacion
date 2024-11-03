--Utilzando el even como predefinida de haskell junto con filter
filtrarPares :: [Int] -> [Int]
filtrarPares lista = filter even lista --even ya esta definida en haskell
--filter conbminado con funciones lambda
filtrarPares2 :: [Int] -> [Int]
filtrarPares2 lista = filter (\x -> x `mod` 2 == 0) lista --se podria definir la funcion lambda anteriormente utilizando una manera mas extendsa 