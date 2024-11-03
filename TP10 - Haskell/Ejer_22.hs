--utilizando la funciona lambda, se puede hacer realizando una fuincion previa que eleve al cuadrado un elemento y utilizandola debajo junto con el map
calcularCuadrados :: [Int] -> [Int]
calcularCuadrados lista = map (\x -> x^2) lista