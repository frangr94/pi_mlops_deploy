![Alt text](https://assets.soyhenry.com/henry-landing/assets/Henry/logo.png)
# Proyecto indivudual - ML OPS


Este repositorio contiene los archivos necesarios para realizar un deploy de una FastAPI en Render. Fue creado en el contexto de la cursada de la academia SoyHenry.

El dataset con el que se trabajo fue movies dataset y contiene informacion sobre aproximadamente 45.000 obras fílmicas.
La API es capaz de devolver datos puntuales sobre el dataset y, ademas, proveer una recomendacion de peliculas basada en la similaridad de los registros.


Los archivos provistos son:

* app.py: contiene la API en sí y las funciones pertinentes para poder realizar consultas

* /datasets/data_api.csv: contiene los datos sobre los que se realizan las consultas

* /datasets/data_modelado_nn.csv: contiene datos modelados listos para ser consumidos por un modelo de NearestNeighbors


### Instrucciones de uso:
Realizar deploy en render y acceder a la pagina de inicio seleccionada:

Se puede escribir a mano un url para obtener datos de la API

* Por ejemplo: <url>https://movies-api-fyi9.onrender.com/directores/James%20Cameron</url>



Se puede ingresar a <url>https://movies-api-fyi9.onrender.com/docs</url> para ver las opciones de consulta y usar la interfaz gráfica de FastAPI.

* /count_lang/{Idioma} --> devuelve la cantidad de peliculas producidas en un idioma: formato iso 639 (MAYÚSCULAS): <url>https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes</url>

* /duracion_pelicula/{Pelicula} --> devuelve la duracion y el año de estreno: hay que dar un nombre exacto (EJ: _The Lord of the Rings: The Fellowship of the Ring_)

* /franquicia/{Franquicia} --> devuelve cantidad de peliculas, ganancias totales y promedio de una franquicia (EJ: _Toy Story Collection_)

* /count_pais/{Pais} -->devuelve la cantidad de peliculas producidas en un pais: formato iso 3166 alpha 2: <url>https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements</url>

* /productoras/{Productora} --> devuelve el revenue total y cantidad de peliculas realizadas (EJ: Pixar Animation Studios)

* /directores/{nombre_director} --> devuelve el exito de un director, junto a una lista de peliculas con estadisticas (EJ: James Cameron)

* /recomendacion/{title} --> devuelve una lista con peliculas recomendadas en base al title provisto (EJ:The Lord of the Rings: The Fellowship of the Ring)



### De los datos a la API

El proceso que se le aplico a los datos se puede resumir en cuatro partes:


#### Transformacion primaria de los datos: 
En esta primera etapa se ingestaron los datos "en crudo" (movies.csv/credits.csv) y se les aplicaron varias transformaciones:

* Eliminación de datos con formatos incorrectos
* Join de las tablas
* Eliminación de nulos/reemplazo por 0, dependiendo del campo
* Cambiar formato de fechas
* Desanidado de campos
* Creacion de columnas a utilizar posteriormente (release_year y return)
* Exportacion de resultados a data_api.csv

#### Análisis exploratorio de los datos:
Luego se procedió a realizar un EDA con el fin de comprender un poco los datos con los que se estaba trabajando:

* Se realizaron gráficas para variables cuantitativas y cualitativas
* Se analizó la correlación entre algunas variables
* Se visualizaron rangos y outliers

#### Modelado de los datos para el modelo de recomendacion:
En esta segunda etapa de transformación se procedio a preparar los datos para ser ingestados por un modelo de NNeighbors(que utiliza el radio de una circunferencia para encontrar "N"-"vecinos" mas cercanos):

* Desempaquetado de listas obtenidas en el desanidamiento
* Scaling de campos cuantitativos usando varios métodos (z-score, minmax, max-absolutes) dependiendo de las distintas distribuciones
* Recategorización de campos categóricos con muchos valores posibles
* Exportacion de resultados a data_modelado_nn.csv

#### Construcción de la API y sus funciones pertinentes:
Por último, se construyó la API (FastAPI) con las funciones requeridas en el archivo app.py para ser desplegado en la versión gratuita de Render. También se realiza algo de preprocesamiento en la función recomendación ya que era necesario aplicar One Hot Encoding a las variables categóricas para luego sumarlas al array que alimenta al sistema. Cabe destacar que se experimentó con varios sistemas de recomendación, pero por una cuestion de recursos se optó por el presentado en este repositorio, ya que permitía utilizar la API en Render con el dataset completo sin crashear (los otros funcionaban de forma local, pero los 512mb de RAM que ofrece Render en su versión gratuita no fueron suficientes).

#### Nota
Los archivos (transformaciones.ipynb,EDA.ipynb,ingesta_nn.ipynb) se pueden ver en:
<url>https://drive.google.com/drive/folders/1nAai3gaKSxLjAQ16Kzgz8esPDXPm9ZEI</url>

### Hacia el futuro
La construcción de este proyecto presentó un desafío importante y fue clave para la integración de las herramientas vistas a lo largo de la etapa de bootcamp. En el futuro, espero embarcarme en data-aventuras aún más difíciles e incorporar nuevas herramientas que me permitan navegar el mundo de los datos y _El Código_.

¡ Muchas gracias por visitar mi repositorio !

frangr94


