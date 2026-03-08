# 🚀 API de Ventas – Mi Ruta SJR

API REST desarrollada con **FastAPI** para la gestión de **vendedores y productos**, diseñada como backend para aplicaciones que necesiten administrar inventario y productos asociados a vendedores.

La API permite realizar operaciones **CRUD** sobre vendedores y productos, así como consultar los productos asociados a cada vendedor. Además, incluye documentación automática generada con Swagger.

---

# 📌 Características

- API REST moderna  
- CRUD completo para **vendedores**  
- CRUD completo para **productos**  
- Consulta de productos por vendedor  
- Validación de datos con **Pydantic**  
- Documentación automática con Swagger  
- Conexión a base de datos mediante **Supabase**

---

# 🛠 Tecnologías utilizadas

- Python  
- FastAPI  
- Uvicorn  
- Supabase  
- Pydantic  
- Swagger UI  

---

# 📂 Estructura del proyecto

```bash
ventas-api
│
├── app
│   ├── core
│   ├── models
│   ├── routes
│   ├── services
│   └── main.py
│
├── requirements.txt
└── README.md
```

---

# 📚 Documentación de la API

La documentación interactiva se genera automáticamente con Swagger.

Accede a ella en:

```
/docs
```

Ejemplo:

```
http://localhost:8000/docs
```

Desde ahí puedes probar todos los endpoints de la API.

---

# 📡 Endpoints disponibles

## 👨‍💼 Vendedores

| Método | Endpoint | Descripción |
|------|------|------|
| GET | `/api/v1/vendedores` | Listar vendedores |
| POST | `/api/v1/vendedores` | Crear vendedor |
| GET | `/api/v1/vendedores/{vendedor_id}` | Obtener vendedor |
| PUT | `/api/v1/vendedores/{vendedor_id}` | Actualizar vendedor |
| DELETE | `/api/v1/vendedores/{vendedor_id}` | Eliminar vendedor |
| GET | `/api/v1/vendedores/{vendedor_id}/productos` | Obtener productos del vendedor |

---

## 📦 Productos

| Método | Endpoint | Descripción |
|------|------|------|
| GET | `/api/v1/productos` | Listar productos |
| POST | `/api/v1/productos` | Crear producto |
| GET | `/api/v1/productos/{product_id}` | Obtener producto |
| PUT | `/api/v1/productos/{product_id}` | Actualizar producto |
| DELETE | `/api/v1/productos/{product_id}` | Eliminar producto |

---

# ▶️ Ejecutar el proyecto

## 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/tuusuario/ventas-api.git
```

---

## 2️⃣ Crear entorno virtual

```bash
python -m venv venv
```

---

## 3️⃣ Activar entorno virtual

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 4️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Ejecutar la API

```bash
uvicorn app.main:app --reload
```

---

## 6️⃣ Abrir documentación

```
http://localhost:8000/docs
```

---

# 📌 Ejemplos de respuesta JSON

### Ejemplo de producto

```json
{
  "vendedor_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "name": "string",
  "price": 0,
  "category_id": 0,
  "quantity": 0,
  "min_stock": 0
}
```

### Ejemplo de vendedor

```json
{
  "nombre": "string",
  "nombre_local": "string",
  "direccion": "string",
  "telefono_1": "string",
  "telefono_2": "string",
  "email": "correo@ejemplo.com",
  "is_activated": true
}
```

---

# 🎯 Objetivo del proyecto

Este proyecto forma parte del desarrollo de **Mi Ruta SJR**, una plataforma que busca facilitar la gestión de productos y vendedores dentro de una aplicación que conecta negocios locales con usuarios.

---

# 👨‍💻 Autor

**Bryan Santiago**

Estudiante de Ingeniería en Desarrollo de Software  
Enfocado en desarrollo **Backend con Python, FastAPI y APIs REST**.
