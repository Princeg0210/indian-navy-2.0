import sys
import os
from pathlib import Path

# Add the backend directory to sys.path so that internal imports 
# (like 'from routes.vessels import ...') work correctly.
backend_dir = str(Path(__file__).parent / "indian" / "backend")
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

# Import the FastAPI app instance from the backend main file
from indian.backend.main import app

# This allows Vercel to find the 'app' variable at the root level
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
