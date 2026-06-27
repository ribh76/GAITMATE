# GaitMate Demo

GaitMate is a local hackathon demo for an ankle biosensor dashboard. The backend reads CSV sensor data and exposes JSON endpoints; the frontend is plain HTML, CSS, and JavaScript.

## Run Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Backend URL: http://127.0.0.1:5000

## Run Frontend

```bash
cd frontend
python -m http.server 5173
```

Frontend URL: http://127.0.0.1:5173

## API

- `GET /api/health`
- `GET /api/sensor/all`
- `GET /api/sensor/latest`
- `GET /api/sensor/time/<time_value>`
- `GET /api/sensor/ligaments/latest`
- `GET /api/risk/latest`



## Run steps (for developers)

- Open two terminals, one for frontend, one for backend. 
- In frontend terminal, run 'cd frontend' 
- In backend terminal, run 'cd backend'
- TO RUN: 
- In backend terminal: 'python app.py'
- In frontend terminal: 'python3 -m http.server 5173 --bind 127.0.0.1'