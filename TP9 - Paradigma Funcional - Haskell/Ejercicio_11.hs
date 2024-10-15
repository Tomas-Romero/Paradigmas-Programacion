signo :: Float -> Int
signo x
    | x == 0 = 0
    | x > 0 = 1
    |otherwise = -1
     