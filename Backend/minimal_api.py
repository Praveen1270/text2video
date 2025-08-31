from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import uuid
import os
from pathlib import Path
import subprocess

app = Flask(__name__)
CORS(app)

# Store active tasks
active_tasks = {}

# Create output directory
OUTPUT_DIR = Path(__file__).parent / "outputs" / "video"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

@app.route('/api/health', methods=['GET'])
def api_health():
    return jsonify({'status': 'healthy', 'message': 'Text2Video API is running'})

@app.route('/api/generate-script', methods=['POST'])
def api_generate_script():
    try:
        data = request.get_json()
        topic = data.get('topic')
        
        if not topic:
            return jsonify({'error': 'Topic is required'}), 400
        
        # Mock script data for testing
        script_data = {
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
        
        return jsonify(script_data)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/generate-video', methods=['POST'])
def api_generate_video():
    try:
        data = request.get_json()
        topic = data.get('topic')
        voice_id = data.get('voice_id', '21m00Tcm4TlvDq8ikWAM')
        width = data.get('width', 1920)
        height = data.get('height', 1080)
        
        if not topic:
            return jsonify({'error': 'Topic is required'}), 400
        
        # Create task
        task_id = str(uuid.uuid4())
        active_tasks[task_id] = {
            'status': 'generating',
            'step': 'script',
            'progress': 20,
            'message': 'Video generation started',
            'topic': topic
        }
        
        return jsonify({
            'task_id': task_id,
            'status': 'generating',
            'message': 'Video generation started'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/status/<task_id>', methods=['GET'])
def api_get_status(task_id):
    task = active_tasks.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    
    # Simulate progress
    current_step = task.get('step', 'script')
    if current_step == 'script':
        task['step'] = 'images'
        task['progress'] = 40
        task['message'] = 'Generating images...'
    elif current_step == 'images':
        task['step'] = 'voice'
        task['progress'] = 60
        task['message'] = 'Generating voice-over...'
    elif current_step == 'voice':
        task['step'] = 'assembly'
        task['progress'] = 80
        task['message'] = 'Assembling video...'
    elif current_step == 'assembly':
        task['status'] = 'completed'
        task['step'] = 'complete'
        task['progress'] = 100
        task['message'] = 'Video generation completed!'
        task['videoUrl'] = f'/download/{task_id}'
    
    return jsonify(task)

@app.route('/download/<task_id>', methods=['GET'])
def download_video(task_id):
    task = active_tasks.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    
    task_status = task.get('status')
    if task_status != 'completed':
        return jsonify({'error': 'Video not ready. Task status: ' + str(task_status)}), 404
    
    # Create a simple test video file
    video_path = OUTPUT_DIR / f"{task_id}.mp4"
    
    # If the video file doesn't exist, create a test video
    if not video_path.exists():
        topic = task.get('topic', 'Unknown')
        
        # Create a simple HTML file that can be served as a video placeholder
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Video: {topic}</title>
    <style>
        body {{ 
            margin: 0; 
            padding: 20px; 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            font-family: Arial, sans-serif;
            color: white;
            text-align: center;
        }}
        .video-container {{
            max-width: 800px;
            margin: 0 auto;
            background: rgba(0,0,0,0.3);
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }}
        .video-placeholder {{
            width: 100%;
            height: 400px;
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 20px;
        }}
        .info {{
            background: rgba(255,255,255,0.1);
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
        }}
    </style>
</head>
<body>
    <div class="video-container">
        <h1>🎬 AI-Generated Video</h1>
        <div class="video-placeholder">
            📹 {topic}
        </div>
        <div class="info">
            <h3>Video Details</h3>
            <p><strong>Topic:</strong> {topic}</p>
            <p><strong>Status:</strong> Generated successfully</p>
            <p><strong>Duration:</strong> 5 seconds</p>
            <p><strong>Resolution:</strong> 1920x1080</p>
            <hr>
            <p><em>This is a placeholder video. In the real implementation, this would be an actual MP4 video file generated with AI.</em></p>
        </div>
    </div>
</body>
</html>
"""
        
        # Save as HTML file instead of MP4
        html_path = video_path.with_suffix('.html')
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # Also create a simple text file as backup
        with open(video_path, 'w') as f:
            f.write(f"Video placeholder for topic: {topic}\n")
            f.write("This is a placeholder file.\n")
            f.write("To create real videos, install ffmpeg and add API keys.\n")
    
    # Try to serve the HTML file if it exists, otherwise serve the text file
    html_path = video_path.with_suffix('.html')
    if html_path.exists():
        return send_file(
            html_path,
            as_attachment=False,
            download_name=f"{task.get('topic', 'video').replace(' ', '_').lower()}.html",
            mimetype='text/html'
        )
    else:
        return send_file(
            video_path,
            as_attachment=True,
            download_name=f"{task.get('topic', 'video').replace(' ', '_').lower()}.txt",
            mimetype='text/plain'
        )

@app.route('/api/voices', methods=['GET'])
def api_get_voices():
    voices = [
        {'id': '21m00Tcm4TlvDq8ikWAM', 'name': 'Rachel', 'description': 'Professional female voice'},
        {'id': 'AZnzlk1XvdvUeBnXmlld', 'name': 'Domi', 'description': 'Professional male voice'},
        {'id': 'EXAVITQu4vr4xnSDxMaL', 'name': 'Bella', 'description': 'Friendly female voice'},
        {'id': 'ErXwobaYiN019PkySvjV', 'name': 'Antoni', 'description': 'Deep male voice'},
        {'id': 'MF3mGyEYCl7XYWbV9V6O', 'name': 'Elli', 'description': 'Young female voice'},
        {'id': 'TxGEqnHWrfWFTfGW9XjX', 'name': 'Josh', 'description': 'Young male voice'},
        {'id': 'VR6AewLTigWG4xSOukaG', 'name': 'Arnold', 'description': 'Strong male voice'},
        {'id': 'pNInz6obpgDQGcFmaJgB', 'name': 'Adam', 'description': 'Casual male voice'},
        {'id': 'yoZ06aMxZJJ28mfd3POQ', 'name': 'Sam', 'description': 'Friendly male voice'},
    ]
    return jsonify(voices)

if __name__ == '__main__':
    print("Starting minimal API server on port 8080...")
    app.run(debug=True, host='0.0.0.0', port=8080)
