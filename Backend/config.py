import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()


ROOT = Path(__file__).parent
OUTPUT_DIR = ROOT / "outputs"
IMAGES_DIR = OUTPUT_DIR / "images"
AUDIO_DIR = OUTPUT_DIR / "audio"
VIDEO_DIR = OUTPUT_DIR / "video"
TMP_DIR = OUTPUT_DIR / "tmp"


for d in [OUTPUT_DIR, IMAGES_DIR, AUDIO_DIR, VIDEO_DIR, TMP_DIR]:
    d.mkdir(parents=True, exist_ok=True)


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
STABILITY_API_KEY = os.getenv("STABILITY_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
ELEVENLABS_VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID", "21m00Tcm4TlvDq8ikWAM")


DEFAULT_FPS = 30
DEFAULT_RES = (1920, 1080)
DEFAULT_ASPECT = "16:9"