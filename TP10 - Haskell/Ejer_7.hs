numerosPares :: [Int]
numerosPares = [ x | x <- [1..50], x `mod`  2 == 0, x `mod` 4 /= 0]