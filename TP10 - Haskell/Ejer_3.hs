numerosDivisibles3 :: [Int]
numerosDivisibles3 = [ x | x <- [1..100], x `mod`  3 == 0 ]