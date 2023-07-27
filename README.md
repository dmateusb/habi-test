# Cómo abordaré la prueba
Mi estrategia para solucionar la prueba técnica consiste en implementar dos microservicios 
usando unicamente librerías de Python, crearé una estructura que instancie un microservicio por cada subcarpeta que 
se encuentra dentro de la carpeta webserver/microservices, de esta manera solo tendré que cambiar parámetros en el comando
de ejecución principal. Una vez tenga esto dockerizaré el proyecto y dejaré dentro de los comando del docker-compose 
los comando para iniciar automáticamente los dos microservicios.
Para la conexión con la base de datos implementaré manualmente un ORM que se limite a tener las funcionales de filtrado
y consultas necesarias para resolver los puntos usando el conector de MySQL.