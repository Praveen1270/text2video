from __future__ import annotations
# Semi-transparent caption bar
bar_h = int(H * 0.14)
bar_y = H - bar_h
draw.rectangle([(0, bar_y), (W, H)], fill=(0, 0, 0, 128))


# Text
font_path = _pick_font()
font = ImageFont.truetype(font_path, int(bar_h * 0.45)) if font_path else None
text = caption[:90]
tw, th = draw.textbbox((0, 0), text, font=font)[2:]
x = (W - tw) // 2
y = bar_y + (bar_h - th) // 2
draw.text((x, y), text, fill=(255, 255, 255), font=font)


out = TMP_DIR / f"cap_{img_path.name}"
img.save(out)
return out




def assemble_video(scenes: List[Dict[str, Any]], image_paths: List[Path], audio_path: Path,
out_name: str = "video.mp4", fps: int = DEFAULT_FPS, res=DEFAULT_RES) -> Path:
# Load audio for total duration
audio_clip = AudioFileClip(str(audio_path))
total_dur = audio_clip.duration


# Compute per-scene durations proportionally to voice lengths
voice_lengths = [max(1, len(s.get("voice", ""))) for s in scenes]
total_chars = sum(voice_lengths)
durations = [total_dur * (vl / total_chars) for vl in voice_lengths]


# Prepare image clips (with captions)
clips = []
for scene, img_path, dur in zip(scenes, image_paths, durations):
captioned = caption_image(img_path, scene.get("caption", ""), size=res)
clip = ImageClip(str(captioned)).set_duration(dur)
clips.append(clip)


video = concatenate_videoclips(clips)
final = video.set_audio(audio_clip)


out_path = VIDEO_DIR / out_name
final.write_videofile(
str(out_path), fps=fps, codec="libx264", audio_codec="aac", bitrate="4000k"
)
try:
audio_clip.close()
video.close()
final.close()
except Exception:
pass
return out_path