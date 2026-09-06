# Sprint 1 report — Foundation

Copy this file to `docs/reports/sprint-01.md` in **your** repo and fill the blanks. Keep it a process log: no pasted source, no secrets, no `.env` values.

| Field        | Your answer |
| ------------ | ----------- |
| **Dates**    |             |
| **Names**    |             |
| **Repo URL** |             |
| **Branch**   |             |

Tickets: [sprint-01-tickets.md](../tickets/sprint-01-tickets.md) · Index: [../README.md](../README.md)

## Sprint goal

From the tickets: ship a runnable skeleton so later sprints can focus on features. You are done when Compose starts `db`, `api`, and `web`; `GET /health` returns JSON; the frontend opens; the README covers clone → `.env` → Compose → URLs.

In your words (2–3 sentences): did you meet that, and what is still rough?

## Tickets

For **each** ticket fill **Status** and **PR / commit**.

Fill **Demonstration** only where this template includes that section. Follow the numbered steps exactly. Store images under `docs/reports/images/sprint-01/` using the suggested filename. Crop secrets.

For **every** ticket: set **Used AI?** to `Yes` or `No`. Write the sprint-level **AI usage** reflection at the end of this report (not under each ticket).

Skip stretch tickets you did not do. Stretch: Status, PR, and Used AI? for each stretch you did; add a Demonstration only where listed below.

### S1-01 — Create monorepo layout and root `.gitignore` (Must)

- **Status:** Done / deferred (why): `Done`
- **PR / commit:** `ffb390d S1-01: project foundation + gitignore added`
- **Used AI?** Yes / No `Yes`

### S1-02 — FastAPI app skeleton (Must)

- **Status:** `Done`
- **PR / commit:** `2f99c46 S1-02: FastAPI app skeleton added`
- **Demonstration:**
  1. **Do this:** From `backend/`, start Uvicorn (`uvicorn app.main:app --reload` or your documented command). Open `http://localhost:8000/docs` in a browser.
  2. **Capture:** Screenshot of the OpenAPI / Swagger UI page.
  3. **Must show:** The `/docs` page loaded (title or Swagger chrome visible) and that the API is reachable (page is not a connection error).
  4. **Must not show:** `.env` contents, database passwords, or unrelated desktop clutter with secrets.
  5. **Save as:** `docs/reports/images/sprint-01/s1-02-docs.png`
  6. **Caption (1–2 sentences):** `A screencap of Swagger UI page, with the /docs page loaded.`
- **Used AI?** Yes / No `Yes`

### S1-03 — Health endpoint (Must)

- **Status:** `Done`
- **PR / commit:** `db0f7fb S1-03 added health endpoint`
- **Demonstration:**
  1. **Do this:** With the API running, open `http://localhost:8000/health` in the browser, or use Try it out on `GET /health` in `/docs`.
  2. **Capture:** Screenshot of the JSON response (browser or `/docs` response panel).
  3. **Must show:** HTTP success and a JSON body for `/health` (fields as in your ticket acceptance criteria, for example status).
  4. **Must not show:** Stack traces, env dumps, or secrets.
  5. **Save as:** `docs/reports/images/sprint-01/s1-03-health.png`
  6. **Caption (1–2 sentences):** `A screencap of FastAPI's Swagger UI showing health check response. Showing HTTP status code 200 and that status is ok.`
- **Used AI?** Yes / No `Yes`

### S1-04 — Python dependencies (Must)

- **Status:** `Done`
- **PR / commit:** `c8dc9f3 added Python virtual environment and reqs`
- **Used AI?** Yes / No `No`

### S1-06 — Env example and settings (Must)

- **Status:** `Done`
- **PR / commit:** `fdb0b00 S1-06 added env example and settings`
- **Used AI?** Yes / No `Yes`

### S1-07 — Docker Compose for db and api (Must)

- **Status:** `Done`
- **PR / commit:** `86d2463 S1-07 Docker Compose for db and api added`
- **Demonstration:**
  1. **Do this:** From the repo root, run `docker compose up --build` (or your documented equivalent). Wait until services settle. Run `docker compose ps` (or show the Docker Desktop containers view).
  2. **Capture:** Screenshot of the terminal `ps` output or Docker UI listing services.
  3. **Must show:** Both `db` and `api` listed as running / healthy (or equivalent status for your Compose file).
  4. **Must not show:** Full `.env` values, Postgres passwords in clear text, or cloud credentials.
  5. **Save as:** `docs/reports/images/sprint-01/s1-07-compose-db-api.png`
  6. **Caption (1–2 sentences):** `Screencap of a docker compose ps report, showing both api and db running. Full .env values, passwords etc are not showing.`
- **Used AI?** Yes / No `Yes`

### S1-08 — API reaches Postgres (Must)

