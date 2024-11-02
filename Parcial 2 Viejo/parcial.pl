% Juan Vergara
% Pelicula y genero
pelicula('2001: Una Odisea del Espacio', 'Ciencia Ficcion').
pelicula('The Killer', 'Suspenso').
pelicula('Soul', 'Animacion').
pelicula('La historia oficial', 'Drama').
pelicula('Her', 'Drama').
pelicula('The Shawshank Redemption', 'Drama').

% Definición de usuario/3
usuario(jose, 'The Killer', 7).
usuario(jose, 'The Shawshank Redemption', 10).
usuario(jose, 'Her', 8).

usuario(mario, 'Soul', 7).
usuario(mario, '2001: Una Odisea del Espacio', 8).

usuario(sofia, 'La historia oficial', 7).
usuario(sofia, 'Her', 7).

recomendar(Usuario, Recomendacion) :- 
    usuario(Usuario, Pelicula, Calificacion), % son la peliculas que vio el usuario
    Calificacion >= 4, % verifica que la nota de la pelicula sea mayor a 4
    pelicula(Recomendacion, Genero), % es el genero de la pelicula
    pelicula(Pelicula, Genero), % verifica que sean el mismo genero
    not(usuario(Usuario, Recomendacion, _)). % verifique que no repita la pelicula que ha visto el usuario

watch(Usuario, Pelicula) :- % el predicado tiene 2 argumentos, consulta si el usuario vio una pelicula en particular
    usuario(Usuario, Pelicula, _).