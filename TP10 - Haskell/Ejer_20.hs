invertir :: [a] -> [a]
invertir [] = []
invertir (x:xs) = invertir xs ++ [x]
inversa :: [[a]] -> [[a]]
inversa listaPalabras = map invertir listaPalabras