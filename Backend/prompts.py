SCENES_PROMPT = """
You are a video scriptwriter. Create a concise educational explainer about the TOPIC.
Constraints:
- Audience: beginners
- Duration: ~60 seconds narration (about 120-150 words)
- Output format (JSON):
{
"title": "string",
"script": "full voiceover text in natural, engaging tone",
"scenes": [
{"caption": "on-screen caption (<=10 words)", "image_prompt": "detailed prompt for image generator", "voice": "sentence/paragraph for this scene"},
... 4-6 scenes total ...
]
}
Avoid special characters that would break JSON. Use plain ASCII.
TOPIC: """.strip()