esMayorEdad :: [Int] -> String
esMayorEdad edad = 
    if edad >= 18 
        then "Mayor" 
        else if edad >= 0
            then "Menor"
            else "No es posible la edad"

mayoriaEdad :: [Int] -> [String]
mayoriaEdad listaEdades = map esMayorEdad listaEdades