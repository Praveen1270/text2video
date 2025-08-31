from __future__ import annotations
import json
import google.generativeai as genai
from typing import Dict, Any
from prompts import SCENES_PROMPT
from config import GEMINI_API_KEY

# Model choices: "gemini-1.5-flash", "gemini-1.5-pro"
MODEL = "gemini-1.5-flash"

SYSTEM_INSTRUCTIONS = (
    "You are a precise JSON generator. Always return valid JSON only, no prose."
)

# Check if API key is available
if not GEMINI_API_KEY:
    print("WARNING: GEMINI_API_KEY is missing. Set it in .env for real AI generation.")
    print("Using mock data instead.")
    
    def generate_script_and_scenes(topic: str) -> Dict[str, Any]:
        # Return mock data when API key is missing
        return {
            "title": f"Introduction to {topic}",
            "script": f"This is a sample script about {topic}. It provides an overview of the key concepts and important details that beginners should know.",
            "scenes": [
                {
                    "caption": f"What is {topic}?",
                    "image_prompt": f"educational diagram showing {topic}",
                    "voice": f"Let's start by understanding what {topic} is and why it's important."
                },
                {
                    "caption": "Key Concepts",
                    "image_prompt": f"visual representation of {topic} concepts",
                    "voice": "Here are the fundamental concepts you need to know."
                },
                {
                    "caption": "Real World Examples",
                    "image_prompt": f"practical examples of {topic} in use",
                    "voice": "Let's look at some real-world applications and examples."
                }
            ]
        }
else:
    # Configure Gemini for real AI generation
    genai.configure(api_key=GEMINI_API_KEY)
    
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