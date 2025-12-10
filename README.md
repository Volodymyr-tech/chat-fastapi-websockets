# FastApi mini-chat: Modern interface, websockets and SQLAlchemy

This project is a simple real-time chat application with user registration, authentication, message storage, and a basic web interface. It is built for learning purposes but is deployable without major rewrites.

### 🧰 Tech Stack
- Backend: FastAPI (Python)

- Database: SQLAlchemy + aiosqlite (async SQLite)

- Migrations: Alembic (async setup)
 
- Authentication: JWT tokens + password hashing (bcrypt / passlib)

- Real-time communication: WebSockets

- Frontend: HTML, CSS, Vanilla JavaScript

- Deployment: Ready for cloud deployment

### 📦 Project Structure

````
project_root/
│
├── app/
│   ├── database.py          # Database connection and base model
│   ├── config.py            # App configuration (.env reader)
│   ├── main.py              # App entry point
│   │
│   ├── users/               # User logic
│   │   ├── models.py        # User model
│   │   ├── dao.py           # Data access logic
│   │   ├── auth.py          # Auth logic (JWT, hashing, login/register)
│   │   ├── dependencies.py # Current user dependency
│   │   └── schemas.py      # Pydantic schemas
│   │
│   ├── chat/                # Chat logic
│   │   ├── models.py        # Message model
│   │   ├── dao.py           # Message DAO
│   │   ├── router.py       # Routes and WebSocket handlers
│   │   └── schemas.py      # Pydantic schemas for messages
│   │
│   ├── static/              # Frontend static files
│   │   ├── js/
│   │   │   ├── auth.js
│   │   │   └── chat.js
│   │   └── styles/
│   │       ├── auth.css
│   │       └── chat.css
│   │
│   └── templates/           # HTML templates
│       ├── auth.html        # Login / registration page
│       └── chat.html        # Chat page
│
├── .env                     # Environment variables
├── pyproject.toml         # Python dependencies
└── other project files
````

### 🚀 How to Run

- Clone the repository.
- Install dependencies
- Create a .env file like in .env.example
- Run database migrations:

```alembic init -t async migration
alembic revision --autogenerate -m "Initial revision"
alembic upgrade head
```
This will create the SQLite database with all required tables.

- Start the application:
```uvicorn app.main:app --reload ```

- Open in browser:
```http://127.0.0.1:8000```
You will see the authentication page. After logging in, you are redirected to the chat.

## ✅ Features

- User registration and login

- Secure password hashing

- JWT authentication with cookies

- Real-time messaging via WebSockets

- Message storage in SQLite

- Simple web interface (no frontend frameworks)

- Ready for deployment with minimal changes

## 🔧 What Can Be Improved

- File and media message support

- Online status and typing indicators

- Better UI/UX

- Replace SQLite with PostgreSQL for production

- User roles and permissions

- Tests, CI/CD

- Docker support

Right now this is a solid demo project, not a production-grade messenger. It does its job without pretending to be Telegram.

### 📄 License

No license specified by default. If you plan to use this publicly, add one (MIT is the usual painless choice).