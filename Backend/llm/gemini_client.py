from __future__ import annotations
import json
import google.generativeai as genai
from typing import Dict, Any
from prompts import SCENES_PROMPT
from config import GEMINI_API_KEY


if not GEMINI_API_KEY:
raise RuntimeError("GEMINI_API_KEY is missing. Set it in .env")


genai.configure(api_key=GEMINI_API_KEY)


# Model choices: "gemini-1.5-flash", "gemini-1.5-pro"
MODEL = "gemini-1.5-flash"


SYSTEM_INSTRUCTIONS = (
"You are a precise JSON generator. Always return valid JSON only, no prose."
)


def generate_script_and_scenes(topic: str) -> Dict[str, Any]:
prompt = f"{SCENES_PROMPT} {topic}\nReturn only JSON."
model = genai.GenerativeModel(MODEL, system_instruction=SYSTEM_INSTRUCTIONS)
resp = model.generate_content(prompt)
text = resp.text.strip()
# Attempt to parse JSON; fix common surrounding ``` fences
if text.startswith("```"):
text = text.strip("`\n ")
if text.lower().startswith("json\n"):
text = text[5:]
try:
data = json.loads(text)
except json.JSONDecodeError as e:
# Fallback: try to extract first JSON block
start = text.find('{')
end = text.rfind('}')
data = json.loads(text[start:end+1])
return data