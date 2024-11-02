repetirA :: Int -> String
repetirA n
    | n <= 0    = ""
    | otherwise = "a" ++ repetirA (n - 1)

--Caso para otro caracter que se quiera
repetirLetra :: Int -> Char -> String
repetirLetra n c
    | n <= 0    = ""
    | otherwise = c : repetirLetra (n - 1) c
