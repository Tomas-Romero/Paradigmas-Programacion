--función para sumar una lista con map y lambda
sumarLista :: [Double] -> Double
sumarLista lista = sum (map (\x -> x) lista)

--calcularPromedio usando sumarLista y length
calcularPromedio :: [Double] -> Double
calcularPromedio lista = (sumarLista lista) / fromIntegral (length lista) --se usa para pasar a double un entero

