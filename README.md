# Simple Todo Application with FastAPI

A beginner-friendly REST API built with **FastAPI** to practice CRUD operations, database integration, authentication, and database migrations using SQLAlchemy and Alembic.

## Features

- Create and manage user accounts
- User authentication using OAuth2 password flow
- JWT access token generation and verification
- Password hashing with bcrypt
- Create, read, update, and delete Todo tasks
- PostgreSQL database integration
- SQLAlchemy ORM for database operations
- Alembic for database migrations
- Request validation using Pydantic
- Interactive API documentation with Swagger UI

## Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Migrations:** Alembic
- **Authentication:** OAuth2 and JWT
- **Password Hashing:** Passlib and bcrypt
- **Validation:** Pydantic
- **ASGI Server:** Uvicorn

## Project Structure

```text
FastAPI-Todo-Application/
├── main.py
├── database.py
├── models.py
├── routers/
│   ├── auth.py
│   └── todos.py
├── alembic/
├── alembic.ini
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

*Note: Adjust the structure to match your actual project files.*

## Installation and Setup

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd FastAPI-Todo-Application
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

On Linux or macOS:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file and configure your database connection and JWT secret.

```env
DATABASE_URL=sqlite
SECRET_KEY=your_secure_secret_key
ALGORITHM=HS256
```

Update your application to read these variables from the environment. Do not commit `.env` or real credentials to GitHub.

### 5. Configure the database

Create a PostgreSQL database named `TodoApplicationDatabase`, or update `DATABASE_URL` to match your database configuration.

### 6. Run database migrations

If Alembic is configured:

```bash
alembic upgrade head
```

### 7. Start the application

```bash
python -m uvicorn main:app --reload
```

The application will normally be available at:

http://127.0.0.1:8000

## API Documentation

FastAPI automatically generates interactive API documentation.

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

Use Swagger UI to test endpoints, submit JSON requests, authenticate, and inspect responses.

## Core API Operations

The exact paths depend on how the routers are registered in `main.py`.

| Operation | HTTP Method | Description |
|---|---|---|
| Create user | POST | Register a new user |
| Login | POST | Authenticate and obtain a JWT |
| Create Todo | POST | Create a task |
| List Todos | GET | Retrieve tasks |
| Get Todo | GET | Retrieve a specific task |
| Update Todo | PUT/PATCH | Modify a task |
| Delete Todo | DELETE | Remove a task |

## Authentication Workflow

1. Register a user through the user creation endpoint.
2. Log in using the username and password.
3. Copy the returned access token.
4. Click **Authorize** in Swagger UI.
5. Enter the bearer token if requested.
6. Test protected endpoints.

Protected routes should verify the token and enforce ownership so users cannot modify other users' tasks.

## Learning Objectives

This project is intended to practice:

- REST API development with FastAPI
- HTTP methods and status codes
- CRUD operations
- SQLAlchemy models and database sessions
- PostgreSQL connectivity
- Pydantic request validation
- Password hashing and authentication
- JWT-based authorization
- Dependency injection with `Depends()`
- Alembic database migrations
- API testing using Swagger UI

## Future Improvements

- Add pagination and filtering
- Add task priorities and due dates
- Implement role-based access control
- Add automated tests with Pytest
- Add Docker support
- Deploy the API to a cloud platform
- Add a frontend interface

## Security Notes

- Store credentials in environment variables.
- Use a strong, randomly generated JWT secret.
- Never store passwords in plain text.
- Add token expiration and proper error handling.
- Validate user permissions on protected endpoints.
- Keep secrets and virtual environments out of version control.

## License

This project is intended for learning and practice. Add a license if you plan to distribute or reuse it publicly.
