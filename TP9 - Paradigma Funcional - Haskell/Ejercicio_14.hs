mult :: Int -> Int -> Int
mult _ 0 = 0  -- Caso base: cualquier número multiplicado por 0 es 0
mult a b 
    | b > 0    = a + mult a (b - 1)  -- Si b es positivo, sumamos a repetidamente
    | b < 0    = - (mult a (-b))     -- Si b es negativo, usamos la misma lógica pero invirtiendo el signo