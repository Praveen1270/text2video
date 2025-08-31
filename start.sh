#!/bin/bash

echo "Starting Text2Video Application..."
echo

echo "Starting Backend API..."
cd Backend
source venv/bin/activate
python api.py &
BACKEND_PID=$!

echo
echo "Starting Frontend..."
cd ../Frontend
npm start &
FRONTEND_PID=$!

echo
echo "Application is starting..."
echo "Frontend will be available at: http://localhost:3000"
echo "Backend API will be available at: http://localhost:5000"
echo
echo "Press Ctrl+C to stop both services..."

# Wait for user to stop
trap "echo 'Stopping services...'; kill $BACKEND_PID $FRONTEND_PID; exit" INT
wait
