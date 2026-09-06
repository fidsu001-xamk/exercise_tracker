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


## Env example and settings ##
At this point (sprint 1, ticket 6) not all of the variables in .env.example are read.
The ones being read right now are API_HOST and API_PORT. The rest are prepped as placeholders for later.


## Web service ##
This app uses Vite dev server in Docker for ease of use – especially at this point of the course it is more straightforward.
There are Dockerfiles in both frontend/ and backend/ to make a combo that starts the whole stack with one command.

Since frontend runs React+Vite, frontend/Dockerfile uses node as a base image.
frontend/Dockerfile copies package.json and package-lock.json and then installs dependencies, after which it copies the rest of the frontend code.
Frontend port is 5173. API port is 8000.

In docker-compose.yml in the root folder, added a web service. It uses the frontend folder as a basis.

Start the application with:

docker compose up --build

The frontend can then be opened in browser at
http://localhost:5173/
