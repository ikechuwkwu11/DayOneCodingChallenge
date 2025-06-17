# 🔐 Flask Staff Token Authentication API
A lightweight and secure Flask-based authentication system for staff users using token-based access control. This project supports registration, login, logout, and protected route access using time-limited tokens and hashed passwords.

## 🚀 Features
- User registration and login with hashed passwords (via Flask-Bcrypt)
- Token generation on login (valid for 24 hours)
- Protected routes that require a valid token
- Secure logout that deactivates the token
- Session management using Flask-Login
- Lightweight database using SQLite via SQLAlchemy

## 🧰 Tech Stack
| Purpose            | Library/Tool        |
| ------------------ | ------------------- |
| Backend Framework  | Flask               |
| Session Management | Flask-Login         |
| Password Hashing   | Flask-Bcrypt        |
| Token Generation   | Python `secrets`    |
| ORM + Database     | SQLAlchemy + SQLite |


## 📫 API Endpoints
| Method | Route        | Description                       | Auth Required |
| ------ | ------------ | --------------------------------- | ------------- |
| POST   | `/register`  | Register a new staff user         | ❌             |
| POST   | `/login`     | Log in and receive a token        | ❌             |
| GET    | `/protected` | Access a token-protected resource | ✅             |
| POST   | `/logout`    | Log out and deactivate token      | ✅             |
	

Tokens expire after 24 hours and are generated using Python’s built-in secrets module for cryptographic safety.

## 🛡️ Security Highlights
- Passwords are hashed with bcrypt before storage
- Tokens are randomly generated and securely stored
- Token expiration enforced via timestamp comparison
- Uses Flask-Login to manage active sessions

## 📌 To-Do / Future Improvements
- Add JWT support as an alternative
- Add user roles (admin, staff, viewer)
- Admin dashboard or analytics route
- Unit tests with pytest or unittest
