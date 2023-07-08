Proyecto indivudual - ML OPS

Este repositorio contiene los archivos necesarios para realizar un deploy de una FastAPI en Render.
El dataset con el que se trabajo fue movies y contiene informacion sobre aproximadamente 45.000 obras.
La API es capaz de devolver datos puntuales sobre el dataset y, ademas, proveer una recomendacion de peliculas basada en la similaridad de los registros.


Los archivos provistos son:

app.py: contiene la api en si y las funciones pertinentes para poder realizar consultas
data_api.csv: contiene los datos sobre los que se realizan las consultas
data_modelado_nn.csv: contiene datos modelados listos para ser consumidos por un modelo de NearestNeighbors

Instrucciones de uso:
Realizar deploy en render y acceder a la pagina de inicio seleccionada:

Se puede escribir a mano un url para obtener datos de la API

* Por ejemplo: <url>https://movies-api-fyi9.onrender.com/directores/James%20Cameron</url>



Se puede ingresar a <url>https://movies-api-fyi9.onrender.com/docs</url> para ver las opciones de consulta y usar la interfaz gráfica de FastAPI.

* /count_lang/{Idioma} --> devuelve la cantidad de peliculas producidas en un idioma: formato iso 639 (MAYÚSCULAS): <url>https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes</url>

* /duracion_pelicula/{Pelicula} --> devuelve la duracion y el año de estreno: hay que dar un nombre exacto (EJ:The Lord of the Rings: The Fellowship of the Ring)

* /franquicia/{Franquicia} --> devuelve cantidad de peliculas, ganancias totales y promedio de una franquicia

* /count_pais/{Pais} -->devuelve la cantidad de peliculas producidas en un pais: formato iso 3166 alpha 2: <url>https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements</url>

* /productoras/{Productora} --> devuelve el revenue total y cantidad de peliculas realizadas (EJ: Pixar Animation Studios)

* /directores/{nombre_director} --> devuelve el exito de un director, junto a una lista de peliculas con estadisticas (EJ: James Cameron)

* /recomendacion/{title} --> devuelve una lista con peliculas recomendadas en base al title provisto (EJ:The Lord of the Rings: The Fellowship of the Ring)



