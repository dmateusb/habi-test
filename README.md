# Cómo abordaré la prueba
Mi estrategia para solucionar la prueba técnica consiste en implementar dos microservicios 
usando unicamente librerías de Python, crearé una estructura que instancie un microservicio por cada subcarpeta que 
se encuentra dentro de la carpeta webserver/microservices, de esta manera solo tendré que cambiar parámetros en el comando
de ejecución principal. Una vez tenga esto dockerizaré el proyecto y dejaré dentro los comando del docker-compose 
para iniciar automáticamente los dos microservicios.
Para la conexión con la base de datos implementaré manualmente un ORM que se limite a tener las funcionales de filtrado
y consultas necesarias para resolver los puntos usando el conector de MySQL.

# Comando ejecución

Para iniciar los dos microservicios 
```
docker-compose up
```
Iniciando directamente el comando en python
```
python index.py -m property
python index.py -m operations
```
Para ejecutar los tests desde dentro del contenedor 
```
docker exec -it $(docker ps -aqf "name=habi_property_ms") sh -c "python3 -m unittest discover tests"
```
Para ejecutarlo directmente
```
python -m unittest discover tests
```
El json de ejemplo es el archivo request_filters_example.json

# Implementación likes

Para la implementacion de los likes propongo la creacipon de la tabla Likes la cual va a funcionar como una tabla de muchos a muchos
entre la tabla User y Property, para poder optimizar el calculo de los likes que lleva una propiedad cada vez que se guarde un nuevo
registro en la tabla Likes se incrementará un contador que será almacenado dentro de un nuevo campo en el model Property, este campo se 
llama likes_count, y se incrementa o decrementa dependiendo de si se añaaden o se eliminan registros en la tabla Likes.

Esto mismo se puede hacer para evitar la lógica que tiene que estar buscando cual es el registro del estado más reciente en la tabla
StatusHistory cuando se desea consultar el actual estado. En este caso cada que se guarda un nuevo registro en la tabla StatusHistory también
se actualiza el campo last_status_id dentro de la tabla Property

# Segundo ejercicio

La implementacion del segundo ejercicio se encuentra en el archivo second_exercise.py
