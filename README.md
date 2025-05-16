# Prueba tecnica Plenitas
## Django REST Auth API con Registro de Dispositivos

API de autenticación con registro de dispositivos que implementa:
- Autenticación JWT con email como usuario
- Registro automático de dispositivos en login/registro
- Gestión centralizada de dispositivos por usuario
- Panel de administración completo

## ✨ Features

- ✅ Autenticación JWT con refresh token
- ✅ Registro de usuarios con email como identificador único
- ✅ Detección automática de IP del cliente
- ✅ Registro de dispositivo en cada login/registro
- ✅ Panel de administración personalizado

## 🛠 Tech Stack

- Python 3.10+
- Django 5.2
- Django REST Framework
- Simple JWT


## 🚀 Instalación

1. Clonar repositorio:
```bash
git clone https://github.com/AntonioManuelGarcia/prueba-plenitas/
cd proyecto
```
2. Crear y activar entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```
3.Instalar dependencias:
```bash
pip install -r requirements.txt
````
## Endpoints principales
Método	Endpoint	Descripción
- POST	/api/register/	Registro de nuevo usuario
- POST	/api/token/	Obtener JWT (login)
- POST	/api/token/refresh/	Refrescar JWT
- GET	/api/dispositivos/	Listar dispositivos del usuario

Ejemplo de registro

```bash
curl -X POST http://localhost:8000/api/register/ \
-H "Content-Type: application/json" \
-d '{"email": "user@example.com", "password": "Pass123!"}'
````
Ejemplo de login
```bash
curl -X POST http://localhost:8000/api/token/ \
-H "Content-Type: application/json" \
-d '{"email": "user@example.com", "password": "Pass123!"}'
````
Ejemplo de listado de dispositivos
```bash
curl http://localhost:8000/api/dispositivos/ \
-H "Authorization: Bearer tu_token_jwt"
````
