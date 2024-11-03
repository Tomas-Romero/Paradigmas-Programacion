quicksort :: Ord a => [a] -> [a]
quicksort [] = []  -- Caso base: una lista vacía ya está ordenada
quicksort (pivote:xs) = 
    quicksort menores ++ [pivote] ++ quicksort mayores
  where
    menores = filter (< pivote) xs  -- Elementos menores que el pivote
    mayores = filter (>= pivote) xs  -- Elementos mayores o iguales al pivote
