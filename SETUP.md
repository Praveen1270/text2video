# Quick Setup Guide

## Prerequisites
- Python 3.8+
- Node.js 16+
- API keys for Gemini, Stability AI, and ElevenLabs

## Backend Setup

1. **Navigate to Backend directory:**
   ```bash
   cd Backend
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment:**
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Create .env file:**
   Create a `.env` file in the Backend directory with:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   STABILITY_API_KEY=your_stability_api_key_here
   ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
   ELEVENLABS_VOICE_ID=21m00Tcm4TlvDq8ikWAM
   ```

6. **Start backend:**
   ```bash
   python api.py
   ```

## Frontend Setup

1. **Navigate to Frontend directory:**
   ```bash
   cd Frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start frontend:**
   ```bash
   npm start
   ```

## Quick Start (Windows)

1. **Double-click `start.bat`** to start both services automatically

## Quick Start (macOS/Linux)

1. **Make script executable:**
   ```bash
   chmod +x start.sh
   ```

2. **Run the script:**
   ```bash
   ./start.sh
   ```

## Access the Application

- Frontend: http://localhost:3000
- Backend API: http://localhost:5000

## Getting API Keys

- **Google Generative AI**: https://makersuite.google.com/app/apikey
- **Stability AI**: https://platform.stability.ai/
- **ElevenLabs**: https://elevenlabs.io/
