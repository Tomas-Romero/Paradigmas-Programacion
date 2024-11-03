numerosPares :: [Int]
numerosPares = [ x | x <- [1..20], x `mod`  2 == 0 ]