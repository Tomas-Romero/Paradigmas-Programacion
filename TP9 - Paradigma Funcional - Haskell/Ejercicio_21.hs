contarElemento :: Char -> [Char] -> Int
contarElemento c listaEjemplo = length(filter (== c) listaEjemplo)

listaCaracteres :: [Char]
listaCaracteres = "abracadabra"
