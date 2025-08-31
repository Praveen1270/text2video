# Switching from Minimal API to Full API

## 🔄 **What's Changed**

I've successfully updated your `api.py` file to:
- ✅ Use dictionary-based task storage (no more AttributeError)
- ✅ Run on port 8080 (same as minimal API)
- ✅ Include all the same endpoints
- ✅ Support real AI video generation

## 🚀 **How to Switch**

### Option 1: Use the Switch Script
```bash
# Run this batch file
switch_to_full_api.bat
```

### Option 2: Manual Switch
```bash
# Stop current server (Ctrl+C in the terminal)
# Then run:
py Backend/api.py
```

## 🔑 **API Keys Required**

The full API requires these API keys in `Backend/.env`:

```
GEMINI_API_KEY=your_gemini_api_key_here
STABILITY_API_KEY=your_stability_api_key_here
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
```

### Get API Keys:
- **Google Gemini**: https://makersuite.google.com/app/apikey
- **Stability AI**: https://platform.stability.ai/
- **ElevenLabs**: https://elevenlabs.io/

## ⚠️ **What Happens Without API Keys**

If you don't have API keys, you'll see errors like:
```
RuntimeError: GEMINI_API_KEY is missing. Set it in .env
```

### Solutions:
1. **Add API keys** to `Backend/.env` file
2. **Continue using minimal_api.py** for testing without keys
3. **Get free API keys** from the providers above

## 🎯 **Benefits of Full API**

### ✅ Real AI Generation:
- **Gemini AI**: Generates actual scripts based on topics
- **Stability AI**: Creates real images for each scene
- **ElevenLabs**: Produces professional voice-over
- **MoviePy**: Assembles actual MP4 video files

### ✅ Real Video Output:
- Actual MP4 files instead of HTML placeholders
- Professional voice narration
- AI-generated images
- Proper video assembly

## 🔧 **Testing the Switch**

1. **Start the full API**: `py Backend/api.py`
2. **Check for errors**: Look for API key errors
3. **Test the frontend**: http://localhost:3000
4. **Generate a video**: Enter a topic and watch real AI generation

## 🛠️ **Troubleshooting**

### If you get API key errors:
```bash
# Option 1: Add API keys to .env file
# Option 2: Go back to minimal API
py Backend/minimal_api.py
```

### If the server won't start:
```bash
# Check if port 8080 is in use
netstat -ano | findstr :8080
# Kill the process if needed
taskkill /f /pid <process_id>
```

## 📁 **File Structure After Switch**

```
Backend/
├── api.py              # Full API (real AI generation)
├── minimal_api.py      # Minimal API (testing only)
├── .env                # API keys (create this)
└── outputs/
    └── video/          # Real MP4 files will be here
```

## 🎉 **Ready to Switch?**

Your full API is ready! Just run:
```bash
py Backend/api.py
```

The frontend will work exactly the same, but now you'll get real AI-generated videos! 🎬✨
