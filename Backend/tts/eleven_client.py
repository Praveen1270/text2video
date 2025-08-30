from pathlib import Path
from typing import Optional
from elevenlabs import ElevenLabs
from config import ELEVENLABS_API_KEY, ELEVENLABS_VOICE_ID, AUDIO_DIR


if not ELEVENLABS_API_KEY:
raise RuntimeError("ELEVENLABS_API_KEY is missing. Set it in .env")


client = ElevenLabs(api_key=ELEVENLABS_API_KEY)




def synthesize_voice(script_text: str, voice_id: Optional[str] = None) -> Path:
voice = voice_id or ELEVENLABS_VOICE_ID
out_path = AUDIO_DIR / "voiceover.mp3"


# Model: elevent-labs multilingual v2 (default via SDK)
audio = client.text_to_speech.convert(
text=script_text,
voice_id=voice,
model_id="eleven_multilingual_v2",
output_format="mp3_44100_128",
)


with open(out_path, "wb") as f:
for chunk in audio:
if chunk:
f.write(chunk)
return out_path