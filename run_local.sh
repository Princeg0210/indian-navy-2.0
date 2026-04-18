#!/bin/bash
# 🚢 Indian Navy - MDA Local Deployment Script (No Docker)
# Automates the build and launch directly on your Mac.

echo "--------------------------------------------------------"
echo "🚀 INITIALIZING LOCAL DEPLOYMENT: Indian Navy NMDA"
echo "--------------------------------------------------------"

# Change to the directory where this script is located
cd "$(dirname "$0")"

echo "📦 1/3: Installing Backend Dependencies..."
python3 -m pip install -r requirements.txt --quiet

echo "🏗️  2/3: Building Frontend tactical dashboard..."
cd indian/frontend
npm install --silent
npm run build
cd ../..

echo "🌐 3/3: Starting System on Port 8000..."
cd indian/backend

# Kill any existing process on port 8000 to free it up
if lsof -i :8000 > /dev/null; then
  echo "⚠️ Port 8000 is occupied. Terminating old process..."
  kill -9 $(lsof -t -i :8000)
fi

# Export production environment variables
export SYSTEM_STATUS="PRODUCTION"
export CLASSIFICATION="RESTRICTED"

# Start the ASGI server
python3 main.py
