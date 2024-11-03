lenLista :: [a] -> Int
contador :: Int
contador = 0
lenLista lista = sum [1 | _ <- lista] --Asi se forma una lista de 1(unos) y luego se suman el total


listaEjemplo :: [Int]
listaEjemplo = [1,2,4,5,23,12,13,14,15,16,167,45,632,333,44,134,3,4,5,6,76,7,7,7,10]

listaEjemplo2 :: [String]
listaEjemplo2 = ["sol", "luna", "estrella", "planeta", "galaxia", "universo", "astro", "cometa", "cosmos", "meteoro"]