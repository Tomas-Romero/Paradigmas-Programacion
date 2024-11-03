quitarMinusculas :: String -> [Char]
quitarMinusculas texto = [x | x<-texto, x `elem` "QWERTYUIOPASDFGHJKLÑZXCVBNM"] --el 'elem' filtra las x que esten dentro de la cadena de condicional
