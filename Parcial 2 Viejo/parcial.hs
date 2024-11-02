{-- Juan Vergara --}
{-- 2) --}
lista numeros = product [x^2 | x <- numeros, numeros `mod` 2 == 0]

{-- 3) --}
inverso palabras = map reverse palabras
frase = "hola mundo"
resultado = inverso (words frase)
