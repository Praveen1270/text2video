@echo off
echo Starting Text2Video Application...
echo.

echo Starting Backend API...
cd Backend
start "Backend API" cmd /k "venv\Scripts\activate && python api.py"

echo.
echo Starting Frontend...
cd ..\Frontend
start "Frontend" cmd /k "npm start"

echo.
echo Application is starting...
echo Frontend will be available at: http://localhost:3000
echo Backend API will be available at: http://localhost:5000
echo.
echo Press any key to exit this window...
pause > nul
