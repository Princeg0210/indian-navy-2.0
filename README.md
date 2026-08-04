# 🚢 Indian Navy — Maritime Domain Awareness (MDA) System

An AI-powered Maritime Domain Awareness platform for real-time vessel tracking, multi-sensor data fusion, and automated anomaly detection (Dark vessels, Ship-to-Ship transfers, position spoofing, route deviation, and loitering).

---

## 🏗️ System Architecture

- **Backend**: FastAPI (Python 3.11+) with WebSocket live stream support
- **Frontend**: React 18, Vite, Leaflet Maps, Lucide Icons, Recharts
- **ML Engine**: DBSCAN clustering, LSTM Autoencoders, Extended Kalman Filtering (EKF)
- **Deployment**: Integrated static asset serving on FastAPI port `8000` or Docker containerization

---

## 📋 Prerequisites

Before running the project locally, ensure you have installed:
- **Python**: `3.10` or higher (`python3 --version`)
- **Node.js**: `v18` or higher (`node -v` & `npm -v`)
- **Docker** *(Optional)*: If using containerized deployment

---

## 🔒 Security & Access Control

The site is protected with a tactical **Password Lock Screen** on startup.
- **Username**: *None (Password only)*
- **Default Clearance Passcode**: `NAVY2026` *(Also accepts `NAVY` or `1234`)*
- **Session Locking**: Operators can click the red **Lock** icon in the top-right header at any time to re-lock the system terminal.

---

## 🚀 Quick Start (Local Setup)

### Option 1: Automated Script (Recommended)

Run the local launch script directly from the project root:

```bash
bash run_local.sh
```

This script automatically:
1. Installs Python dependencies (`requirements.txt`).
2. Builds the React frontend tactical dashboard (`indian/frontend/dist`).
3. Clears port `8000` if occupied.
4. Starts the ASGI server at `http://localhost:8000`.

---

### Option 2: Step-by-Step Manual Start

#### Step 1: Install Python Backend Dependencies
```bash
pip install -r requirements.txt
```

#### Step 2: Build the Frontend
```bash
cd indian/frontend
npm install
npm run build
cd ../..
```

#### Step 3: Launch the Unified Server
```bash
python3 main.py
```
*(Or use `bash start_backend.sh`)*

---

## 🐳 Docker Containerized Deployment

To deploy using Docker Compose:

```bash
bash run_mda.sh
```
or manually:
```bash
docker compose up --build -d
```

---

## 🌐 Access Points & API Endpoints

Once the application is running, access the following endpoints in your browser:

| Interface | URL | Description |
|---|---|---|
| **Tactical Dashboard** | [http://localhost:8000](http://localhost:8000) | Main React map & vessel tracking UI |
| **API Documentation (Swagger)** | [http://localhost:8000/docs](http://localhost:8000/docs) | Interactive OpenAPI documentation |
| **ReDoc Documentation** | [http://localhost:8000/redoc](http://localhost:8000/redoc) | Alternative API spec viewer |
| **System Health Check** | [http://localhost:8000/api/health](http://localhost:8000/api/health) | Backend status & AIS stats |
| **WebSocket Live Stream** | `ws://localhost:8000/ws/live-feed` | Real-time AIS telemetry stream |

---

## 📁 Repository Structure

```
indian-navy-2.0/
├── README.md               # Project guide and startup instructions
├── DEPLOYMENT.md           # Strategic deployment & VPS production guide
├── main.py                 # Root application launcher
├── run_local.sh            # One-click local deployment script
├── run_mda.sh              # One-click Docker deployment script
├── start_backend.sh        # Backend process launcher script
├── requirements.txt        # Python backend dependencies
├── Dockerfile              # Container definition (Multi-stage build)
├── docker-compose.yml      # Docker stack service configuration
└── indian/
    ├── backend/            # FastAPI app, routing, and WebSocket service
    ├── frontend/           # React tactical dashboard source code
    ├── ml_engine/          # ML anomaly detection models & pipeline
    └── simulation/         # Synthetic AIS data generation & simulation
```

---

## 🛠️ Troubleshooting

- **Port 8000 already in use**:
  ```bash
  kill -9 $(lsof -t -i :8000)
  ```
- **Node.js lockfile issues during `npm install`**:
  ```bash
  rm -f indian/frontend/package-lock.json && cd indian/frontend && npm install
  ```

---
*Classification: RESTRICTED — Strategic Asset Deployment Documentation*
