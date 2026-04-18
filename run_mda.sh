#!/bin/bash
# 🚢 Indian Navy - MDA Deployment Script
# Automates the build and launch of the containerized stack.

echo "--------------------------------------------------------"
echo "🚀 INITIALIZING FULL-FLEDGE DEPLOYMENT: Indian Navy NMDA"
echo "--------------------------------------------------------"

# 1. Check for Docker
if ! [ -x "$(command -v docker)" ]; then
  echo "❌ Error: Docker is not installed and is required for deployment."
  exit 1
fi

# 2. Build and Up
echo "📦 Building tactical containerized stack..."
if docker compose version > /dev/null 2>&1; then
  docker compose up --build -d
else
  docker-compose up --build -d
fi

# 3. Wait for Health
echo "🛡️  Checking system status..."
ATTEMPT=0
MAX=12
while [ $ATTEMPT -lt $MAX ]; do
  if curl -s http://localhost:8000/api/anomalies/stats > /dev/null; then
    echo "✅ Success! Deployment complete."
    echo "🌐 Access Dashboard at: http://localhost:8000"
    exit 0
  fi
  echo "📡 Waiting for satellite systems to initialize... ($ATTEMPT/$MAX)"
  sleep 5
  ATTEMPT=$((ATTEMPT+1))
done

echo "⚠️ System taking longer than expected to initialize."
echo "📜 Check status with: docker logs -f indian-navy-mda"
