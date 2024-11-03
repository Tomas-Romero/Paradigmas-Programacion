moverPrimeraFinal :: String -> String
moverPrimeraFinal "" = ""  -- Si la palabra es vacía, retorna una cadena vacía
moverPrimeraFinal (x:palabra) = palabra ++ [x]  -- Remueve la primera letra y la coloca al final
