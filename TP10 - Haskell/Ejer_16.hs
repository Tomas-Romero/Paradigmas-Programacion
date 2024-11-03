mizip :: [a] -> [b] -> [(a, b)]
mizip xs ys = [(xs !! i, ys !! i) | i <- [0..(min (length xs) (length ys) - 1)]]
