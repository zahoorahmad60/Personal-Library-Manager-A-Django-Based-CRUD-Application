# Personal Library Manager

**Author**: Zahoor Ahmad

This web-based application helps users manage their personal library. Users can add, view, update, and delete books in their library while ensuring secure user authentication.

---

## How to Run

Follow these steps to set up and run the application on your local machine:

### 1. Clone the Repository
```bash
git clone <https://github.com/zahoorahmad60/Personal-Library-Manager-A-Django-Based-CRUD-Application>
cd library_manager
```

### 2. Create a Python Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Development Server
```bash
python manage.py runserver
```

Access the application at `http://127.0.0.1:8000/`.

---

## Installation Steps

1. **Install Python**: Ensure Python 3.8 or higher is installed.
2. **Install Django**: Included in `requirements.txt`.
3. **Install Dependencies**:
   - Use `pip install -r requirements.txt` to install all necessary packages.

---

## Folder Structure
```
personal_library_manager/
|-- manage.py                  # Django project management file
|-- library_manager/  # Main project settings
|   |-- __init__.py
|   |-- settings.py            # Project settings
|   |-- urls.py                # URL configuration
|   |-- wsgi.py                # WSGI application
|-- books/               # Custom app for book management
|   |-- migrations/            # Database migrations
|   |-- templates/             # HTML templates
|   |-- models.py              # Data models for the app
|   |-- views.py               # Views for CRUD and authentication
|   |-- urls.py                # URL routing for the app
|-- accounts/               # Custom app for book management
|   |-- migrations/            # Database migrations
|   |-- templates/             # HTML templates
|   |-- models.py              # Data models for the app
|   |-- views.py               # Views for CRUD and authentication
|   |-- urls.py                # URL routing for the app
|-- db.sqlite3                 # SQLite database
|-- requirements.txt           # Project dependencies
|-- README.md                  # Project documentation
```
---

## Notes
- Zahoor Ahmad developed this application to demonstrate CRUD operations and user authentication in Django.
- The application uses SQLite as the default database for simplicity.
