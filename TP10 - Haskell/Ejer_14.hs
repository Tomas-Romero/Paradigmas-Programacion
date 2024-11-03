vocalesExtraidas :: String -> [Char]
vocalesExtraidas texto = [x | x<-texto, x `elem` "aeiouAEIOU"] --el 'elem' filtra las x que esten dentro de la cadena de condicional