- **Status:** `Done`
- **PR / commit:** `8c49ff3 make sure API reaches Postgres`
- **Demonstration:**
  1. **Do this:** With Compose up, open API logs (`docker compose logs api`) and/or hit a healthcheck that talks to Postgres if you already have one. Confirm the connection string host inside Compose is the service name `db`, not `localhost`.
  2. **Capture:** Screenshot of logs or health output that proves the API reached Postgres.
  3. **Must show:** Evidence the API talks to host `db` (successful connect message, healthcheck pass, or equivalent)—not a connection refused to the wrong host.
  4. **Must not show:** Full `DATABASE_URL` with real passwords; redact credentials.
  5. **Save as:** `docs/reports/images/sprint-01/s1-08-api-db.png`
  6. **Caption (1–2 sentences):** `A combined screencap of a log given by Docker compose config command and a health check by Docker compose ps.`
- **Used AI?** Yes / No `Yes`

### S1-09 — Vite React TypeScript scaffold (Must)

- **Status:** `Done`
- **PR / commit:** `5ef124d S1-09 Vite/React/Typescript scaffold added`
- **Demonstration:**
  1. **Do this:** Start the frontend (`npm run dev` in `frontend/` or via Compose if `web` already exists). Open the printed localhost URL in a browser.
  2. **Capture:** Screenshot of the browser showing the default Vite/React app shell.
  3. **Must show:** Browser address bar with the frontend URL and the running React/Vite page (not a blank error page).
  4. **Must not show:** API tokens or `.env` panels.
  5. **Save as:** `docs/reports/images/sprint-01/s1-09-frontend.png`
  6. **Caption (1–2 sentences):** `A screencap of the default Vite page running, with URL visible.`
- **Used AI?** Yes / No `No`

### S1-10 — Router and placeholder home (Must)

- **Status:** `Done`
- **PR / commit:** `2fb6a73 S1-10 Router and placeholder home added`
- **Demonstration:**
  1. **Do this:** With the frontend running, open the home route (usually `/`). Confirm your placeholder home content is what appears (not only the stock Vite counter if you replaced it).
  2. **Capture:** Screenshot of the home page including the URL bar.
  3. **Must show:** Placeholder home content and the route URL.
  4. **Must not show:** Secrets or unrelated authenticated data (none expected yet).
  5. **Save as:** `docs/reports/images/sprint-01/s1-10-home.png`
  6. **Caption (1–2 sentences):** `A screencap of the home route showing h1, h2, and p elements + URL bar.`
- **Used AI?** Yes / No `No`

### S1-11 — API base URL and health indicator (Should)

- **Status:** `Not done. Ran out of time.`
- **PR / commit:**
- **Demonstration:** (only if you did this ticket)
  1. **Do this:** Open the home page with API and frontend running. Trigger or wait for the health fetch so the UI shows API status (and/or the configured base URL if you display it).
  2. **Capture:** Screenshot of the home page after the health indicator updates.
  3. **Must show:** Visible API health status (healthy/unhealthy or equivalent) on the home page; include the base URL on screen if your UI shows it.
  4. **Must not show:** Bearer tokens or `.env` files.
  5. **Save as:** `docs/reports/images/sprint-01/s1-11-health-ui.png`
  6. **Caption (1–2 sentences):**
- **Used AI?** Yes / No

### S1-12 — Web service in Compose (Must)

- **Status:** `Done`
- **PR / commit:** `6a41762 Frontend web service in Compose added`
- **Demonstration:**
  1. **Do this:** Run `docker compose up --build` so `db`, `api`, and `web` start. Open the frontend URL published by Compose (see your README / `.env` ports, often `http://localhost:5173`).
  2. **Capture:** One screenshot of `docker compose ps` (or Docker UI) showing all three services, and one of the frontend loaded from that URL—or a single collage if both fit.
  3. **Must show:** `db`, `api`, and `web` running; browser showing the frontend from the Compose-published URL.
  4. **Must not show:** Secrets from env files in the terminal scrollback.
  5. **Save as:** `docs/reports/images/sprint-01/s1-12-compose-web.png`
  6. **Caption (1–2 sentences):** `A screencap combo of docker compose ps view, showing api, db and web running, plus a view of browser at http://localhost:5173.`
- **Used AI?** Yes / No `Yes`

### S1-13 — Root README (Must)

- **Status:** `Done`
- **PR / commit:** `3145997 S1-13 Root readme updated - previous contained old info`
- **Demonstration:**
  1. **Do this:** Open the root `README.md` in the editor or on your Git host.
  2. **Capture:** Screenshot of the section that covers prerequisites, `.env`, Compose, and the URL / demo-path table.
  3. **Must show:** Clone → `.env` → Compose (or equivalent) steps and a table or list of service URLs a classmate can follow.
  4. **Must not show:** Real passwords committed in the README.
  5. **Save as:** `docs/reports/images/sprint-01/s1-13-readme.png`
  6. **Caption (1–2 sentences):** `A screencap of the readme file, including prerequisites, .env, Compose and the URL/demo path list.`
- **Used AI?** Yes / No `No`

### Stretch (only if you did them)

