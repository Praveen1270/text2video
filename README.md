# Text2Video - AI-Powered Video Generator

A modern web application that generates educational videos from text topics using AI. The application uses Gemini AI for script generation, Stable Diffusion for image creation, and ElevenLabs for voice-over narration.

## Features

- 🎬 **AI Video Generation**: Create educational videos from any topic
- 🤖 **Gemini AI Integration**: Intelligent script and scene generation
- 🎨 **Stable Diffusion**: High-quality AI-generated images
- 🎤 **ElevenLabs Voice**: Professional voice-over narration
- 🎛️ **Customizable Settings**: Choose voice, resolution, and more
- 📱 **Modern UI**: Beautiful, responsive web interface
- ⚡ **Real-time Progress**: Live updates during video generation

## Tech Stack

### Backend
- **Python 3.8+**
- **Flask**: Web API framework
- **Google Generative AI**: Script generation
- **Stability AI**: Image generation
- **ElevenLabs**: Voice synthesis
- **MoviePy**: Video assembly

### Frontend
- **React 18** with TypeScript
- **Tailwind CSS**: Modern styling
- **Lucide React**: Beautiful icons
- **Axios**: HTTP client

## Prerequisites

- Python 3.8 or higher
- Node.js 16 or higher
- API keys for:
  - Google Generative AI (Gemini)
  - Stability AI
  - ElevenLabs

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd text2video
```

### 2. Backend Setup

```bash
cd Backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
```

### 3. Configure Environment Variables

Edit the `.env` file in the Backend directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
STABILITY_API_KEY=your_stability_api_key_here
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
ELEVENLABS_VOICE_ID=21m00Tcm4TlvDq8ikWAM
```

### 4. Frontend Setup

```bash
cd Frontend

# Install dependencies
npm install

# Start development server
npm start
```

### 5. Start the Backend

```bash
cd Backend

# Activate virtual environment (if not already activated)
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Start the Flask API
python api.py
```

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000

## Usage

1. **Enter a Topic**: Type any educational topic (e.g., "How do electric circuits work?")
2. **Configure Settings**: Choose voice, resolution, and other options
3. **Generate Video**: Click "Generate Video" to start the process
4. **Monitor Progress**: Watch real-time progress updates
5. **Download Result**: Download your generated video when complete

## API Endpoints

### Video Generation
- `POST /api/generate-video`: Start video generation
- `GET /api/status/<task_id>`: Get generation status
- `GET /download/<task_id>`: Download generated video

### Script Generation
- `POST /api/generate-script`: Generate script for a topic

### Utilities
- `GET /api/voices`: Get available voice options
- `GET /api/health`: Health check

## Project Structure

```
text2video/
├── Backend/
│   ├── api.py              # Flask API server
│   ├── main.py             # Video generation logic
│   ├── config.py           # Configuration settings
│   ├── prompts.py          # AI prompts
│   ├── requirements.txt    # Python dependencies
│   ├── llm/
│   │   └── gemini_client.py
│   ├── image/
│   │   └── stability_client.py
│   ├── tts/
│   │   └── eleven_client.py
│   └── assemble/
│       └── video_maker.py
├── Frontend/
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── services/       # API services
│   │   ├── types/          # TypeScript types
│   │   └── App.tsx         # Main app component
│   ├── public/
│   └── package.json
└── README.md
```

## Troubleshooting

### Common Issues

1. **API Key Errors**: Ensure all API keys are correctly set in the `.env` file
2. **Port Conflicts**: Make sure ports 3000 and 5000 are available
3. **Dependencies**: Run `pip install -r requirements.txt` and `npm install` if you encounter missing dependencies
4. **Virtual Environment**: Always activate the Python virtual environment before running the backend

### Getting API Keys

- **Google Generative AI**: Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
- **Stability AI**: Visit [Stability AI Platform](https://platform.stability.ai/)
- **ElevenLabs**: Visit [ElevenLabs](https://elevenlabs.io/)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter any issues or have questions, please open an issue on the GitHub repository.
