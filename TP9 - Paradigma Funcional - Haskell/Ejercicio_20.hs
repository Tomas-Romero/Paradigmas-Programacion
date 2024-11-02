ultimoPredefinido :: [a] -> a

ultimoPredefinido listaEjemplo = last listaEjemplo

ultimoAlterna :: [a] -> a
ultimoAlterna [x] = x
ultimoAlterna (_:listaEjemplo) = ultimoAlterna listaEjemplo


lista :: [Int]
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]