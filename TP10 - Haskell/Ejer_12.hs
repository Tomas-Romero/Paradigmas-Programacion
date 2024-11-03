largoPalabras :: [String] -> [Int]
largoPalabras lista = [length(x) | x<-lista]

listaEjemplo :: [String]
listaEjemplo = ["sol", "luna", "estrella", "planeta", "galaxia", "universo", "astro", "cometa", "cosmos", "meteoro"]