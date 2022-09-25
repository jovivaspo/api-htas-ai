Crear imagen: 
docker build -t api-htas .

Iniciar el programa en terminal, puerto 4000 para docker, 3000 para navegador:
docker run -it -p 3000:4000 api-htas

ver programas corriendo: 
docker container ls

Iniciar el programa como proceso en segundo plano: 
docker run -it -p 3000:4000 -d api-htas

Para programa: 
docker stop id
