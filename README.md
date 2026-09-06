## 1. Exercise Tracker ##

This is a work-in-progress application for exercise tracking. At its current form [sprint 1] it consists of 3 folders at the root: backend, frontend, and docs. The first sprint builds the bones of the tracker: setting the basics in place and getting things to run together.

In docs, you can find the sprint templates, tickets, and the reports and screencaps.
Backend uses FastAPI.
Frontend uses React+Vite.

The project has 5–6 sprints in total, all building on the bones of the previous sprints.

Find out more about the project (documentation, sprints, etc) at https://github.com/xamk-mire/Sovellusohjelmnoinnin-ajankohtaiskurssi-2026/blob/main/sprints/README.md


## 2. Prerequisites ##

To run the project with Docker Compose you need Docker Desktop, which runs the database, frontend, and backend containers.
You do not need to install Node.js or Python. They are already in the Docker containers.


## 3. Starting the application ##

1. Create the .env file.
The project includes an .env.example file for you to use as a basis.
For copying the .env.example file, run:

Copy-Item .env.example .env

At this point [sprint 1] not all of the variables in .env.example are read.
The ones being read right now are API_HOST and API_PORT. The rest are prepped as placeholders for later sprints.


2. Start the application
Docker Desktop has to be running before starting the app.
In PowerShell, go to the root of the project and run:

docker compose up --build

After this, Docker starts the containers for database, api, and web.


3. Open the application
After getting the application running, you can open the frontend in your browser:
http://localhost:5173/

You can access the API in:
http://localhost:8000/

API documentation:
http://localhost:8000/docs

API health check:
http://localhost:8000/health


4. Closing the application + restarting the application
When you want to close the application, input:

docker compose down

If you want to start it again, input:

docker compose up

Normally you don't need to build more than once, unless you make changes.


## 4. Backend development environment ##
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


## 5. Frontend ##
The frontend uses React and Vite.
The Compose setup uses Dockerfile in frontend/ to install dependencies for frontend and start the Vite server.


## 6. Web service ##
This app uses Vite dev server in Docker for ease of use – especially at this point of the course it is more straightforward.
There are Dockerfiles in both frontend/ and backend/ to make a combo that starts the whole stack with one command.

Since frontend runs React+Vite, frontend/Dockerfile uses node as a base image.
frontend/Dockerfile copies package.json and package-lock.json and then installs dependencies, after which it copies the rest of the frontend code.
Frontend port is 5173. API port is 8000.

In docker-compose.yml in the root folder, added a web service. It uses the frontend folder as a basis.


## 7. Troubleshooting ##

1. Port already in use
If Docker says the port is already in use, another application might be using it.
Try stopping the other application and run:

docker compose up --build

You can check running containers with:

docker compose ps


2. Postgres not ready
The API waits for the PostgreSQL service to become healthy before starting. The database might need a bit to start. Wait a few seconds and run to check the services:

docker compose ps

Try opening the application again.

You can also access logs:

docker compose logs api
docker compose logs db


3. Missing .env
If Docker Compose complains about missing environmental variables, make sure an .env file has been created from .env.example.

Copy-Item .env.example .env

Then start Compose again:

docker compose up --build