For each stretch below that you completed: Status, PR / commit, Used AI? Add Demonstration only where steps are listed.

#### S1-S1 — DB-aware health (if done)

- **Status:** `Not done`
- **PR / commit:**
- **Demonstration:**
  1. **Do this:** With Compose up and Postgres reachable, open `http://localhost:8000/health/db` (or your documented path).
  2. **Capture:** Screenshot of the JSON response.
  3. **Must show:** Successful JSON indicating DB connectivity (not only process liveness).
  4. **Must not show:** Connection strings with passwords.
  5. **Save as:** `docs/reports/images/sprint-01/s1-s1-health-db.png`
  6. **Caption (1–2 sentences):**
- **Used AI?** Yes / No

#### S1-S2 — Multi-stage API image (if done)

- **Status:** `Not done`
- **PR / commit:**
- **Used AI?** Yes / No

#### S1-S3 — Smoke CI (if done)

- **Status:** `Not done`
- **PR / commit:**
- **Demonstration:**
  1. **Do this:** Open the CI run on your Git host for the workflow that smoke-tests the API (or installs and runs a documented check).
  2. **Capture:** Screenshot of a green / successful job.
  3. **Must show:** Workflow name and success status for the smoke job.
  4. **Must not show:** Secrets in logs.
  5. **Save as:** `docs/reports/images/sprint-01/s1-s3-ci.png`
  6. **Caption (1–2 sentences):**
- **Used AI?** Yes / No

## How we worked

Sprint 1 is **two weeks**.

- **Week 1** (backend shell & Compose):
- **Week 2** (frontend shell & README):
- Who did what:
- One blocker and how you unblocked it:

## Decisions

Two to four technical choices with why (for example Vite in Compose vs build + nginx).

1. Vite in Compose vs. build + nginx: because at this point Vite felt way more comfortable and straightforward. I am definitely interested in taking a look at build + nginx later, but at right now this solution felt more approachable.
2. BrowserRouter in App.tsx vs. in main.tsx. It was outlined in the ticket S1-10 that the BrowserRouter should be in either frontend/src/main.tsx or App.tsx. I decided to put it in App.tsx, since I feel main.tsx is more for just compiling different elements together, while App.tsx is more like "the engine".

## What we learned

Note what you actually used. Tools this sprint: Git / monorepo, Python venv + `requirements.txt`, FastAPI + Uvicorn, OpenAPI (`/docs`), Pydantic / pydantic-settings, PostgreSQL, Docker Compose, React + TypeScript + Vite, React Router, `.env` / `.env.example`.

- What clicked: It was fun starting to build from the ground up and seeing the application slowly start to grow. Writing the README for ticket S1-13 was really rewarding: I haven't really thought of readmes before so this was sort of an eye-opener.

- One thing you would do differently: This sprint was really rough, due to me thinking for some reason that the deadline was 13.9. and not 6.9., and having to do everything in half a week. So one thing I would definitely do differently is making sure I am absolutely sure about the deadlines.

## Carry-over

Due to my scheduling errors, S1-11 was left undone and will have to be done early in sprint 2.


## AI usage (sprint-level reflection)

Mark **Used AI?** under each ticket above (`Yes` / `No`). Do **not** write per-ticket reflections there.

Here, cover your **overall** AI use during this sprint (Cursor, ChatGPT, Copilot, local coding assistants, etc.). Product Insights via Ollama in Sprint 5 does **not** count unless you also used an AI assistant to write code.

If you marked **No** on every ticket, write a short note that you did not use AI coding assistants this sprint (you may still answer verification / independence questions briefly).

- **Where AI helped most this sprint** (themes, ticket IDs, or areas—not a ticket-by-ticket dump):
I used AI more than I would've liked during this sprint. I mainly used it for explaining some of the concepts that I felt (in my panicked state) were hard to grasp, but there were some places it did write some code too. I had immense difficulties wrapping my head around Docker Compose (S1-07 and S1-12), so I leaned heavily on ChatGPT to figure out what to put in docker-compose.yml and Dockerfiles.

- **What I typically accepted from AI suggestions:**
I take everything the AI says with a grain of salt, but here I did tend to trust it especially when I asked it to summarise something from a pre-existing source. Docker-compose.yml and Dockerfiles I accepted but did go through with a comb.

- **What I typically rejected or reworked, and why:**
Sometimes AI does suggest something kinda wild, which requires taking a closer look or at least asking it for the source. In sprint 1's case, I did not reject a that much though.

- **How I verified AI-assisted work** (tests, `/docs`, manual demos, reviews):
Especially when using AI-generated code, tried to find similar snippets from manuals or discussions. In general tried to double-check from manuals when possible.

- **What I can now explain or do independently** that I relied on AI for earlier:
Now have a clearer understanding of how data flows between different modules and which communicates with which.

- **Anything I would do differently with AI next sprint:**
Use it less overall, and when using it, use it mostly for explaining bits I need additional handholding with.

Do not paste secrets, full JWTs, or `.env` values.

