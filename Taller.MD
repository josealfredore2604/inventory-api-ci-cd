# Taller de Docker - Práctica de Contenedores

## Parte 1: Gestión Básica de Imágenes

1. Listar todas las imágenes disponibles
2. Descargar las imágenes: `nginx`, `postgres:15`, `mysql:8`
3. Etiquetar la imagen de nginx como `mi-nginx:v1.0`
4. Eliminar la imagen original de nginx (no la etiquetada)
5. Listar nuevamente las imágenes para verificar

## Parte 2: Contenedores Básicos

6. Crear un contenedor nginx llamado `web-server` en modo detached en el puerto 8080
7. Verificar que el contenedor está corriendo
8. Detener el contenedor
9. Listar todos los contenedores (incluidos los detenidos)
10. Iniciar nuevamente el contenedor
11. Eliminar el contenedor (forzadamente si es necesario)

## Parte 3: Logs y Ejecución de Comandos

12. Crear un contenedor nginx llamado `nginx-test` en el puerto 8081
13. Ver los logs del contenedor
14. Ejecutar el comando `ls /usr/share/nginx/html` dentro del contenedor
15. Acceder al bash del contenedor de forma interactiva
16. Dentro del contenedor, crear un archivo `index.html` con tu nombre en `/usr/share/nginx/html`
17. Salir del contenedor y verificar en el navegador que se muestra tu nombre

## Parte 4: Variables de Entorno

18. Crear un contenedor MySQL en modo detached con la variable `MYSQL_ROOT_PASSWORD=secreto123`
19. Acceder al contenedor MySQL y conectarte a la base de datos con el usuario root
20. Crear una base de datos llamada `taller_docker`
21. Verificar que la base de datos fue creada

## Parte 5: Volúmenes

22. Crear una carpeta en tu sistema llamada `mi-volumen`
23. Crear un archivo HTML dentro de esa carpeta con contenido personalizado
24. Crear un contenedor nginx montando tu carpeta en `/usr/share/nginx/html`
25. Verificar en el navegador que se muestra tu HTML personalizado
26. Modificar el HTML desde tu máquina y recargar el navegador

## Parte 6: Docker Compose

27. Crear un archivo `docker-compose.yml` con los siguientes servicios:
    - Una base de datos postgres
    - Una aplicación web nginx
    - Un contenedor MySQL

28. Levantar los servicios con docker compose
29. Verificar que todos los contenedores están corriendo
30. Ver los logs de todos los servicios
31. Detener todos los servicios
32. Levantar los servicios nuevamente con rebuild
33. Eliminar todos los contenedores creados por compose

## Parte 7: Limpieza

34. Listar todos los contenedores (activos e inactivos)
35. Eliminar todos los contenedores de una sola vez
36. Listar todas las imágenes
37. Eliminar todas las imágenes que no estés usando