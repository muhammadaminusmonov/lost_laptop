# 🖥️ Lost Laptop Tracker

> A FastAPI-based backend service for tracking and managing lost or stolen laptops and devices.

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.135.1-green.svg)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue.svg)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-✓-2496ED.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Configuration](#environment-configuration)
  - [Running with Docker](#running-with-docker)
  - [Running Locally](#running-locally)
- [API Endpoints](#-api-endpoints)
- [Authentication](#-authentication)
- [Database Migrations](#-database-migrations)
- [Testing](#-testing)
- [Makefile Commands](#-makefile-commands)
- [Contributing](#-contributing)
- [License](#-license)

## 🔍 Overview

**Lost Laptop Tracker** is a RESTful API backend designed to help users register, track, and manage their devices in case of loss or theft. Built with FastAPI, it provides a secure, scalable foundation for device management with JWT-based authentication and PostgreSQL persistence.

## ✨ Features

- 🔐 **User Authentication**: Secure signup/login with JWT access & refresh tokens
- 👤 **User Management**: Create and manage user accounts
- 💻 **Device Management**: Register, list, update, and track lost/stolen devices
- 🏷️ **Category System**: Organize devices by custom categories (e.g., "Work", "Personal")
- 🗄️ **PostgreSQL Database**: Reliable data persistence with SQLAlchemy ORM
- 🐳 **Docker Support**: Easy deployment with Docker Compose
- 🧪 **Testing Ready**: pytest integration for API testing
- 🔄 **Alembic Migrations**: Database schema versioning and migrations

## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| **Framework** | FastAPI 0.135.1 |
| **Language** | Python 3.9+ |
| **Database** | PostgreSQL 15 |
| **ORM** | SQLAlchemy 2.0 + Alembic |
| **Auth** | JWT (python-jose), passlib, bcrypt |
| **Validation** | Pydantic 2.x |
| **Server** | Uvicorn (ASGI) |
| **Containerization** | Docker, Docker Compose |
| **Testing** | pytest |
| **Environment** | python-dotenv |

## 📁 Project Structure

```
lost_laptop/
├── app/
│   ├── api/v1/
│   │   ├── auth.py        # Authentication endpoints (login/signup)
│   │   ├── user.py        # User management endpoints
│   │   ├── device.py      # Device CRUD endpoints
│   │   └── category.py    # Category management endpoints
│   ├── core/
│   │   ├── config.py      # Application configuration
│   │   ├── database.py    # Database connection & session management
│   │   └── security.py    # Password hashing & JWT token utilities
│   ├── crud/
│   │   ├── user.py        # User database operations
│   │   ├── device.py      # Device database operations
│   │   └── category.py    # Category database operations
│   ├── models/
│   │   ├── user.py        # SQLAlchemy User model
│   │   ├── device.py      # SQLAlchemy Device model
│   │   └── category.py    # SQLAlchemy Category model
│   ├── schemas/
│   │   ├── auth.py        # Pydantic schemas for auth requests/responses
│   │   ├── user.py        # User data schemas
│   │   ├── device.py      # Device data schemas
│   │   └── category.py    # Category data schemas
│   └── main.py            # FastAPI app entry point
├── docker/
│   └── ...                # Docker configuration files
├── .github/workflows/     # CI/CD pipeline configurations
├── docker-compose.yml     # Multi-container orchestration
├── Dockerfile             # Application container definition
├── Makefile               # Development utility commands
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variables template
└── README.md              # This file
```

## 🚀 Getting Started

### Prerequisites

- Docker & Docker Compose **OR** Python 3.9+ with pip
- PostgreSQL (if running locally without Docker)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/muhammadaminusmonov/lost_laptop.git
   cd lost_laptop
   ```

2. **Create and configure environment file**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration values
   ```

### Environment Configuration

Copy `.env.example` to `.env` and configure the following variables:

```env
POSTGRES_DB=your_database_name
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_secure_password
DATABASE_URL=postgresql://user:password@localhost:5432/your_database
SECRET_KEY=your-super-secret-jwt-key-change-in-production
ACCESS_TOKEN_EXPIRE_MINUTES=60
ALGORITHM=HS256
```

> ⚠️ **Security Note**: Never commit your `.env` file or use default values in production.

### Running with Docker (Recommended)

```bash
# Build and start all services
make run

# Or manually:
docker compose up --build
```

The API will be available at: **http://localhost:8000**

Interactive API docs (Swagger UI): **http://localhost:8000/docs**

### Running Locally (Without Docker)

1. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start PostgreSQL database** (ensure it's running and configured in `.env`)

4. **Run database migrations** (if Alembic is configured)
   ```bash
   alembic upgrade head
   ```

5. **Start the development server**
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

## 🔌 API Endpoints

### Authentication (`/auth`)

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|--------------|
| POST | `/auth/signup` | Register new user | ❌ |
| POST | `/auth/login` | Login and receive JWT tokens | ❌ |

**Example Signup Request:**
```json
{
  "email": "user@example.com",
  "password": "secure_password_123"
}
```

**Example Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### User Management (`/user`)

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|--------------|
| GET | `/user/me` | Get current user profile | ✅ |
| PUT | `/user/me` | Update current user profile | ✅ |

### Device Management (`/device`)

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|--------------|
| GET | `/device/` | List all user's devices | ✅ |
| POST | `/device/` | Register a new device | ✅ |
| GET | `/device/{id}` | Get device details | ✅ |
| PUT | `/device/{id}` | Update device information | ✅ |
| DELETE | `/device/{id}` | Remove a device | ✅ |

### Category Management (`/category`)

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|--------------|
| GET | `/category/` | List all categories | ✅ |
| POST | `/category/` | Create new category | ✅ |
| PUT | `/category/{id}` | Update category | ✅ |
| DELETE | `/category/{id}` | Delete category | ✅ |

> ✅ = Requires valid JWT token in `Authorization: Bearer <token>` header

## 🔐 Authentication

This API uses JWT (JSON Web Tokens) for authentication:

1. **Signup/Login** → Receive `access_token` and `refresh_token`
2. **Include access token** in subsequent requests:
   ```
   Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
   ```
3. **Token expiration**: Access tokens expire after `ACCESS_TOKEN_EXPIRE_MINUTES` (default: 60 min)
4. **Refresh tokens**: Use to obtain new access tokens without re-authenticating

## 🗄️ Database Migrations

Alembic is used for database schema migrations:

```bash
# Generate new migration after model changes
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head

# Rollback migrations
alembic downgrade -1
```

## 🧪 Testing

Run tests using pytest:

```bash
# With Docker
make test

# Or manually
docker compose exec app pytest

# Locally (with test database configured)
pytest
```

## ⚙️ Makefile Commands

| Command | Description |
|---------|-------------|
| `make run` | Build and start containers |
| `make down` | Stop and remove containers |
| `make restart` | Restart containers with rebuild |
| `make logs` | Follow application logs |
| `make shell` | Open bash shell in app container |
| `make test` | Run pytest suite |
| `make build` | Build Docker images |
| `make rebuild` | Full rebuild with volume cleanup |
| `make clean` | Prune unused Docker resources |

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

Please ensure:
- ✅ Code follows PEP 8 style guidelines
- ✅ New features include tests
- ✅ Documentation is updated
- ✅ All tests pass (`make test`)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

> **Disclaimer**: This is a backend API service. A frontend client or mobile app would be needed for end-user interaction. Ensure proper security measures (HTTPS, secret management, rate limiting) are implemented before deploying to production.

**Built with ❤️ by [muhammadaminusmonov](https://github.com/muhammadaminusmonov) and contributors**
