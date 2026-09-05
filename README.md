This project is comprised of three (3) root folders: backend, frontend, and docs.
In docs, you can find the sprint templates and tickets.
In backend, we will start building the application.

## Backend development environment ##
Backend uses FastAPI with Uvicorn. Virtual environment's requirements are listed in backend/requirements.txt.

Setup:
Open terminal. At root:
    cd backend
    
    Create a Python virtual environment:
    python -m venv .venv

    On Windows Powershell, activate the virtual environment:
     .\.venv\Scripts\Activate.ps1
    
    Install the dependencies (from requirements.txt):
    pip install -r requirements.txt