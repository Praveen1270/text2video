# Text2Video Application - Quick Start Guide

## 🚀 Current Status
Your Text2Video application is now running with a working frontend and backend!

### Backend API (Port 8080)
- ✅ Flask server running on http://localhost:8080
- ✅ All API endpoints working
- ✅ Mock video generation for testing
- ✅ Script generation working

### Frontend (Port 3000)
- ✅ React application running on http://localhost:3000
- ✅ Connected to backend API
- ✅ Modern UI with progress tracking
- ✅ Video download functionality

## 🎯 How to Use

1. **Open your browser** and go to http://localhost:3000
2. **Enter a topic** (e.g., "artificial intelligence", "solar system", "cooking")
3. **Click "Generate Video"** or use one of the suggested topics
4. **Watch the progress** as the app simulates:
   - Script generation with Gemini AI
   - Image generation with Stable Diffusion
   - Voice-over generation with ElevenLabs
   - Video assembly
5. **Download the video** when complete

## 🔧 Current Implementation

### What's Working:
- ✅ Frontend UI with modern design
- ✅ Backend API with all endpoints
- ✅ Progress tracking and status updates
- ✅ Script generation (mock data)
- ✅ Video download (placeholder files)
- ✅ Voice selection
- ✅ Video settings

### What's Mocked (for testing):
- Script generation returns sample data
- Video generation creates placeholder files
- Progress simulation (not real AI processing)

## 🚀 Next Steps

To enable real AI video generation, you'll need to:

1. **Get API Keys**:
   - Google Gemini API key
   - Stability AI API key (for images)
   - ElevenLabs API key (for voice)

2. **Create a .env file** in the Backend folder:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   STABILITY_API_KEY=your_stability_api_key_here
   ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
   ```

3. **Switch to full API**: Replace `minimal_api.py` with the full `api.py` implementation

## 🛠️ Troubleshooting

### If the frontend shows connection errors:
- Make sure the backend is running on port 8080
- Check that both servers are started

### If video download fails:
- The current implementation creates placeholder files
- Real videos will be generated when you add API keys

### To restart the application:
- Use the `start_app.bat` file for easy startup
- Or manually start both servers in separate terminals

## 📁 File Structure
```
text2video/
├── Backend/
│   ├── minimal_api.py      # Current working API
│   ├── api.py              # Full implementation (needs API keys)
│   └── ...
├── Frontend/
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── services/       # API calls
│   │   └── types/          # TypeScript types
│   └── ...
└── start_app.bat           # Easy startup script
```

## 🎉 Enjoy Your AI Video Generator!

The application is fully functional for testing and demonstration. Add your API keys to enable real AI-powered video generation!
