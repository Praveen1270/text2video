@echo off
echo Switching from minimal API to full API...
echo.

echo Stopping any running API servers...
taskkill /f /im python.exe 2>nul
timeout /t 2 /nobreak >nul

echo.
echo Starting Full API Server (api.py)...
echo This will use real AI if you have API keys configured.
echo.
echo If you get errors about missing API keys, you can:
echo 1. Add your API keys to Backend/.env file
echo 2. Or continue using minimal_api.py for testing
echo.

start "Full API Server" cmd /k "cd Backend && py api.py"

echo.
echo Full API server is starting...
echo Check the new terminal window for any error messages.
echo.
echo If you see API key errors, you can:
echo - Press Ctrl+C to stop the server
echo - Run: py Backend/minimal_api.py (for testing without API keys)
echo.
pause
