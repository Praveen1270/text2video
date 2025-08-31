@echo off
echo Starting Text2Video Application...
echo.

echo Starting Backend API Server...
start "Backend API" cmd /k "cd Backend && py minimal_api.py"

echo Waiting 3 seconds for backend to start...
timeout /t 3 /nobreak > nul

echo Starting Frontend Development Server...
start "Frontend" cmd /k "cd Frontend && npm start"

echo.
echo Application is starting up!
echo Backend API: http://localhost:8080
echo Frontend: http://localhost:3000
echo.
echo Press any key to exit this launcher...
pause > nul
