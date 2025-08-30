import argparse
from pathlib import Path
from config import DEFAULT_RES
from llm.gemini_client import generate_script_and_scenes
from image.stability_client import generate_images
from tts.eleven_client import synthesize_voice
from assemble.video_maker import assemble_video

def run(topic: str, voice_id: str | None, width: int, height: int, out: str):
    print("[1/5] Generating script & scenes with Gemini...")
    data = generate_script_and_scenes(topic)
    title = data.get("title", "Explainer")
    script = data.get("script", "")
    scenes = data.get("scenes", [])

    if not scenes:
        raise RuntimeError("Gemini returned no scenes. Try another topic.")

    print("[2/5] Generating images with Stable Diffusion...")
    prompts = [s.get("image_prompt", s.get("caption", topic)) for s in scenes]
    img_paths = generate_images(prompts, out_prefix=Path(out).stem, size=(width, height))

    print("[3/5] Generating voice-over with ElevenLabs...")
    audio_path = synthesize_voice(script, voice_id=voice_id)

    print("[4/5] Assembling video with MoviePy...")
    assemble_video(
        img_paths=img_paths,
        audio_path=audio_path,
        scenes=scenes,
        out_path=out,
        title=title,
        resolution=(width, height)
    )

    print(f"[5/5] Done! Video saved to {out}")

def main():
    parser = argparse.ArgumentParser(description="Text-to-Video Generator")
    parser.add_argument("topic", type=str, help="Topic for the explainer video")
    parser.add_argument("--voice", type=str, default=None, help="Voice ID for ElevenLabs")
    parser.add_argument("--width", type=int, default=DEFAULT_RES[0], help="Video width")
    parser.add_argument("--height", type=int, default=DEFAULT_RES[1], help="Video height")
    parser.add_argument("--out", type=str, default="output.mp4", help="Output video file path")
    args = parser.parse_args()

    run(
        topic=args.topic,
        voice_id=args.voice,
        width=args.width,
        height=args.height,
        out=args.out
    )

if __name__ == "__main__":
    main()