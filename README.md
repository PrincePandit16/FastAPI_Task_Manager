# 📝 FastAPI Task Manager

![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-v2-E92063?style=for-the-badge&logo=pydantic&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-Auth-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI-499848?style=for-the-badge&logo=gunicorn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

A RESTful Task Management API built with **FastAPI**, **SQLAlchemy**, and **MySQL** — featuring JWT authentication, role-based users, and full CRUD operations on tasks.

---

## 🚀 Features

- 🔐 User registration & login with **JWT Bearer authentication**
- 🔒 Passwords hashed with **Argon2** via `passlib`
- ✅ Full **CRUD** for tasks (Create, Read, Update, Delete)
- 🎯 Task **priority levels** (`low`, `medium`, `high`)
- 👤 Each user can only access their **own tasks**
- 🗄️ **MySQL** database with SQLAlchemy ORM
- 📄 Auto-generated **Swagger UI** docs at `/docs`

---

## 🗂️ Project Structure

```
project/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app entry point
│   ├── database.py      # DB engine, session, Base
│   ├── models.py        # SQLAlchemy ORM models (User, Task)
│   ├── schemas.py       # Pydantic request/response schemas
│   ├── utils.py         # Password hashing, JWT logic
│   └── routes/
│       ├── __init__.py
│       ├── auth.py      # Signup & Login routes
│       └── task.py      # Task CRUD routes
```

---

## ⚙️ Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| Database | MySQL |
| ORM | SQLAlchemy |
| Auth | JWT (`python-jose`) |
| Password Hashing | Argon2 (`passlib`) |
| Validation | Pydantic v2 |
| Server | Uvicorn |

---

## 🛠️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/fastapi-task-manager.git
cd fastapi-task-manager
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy pymysql passlib[argon2] python-jose[cryptography] pydantic[email]
```

### 4. Configure the database

Update the credentials in `app/database.py` to match your MySQL setup:

```python
MYSQL_USER = "your_user"
MYSQL_PASSWORD = "your_password"
MYSQL_HOST = "localhost"
MYSQL_PORT = "3306"
MYSQL_DATABASE = "fastapi_db"
```

Then create the database in MySQL:

```sql
CREATE DATABASE fastapi_db;
```

### 5. Run the application

```bash
uvicorn app.main:app --reload
```

The app will be available at `http://127.0.0.1:8000`

---

## 📖 API Reference

### 🔑 Auth

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/auth/signup` | Register a new user |
| `POST` | `/auth/login` | Login and receive a JWT token |

### ✅ Tasks *(requires Bearer token)*

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/tasks/` | Create a new task |
| `GET` | `/tasks/` | Get all tasks for the current user |
| `GET` | `/tasks/{task_id}` | Get a specific task by ID |
| `PUT` | `/tasks/{task_id}` | Update a task |
| `DELETE` | `/tasks/{task_id}` | Delete a task |

---

## 🔐 Authentication Flow

1. **Sign up** via `POST /auth/signup` with `username`, `email`, and `password`
2. **Log in** via `POST /auth/login` with your credentials
3. Copy the returned `access_token`
4. Pass it as a **Bearer token** in the `Authorization` header for all `/tasks` requests:

```
Authorization: Bearer <your_token>
```

---

## 📦 Example Requests

### Signup
```json
POST /auth/signup
{
  "username": "john",
  "email": "john@example.com",
  "password": "secret123"
}
```

### Login
```json
POST /auth/login
(form-data)
username=john&password=secret123
```

### Create Task
```json
POST /tasks/
Authorization: Bearer <token>
{
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "priority": "high"
}
```

### Update Task
```json
PUT /tasks/1
Authorization: Bearer <token>
{
  "completed": true
}
```

---

## 📊 Data Models

### User
| Field | Type | Notes |
|---|---|---|
| `id` | Integer | Primary key |
| `username` | String(50) | Unique |
| `email` | String(255) | Unique |
| `hashed_password` | String(255) | Argon2 hash |
| `role` | String(20) | Default: `"user"` |

### Task
| Field | Type | Notes |
|---|---|---|
| `id` | Integer | Primary key |
| `title` | String(100) | Required |
| `description` | String(500) | Optional |
| `completed` | Boolean | Default: `false` |
| `priority` | String(20) | `low` / `medium` / `high` |
| `created_at` | DateTime | Auto-set |
| `updated_at` | DateTime | Auto-updated |
| `owner_id` | Integer | FK → users.id |

---

## 📝 Interactive Docs

FastAPI provides auto-generated documentation out of the box:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## ⚠️ Security Notes

- The `SECRET_KEY` in `utils.py` should be moved to an environment variable (`.env` file) before deploying to production.
- Database credentials should also be stored in environment variables, not hardcoded.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
