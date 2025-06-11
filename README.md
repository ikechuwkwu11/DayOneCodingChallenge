Flask Staff Token Authentication API
This project is a lightweight authentication system for staff users using Flask, Flask-Login, and token-based access control. It includes secure registration, login, logout, and a protected route that requires a valid token.

Features
- User registration and login with hashed passwords (bcrypt)
- Token generation on login, valid for 24 hours
- Token-based route protection
- Secure logout that deactivates the token
- Uses Flask-Login for session and user management
- SQLite database via SQLAlchemy

Tech Stack
- Python 
- Flask
- Flask-Login
- Flask-Bcrypt
- SQLAlchemy
- SQLite (default database)
- Secrets (for token generation
