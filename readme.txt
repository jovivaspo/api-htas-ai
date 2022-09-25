Create image: 
docker build -t api-htas .

Start the program in terminal, port 4000 for docker, 3000 for browser:
docker run -it -p 3000:4000 api-htas

watch programmes running: 
docker container ls

Start the programme as a background process: 
docker run -it -p 3000:4000 -d api-htas

Stop: 
docker stop id
