# PruebaCodigoPython

Instrucciones de uso:

1. Clona el proyecto en tu máquina.

2. Dentro de la carpeta /PruebaCodigoPython/ crea un archivo .env

3. Agrega al archivo la variable de ruta a la base de datos, ejemplo:

"DATABASE_URL=sqlite:///./candidato.db"

4. Instala las dependencias necesarias

5. Ejecuta un servidor, ejemplo:

"uvicorn app.main:app --reload" (Referencia: https://www.uvicorn.org/#quickstart)

6. Lanza una petición desde un cliente API (p. ej. Postman):

curl -X POST "http://127.0.0.1:8000/candidato" -H "Content-Type: application/json" -d '{"dni":"12345678A", "name":"John", "surname":"Doe"}'