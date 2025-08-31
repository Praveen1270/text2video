import base64
import requests
from pathlib import Path
from typing import List
from tqdm import tqdm
from config import STABILITY_API_KEY, IMAGES_DIR, DEFAULT_RES


# Check if API key is available
if not STABILITY_API_KEY:
    print("WARNING: STABILITY_API_KEY is missing. Set it in .env for real image generation.")
    print("Using mock image generation instead.")
    
    def generate_images(prompts: List[str], out_prefix: str, size=DEFAULT_RES) -> List[Path]:
        # Return mock image paths when API key is missing
        paths = []
        for i, p in enumerate(prompts):
            # Create a placeholder image file
            out_path = IMAGES_DIR / f"{out_prefix}_{i+1:02d}.png"
            # Create a simple text file as placeholder
            with open(out_path, "w") as f:
                f.write(f"Mock image for prompt: {p}\n")
                f.write("This is a placeholder. Add STABILITY_API_KEY to .env for real images.\n")
            paths.append(out_path)
        return paths
else:
    # Configure headers for real image generation
    HEADERS = {
        "Authorization": f"Bearer {STABILITY_API_KEY}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    
    


# SDXL v1.0 text-to-image endpoint
API_URL = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"


HEADERS = {
"Authorization": f"Bearer {STABILITY_API_KEY}",
"Accept": "application/json",
"Content-Type": "application/json",
}


NEGATIVE = (
"low quality, blurry, pixelated, watermark, text, logo, extra fingers, distorted"
)




def _size_tuple_to_str(size):
    w, h = size
    return w, h




def generate_images(prompts: List[str], out_prefix: str, size=DEFAULT_RES) -> List[Path]:
    paths = []
    w, h = _size_tuple_to_str(size)
    for i, p in enumerate(tqdm(prompts, desc="Generating images")):
        payload = {
            "text_prompts": [
                {"text": p, "weight": 1.0},
                {"text": NEGATIVE, "weight": -1.0},
            ],
            "cfg_scale": 7,
            "clip_guidance_preset": "FAST_BLUE",
            "height": h,
            "width": w,
            "samples": 1,
            "steps": 30,
        }
        r = requests.post(API_URL, headers=HEADERS, json=payload, timeout=120)
        r.raise_for_status()
        data = r.json()
        img_b64 = data["artifacts"][0]["base64"]
        img_bytes = base64.b64decode(img_b64)
        out_path = IMAGES_DIR / f"{out_prefix}_{i+1:02d}.png"
        with open(out_path, "wb") as f:
            f.write(img_bytes)
        paths.append(out_path)
    return paths