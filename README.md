# 🚢 Indian Navy — Maritime Domain Awareness (MDA) System

An AI-powered Maritime Domain Awareness platform for real-time vessel tracking, multi-sensor data fusion, and automated anomaly detection (Dark vessels, Ship-to-Ship transfers, position spoofing, route deviation, and loitering).

[![Quick Start Video](https://img.shields.io/badge/▶_Quick_Start-Watch_Video-blue?style=for-the-badge&logo=youtube)](https://youtu.be/YOUR_VIDEO_ID_HERE)
[![License](https://img.shields.io/badge/License-Restricted-red?style=for-the-badge)](.)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![React](https://img.shields.io/badge/React-18-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://react.dev)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)

---

## 📸 Screenshots

### 🔐 Lock Screen — Tactical Authentication

<p align="center">
  <img src="docs/screenshots/lockscreen.png" alt="Lock Screen — Tactical Authentication" width="600"/>
</p>

> The system is protected with a military-grade lock screen. Operators must enter their clearance passcode before accessing the tactical dashboard.

### 🗺️ Tactical Dashboard — Real-Time Maritime Map

<p align="center">
  <img src="docs/screenshots/dashboard.png" alt="Tactical Dashboard — Real-Time Map View" width="800"/>
</p>

> The main dashboard provides a live Leaflet map with vessel markers, risk heat overlays, anomaly alerts, and multi-layer tactical information. Click any vessel to inspect its track history, risk profile, and ML anomaly scores.

---

## 🏗️ System Architecture

- **Backend**: FastAPI (Python 3.11+) with WebSocket live stream support
- **Frontend**: React 18, Vite, Leaflet Maps, Lucide Icons, Recharts
- **ML Engine**: DBSCAN clustering, LSTM Autoencoders, Extended Kalman Filtering (EKF)
- **Deployment**: Integrated static asset serving on FastAPI port `8000` or Docker containerization

```
┌──────────────────────────────────────────────────────┐
│                   React Frontend                     │
│   Leaflet Map ─ Alert Sidebar ─ Vessel Detail Panel  │
│              WebSocket ↕ REST API calls              │
├──────────────────────────────────────────────────────┤
│                 FastAPI Backend (:8000)               │
│ ┌──────────┐  ┌──────────────┐  ┌──────────────────┐│
│ │ Vessels   │  │  Anomalies   │  │  Risk Profiles   ││
│ │ Router    │  │  Router      │  │  Router          ││
│ └─────┬────┘  └──────┬───────┘  └────────┬─────────┘│
│       └───────────┬──┘───────────────────┘           │
│           Detection Service (ML Pipeline)            │
│  ┌────────────┐ ┌────────────┐ ┌────────────────┐   │
│  │  DBSCAN    │ │ LSTM Auto- │ │ Extended Kalman│   │
│  │ Clustering │ │  encoder   │ │    Filter      │   │
│  └────────────┘ └────────────┘ └────────────────┘   │
├──────────────────────────────────────────────────────┤
│              AIS Simulator / Live Bridge             │
│         (Synthetic data + WebSocket streaming)       │
└──────────────────────────────────────────────────────┘
```

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
- **Default Clearance Passcode**: `Create a Request / Contact - gprincegupta0210@gmail.com)*
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

### Swagger API Tag Groups

The API documentation at `/docs` organizes all endpoints into the following logical groups:

| Tag | Description |
|-----|-------------|
| **Vessels** | Vessel registry, track history, ship control, convoy radar, and comms |
| **Anomaly Detection** | ML-powered anomaly alerts, stats, and detection pipeline trigger |
| **Risk Profiles** | Detailed per-vessel risk analysis with ML signal breakdown |
| **Live Feed** | Real-time paginated AIS data stream |
| **Health** | System health check and operational status |

---

## 📁 Repository Structure

```
indian-navy-2.0/
├── README.md               # Project guide and startup instructions
├── DEPLOYMENT.md           # Strategic deployment & VPS production guide
├── CONTRIBUTING.md         # Contribution guidelines (see below)
├── main.py                 # Root application launcher
├── run_local.sh            # One-click local deployment script
├── run_mda.sh              # One-click Docker deployment script
├── start_backend.sh        # Backend process launcher script
├── requirements.txt        # Python backend dependencies
├── Dockerfile              # Container definition (Multi-stage build)
├── docker-compose.yml      # Docker stack service configuration
├── docs/
│   └── screenshots/        # UI screenshots for documentation
└── indian/
    ├── backend/            # FastAPI app, routing, and WebSocket service
    │   ├── main.py         # App entry point + WebSocket manager
    │   ├── routes/
    │   │   ├── vessels.py  # /api/vessels/* endpoints
    │   │   ├── anomalies.py# /api/anomalies/* endpoints
    │   │   └── risk.py     # /api/risk/* endpoints
    │   └── services/       # Detection service, live bridge
    ├── frontend/           # React tactical dashboard source code
    │   ├── src/
    │   │   ├── components/ # React components (Map, AlertSidebar, etc.)
    │   │   ├── App.jsx     # Root React component
    │   │   └── index.css   # Global styles
    │   └── package.json
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
- **Docker container not starting**:
  ```bash
  docker logs -f indian-navy-mda
  ```
- **Frontend assets not found (404 on `/`)**:
  Ensure the frontend has been built before starting the backend:
  ```bash
  cd indian/frontend && npm run build && cd ../..
  ```

---

## 🤝 Contributing

We welcome contributions! Please follow the guidelines below.

### Getting Started

1. **Fork** this repository.
2. **Clone** your fork:
   ```bash
   git clone https://github.com/<your-username>/indian-navy-2.0.git
   cd indian-navy-2.0
   ```
3. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   cd indian/frontend && npm install && cd ../..
   ```

### Code Style

| Layer | Formatter | Linter | Config |
|-------|-----------|--------|--------|
| **Python Backend** | [Black](https://black.readthedocs.io/) | [Flake8](https://flake8.pycqa.org/) | `pyproject.toml` |
| **React Frontend** | [Prettier](https://prettier.io/) | [ESLint](https://eslint.org/) | `.eslintrc` / `.prettierrc` |

### Running Tests

```bash
# Backend tests
cd indian/backend
pytest -v

# Frontend tests
cd indian/frontend
npm test
```

### Commit Convention

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add vessel convoy radar endpoint
fix: resolve WebSocket disconnect on idle timeout
docs: update README with screenshots
chore: bump FastAPI to 0.110
```

### Pull Request Process

1. Ensure your code passes **linting** and **tests**.
2. Update documentation if you add or change endpoints / components.
3. Add screenshots for any UI changes.
4. Submit a PR with a clear title and description.
5. At least one maintainer review is required before merging.

### Reporting Issues

- Use GitHub Issues with the appropriate label (`bug`, `enhancement`, `documentation`).
- Include steps to reproduce, expected vs. actual behavior, and relevant logs.

---

## 📜 License

This project is classified as **RESTRICTED** under the Government of India. Unauthorized distribution or deployment is prohibited.

---

*Classification: RESTRICTED — Strategic Asset Deployment Documentation*
