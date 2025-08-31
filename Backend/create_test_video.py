import os
from pathlib import Path
import subprocess
import tempfile

def create_test_video(output_path, topic="Test Video"):
    """Create a simple test MP4 video using ffmpeg"""
    try:
        # Create a simple video with text overlay
        cmd = [
            'ffmpeg',
            '-f', 'lavfi',
            '-i', f'color=size=1920x1080:duration=5:color=black',
            '-vf', f'drawtext=text=\'{topic}\':fontcolor=white:fontsize=60:x=(w-text_w)/2:y=(h-text_h)/2',
            '-c:v', 'libx264',
            '-preset', 'ultrafast',
            '-t', '5',
            '-y',  # Overwrite output file
            str(output_path)
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ Test video created successfully: {output_path}")
            return True
        else:
            print(f"❌ Failed to create video: {result.stderr}")
            return False
            
    except FileNotFoundError:
        print("❌ ffmpeg not found. Creating a simple placeholder file instead.")
        # Fallback: create a simple text file
        with open(output_path, 'w') as f:
            f.write(f"Test video for topic: {topic}\n")
            f.write("This is a placeholder file.\n")
            f.write("To create real videos, install ffmpeg and add API keys.\n")
        return True

if __name__ == "__main__":
    # Test the video creation
    output_dir = Path(__file__).parent / "outputs" / "video"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    test_video_path = output_dir / "test_video.mp4"
    create_test_video(test_video_path, "Artificial Intelligence")
