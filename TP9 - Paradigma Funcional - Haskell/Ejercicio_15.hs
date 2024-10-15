-- Función sumarUno
sumarUno :: Integer -> Integer
sumarUno n = n + 1

-- Definir la función suma usando solo sumarUno
suma :: Integer -> Integer -> Integer
suma a 0 = a  -- Caso base: si b es 0, la suma es el primer número a
suma a b 
    | b > 0    = suma (sumarUno a) (b - 1)  -- Caso recursivo: si b es positivo, sumamos uno a a y restamos uno de b
    | b < 0    = suma (a - 1) (sumarUno b)       -- Caso recursivo: si b es negativo, restamos uno a a y sumamos uno a b
