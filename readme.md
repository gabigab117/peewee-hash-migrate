# Peewee Hash Project

A simple Python application demonstrating user authentication and message management using Peewee ORM with Argon2 password hashing.

## Features

- **User Management**: Create and authenticate users with secure password hashing
- **Email Validation**: Validate email addresses using the `email-validator` package
- **Password Security**: Argon2 password hashing for enhanced security
- **Message System**: Users can create and manage messages
- **Database Migrations**: Automated database schema management

## Technologies Used

- **Peewee ORM**: Lightweight Python ORM
- **Argon2**: Modern password hashing algorithm
- **SQLite**: Local database storage
- **Email Validator**: Email validation library

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install peewee argon2-cffi email-validator peewee-migrate
   ```

## Database Setup

Create and run migrations to set up the database schema:

```bash
# Create initial migration
pw_migrate create --auto --auto-source models --database "sqlite:///db.db" --directory migrations initial_migration

# Apply migrations
pw_migrate migrate --database "sqlite:///db.db" --directory migrations
```

## Usage

Run the main application:
```bash
python main.py
```

### Creating a User
```python
from models import User

# Create a new user with hashed password
user = User.create_user(name="john", email="john@example.com", password="secure_password")
```

### User Authentication
```python
# Login user
if user.login("secure_password"):
    print("Login successful")
else:
    print("Invalid credentials")
```

### Creating Messages
```python
from models import Message

# Create a message for a user
Message.create(title="Hello", message="This is my first message", user=user)
```

## Project Structure

```
├── main.py          # Main application entry point
├── models.py        # Database models (User, Message)
├── settings.py      # Database configuration
├── migrations/      # Database migration files
└── readme.md        # Project documentation
```

## References

- [Email Validator Package](https://pypi.org/project/email-validator/)
- [Peewee Migrate Documentation](https://pypi.org/project/peewee-migrate/#from-shell)# peewee-hash-migrate
