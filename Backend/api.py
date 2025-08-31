from flask import Flask, request, jsonify, send_from_directory, send_file
from flask_cors import CORS
import os
import uuid
import threading
import time
from pathlib import Path
from main import run
from llm.gemini_client import generate_script_and_scenes
from config import VIDEO_DIR, OUTPUT_DIR
import json

app = Flask(__name__)
CORS(app)

# Store active tasks
active_tasks = {}

# Dictionary-based task storage
def create_task(task_id: str, topic: str, voice_id: str, width: int, height: int):
    return {
        'task_id': task_id,
        'topic': topic,
        'voice_id': voice_id,
        'width': width,
        'height': height,
        'status': 'generating',
        'step': 'script',
        'progress': 0,
        'message': 'Starting video generation...',
        'video_url': None,
        'script_data': None,
        'error': None
    }

def update_task_status(task: dict, step: str, message: str, progress: int = None):
    task['step'] = step
    task['message'] = message
    if progress is not None:
        task['progress'] = progress

def complete_task(task: dict, video_path: str):
    task['status'] = 'completed'
    task['step'] = 'complete'
    task['progress'] = 100
    task['message'] = 'Video generation completed!'
    task['video_url'] = f'/download/{task["task_id"]}'

def fail_task(task: dict, error: str):
    task['status'] = 'error'
    task['error'] = error
    task['message'] = f'Error: {error}'

def generate_video_task(task: dict):
    try:
        # Step 1: Generate script
        update_task_status(task, 'script', 'Generating script with Gemini AI...', 20)
        script_data = generate_script_and_scenes(task['topic'])
        task['script_data'] = script_data

        # Step 2: Generate images
        update_task_status(task, 'images', 'Generating images with Stable Diffusion...', 40)
        
        # Step 3: Generate voice
        update_task_status(task, 'voice', 'Generating voice-over with ElevenLabs...', 60)
        
        # Step 4: Assemble video
        update_task_status(task, 'assembly', 'Assembling final video...', 80)
        
        # Generate the video
        output_filename = f"{task['task_id']}.mp4"
        output_path = VIDEO_DIR / output_filename
        
        run(
            topic=task['topic'],
            voice_id=task['voice_id'],
            width=task['width'],
            height=task['height'],
            out=str(output_path)
        )
        
        complete_task(task, str(output_path))
        
    except Exception as e:
        fail_task(task, str(e))
        print(f"Error in video generation task {task['task_id']}: {e}")

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
        task = create_task(task_id, topic, voice_id, width, height)
        active_tasks[task_id] = task
        
        # Start generation in background
        thread = threading.Thread(target=generate_video_task, args=(task,))
        thread.daemon = True
        thread.start()
        
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
    
    response = {
        'status': task.get('status'),
        'step': task.get('step'),
        'progress': task.get('progress'),
        'message': task.get('message')
    }
    
    if task.get('video_url'):
        response['videoUrl'] = task['video_url']
    
    if task.get('script_data'):
        response['scriptData'] = task['script_data']
    
    if task.get('error'):
        response['error'] = task['error']
    
    return jsonify(response)

@app.route('/api/generate-script', methods=['POST'])
def api_generate_script():
    try:
        data = request.get_json()
        topic = data.get('topic')
        
        if not topic:
            return jsonify({'error': 'Topic is required'}), 400
        
        script_data = generate_script_and_scenes(topic)
        return jsonify(script_data)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download/<task_id>', methods=['GET'])
def download_video(task_id):
    task = active_tasks.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    
    task_status = task.get('status')
    if task_status != 'completed':
        return jsonify({'error': 'Video not ready. Task status: ' + str(task_status)}), 404
    
    video_path = VIDEO_DIR / f"{task_id}.mp4"
    if not video_path.exists():
        return jsonify({'error': 'Video file not found'}), 404
    
    return send_file(
        video_path,
        as_attachment=True,
        download_name=f"{task.get('topic', 'video').replace(' ', '_').lower()}.mp4",
        mimetype='video/mp4'
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

@app.route('/api/health', methods=['GET'])
def api_health():
    return jsonify({'status': 'healthy', 'message': 'Text2Video API is running'})

if __name__ == '__main__':
    # Ensure output directories exist
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    VIDEO_DIR.mkdir(parents=True, exist_ok=True)
    
    app.run(debug=True, host='0.0.0.0', port=8080)
