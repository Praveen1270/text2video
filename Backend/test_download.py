import requests
import json

# Test the API endpoints
base_url = "http://localhost:8080"

def test_video_generation():
    print("Testing video generation workflow...")
    
    # 1. Generate a video
    video_data = {
        "topic": "artificial intelligence",
        "voice_id": "21m00Tcm4TlvDq8ikWAM",
        "width": 1920,
        "height": 1080
    }
    
    response = requests.post(f"{base_url}/api/generate-video", json=video_data)
    print(f"Generate video response: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        task_id = result.get('task_id')
        print(f"Task ID: {task_id}")
        
        # 2. Check status multiple times to simulate progress
        for i in range(5):
            status_response = requests.get(f"{base_url}/api/status/{task_id}")
            if status_response.status_code == 200:
                status_data = status_response.json()
                print(f"Status {i+1}: {status_data.get('step')} - {status_data.get('message')}")
                
                # 3. Try to download when completed
                if status_data.get('status') == 'completed':
                    download_url = status_data.get('videoUrl')
                    if download_url:
                        print(f"Attempting to download from: {download_url}")
                        download_response = requests.get(f"{base_url}{download_url}")
                        print(f"Download response: {download_response.status_code}")
                        if download_response.status_code == 200:
                            print("✅ Download successful!")
                            return True
                        else:
                            print(f"❌ Download failed: {download_response.text}")
                            return False
            else:
                print(f"❌ Status check failed: {status_response.status_code}")
                return False
    
    print("❌ Video generation failed")
    return False

if __name__ == "__main__":
    print("Testing Flask API with dictionary-based task storage...")
    test_video_generation()
