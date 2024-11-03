aplicarALista :: (a -> b) -> [a] -> [b]
aplicarALista _ [] = [] --Si la lista esta vacia ya retorna la lista vacia
aplicarALista funcion (x:xs) = funcion x : aplicarALista funcion xs