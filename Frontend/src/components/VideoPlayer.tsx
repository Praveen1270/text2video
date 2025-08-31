import React from 'react';
import { Download, Play, Pause, RotateCcw } from 'lucide-react';
import { downloadVideo } from '../services/api';

interface VideoPlayerProps {
  videoUrl: string;
  title: string;
  onRegenerate: () => void;
}

const VideoPlayer: React.FC<VideoPlayerProps> = ({ videoUrl, title, onRegenerate }) => {
  const [isPlaying, setIsPlaying] = React.useState(false);
  const [isDownloading, setIsDownloading] = React.useState(false);
  const videoRef = React.useRef<HTMLVideoElement>(null);

  const handlePlayPause = () => {
    if (videoRef.current) {
      if (isPlaying) {
        videoRef.current.pause();
      } else {
        videoRef.current.play();
      }
      setIsPlaying(!isPlaying);
    }
  };

  const handleVideoEnded = () => {
    setIsPlaying(false);
  };

  const handleDownload = async () => {
    setIsDownloading(true);
    try {
      // Create a full URL for the download
              const fullUrl = videoUrl.startsWith('http') ? videoUrl : `http://localhost:8080${videoUrl}`;
      const a = document.createElement('a');
      a.href = fullUrl;
      a.download = `${title.replace(/[^a-z0-9]/gi, '_').toLowerCase()}.mp4`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
    } catch (error) {
      console.error('Error downloading video:', error);
      alert('Failed to download video. Please try again.');
    } finally {
      setIsDownloading(false);
    }
  };

  return (
    <div className="bg-white rounded-lg shadow-md overflow-hidden">
      <div className="p-6">
        <div className="flex items-center justify-between mb-4">
          <h3 className="text-xl font-semibold text-gray-800">{title}</h3>
          <div className="flex space-x-2">
            <button
              onClick={onRegenerate}
              className="flex items-center space-x-2 px-4 py-2 text-gray-600 hover:text-gray-800 hover:bg-gray-100 rounded-lg transition-colors"
            >
              <RotateCcw className="w-4 h-4" />
              <span>Regenerate</span>
            </button>
            <button
              onClick={handleDownload}
              disabled={isDownloading}
              className="flex items-center space-x-2 px-4 py-2 bg-primary-600 text-white hover:bg-primary-700 disabled:bg-gray-300 rounded-lg transition-colors"
            >
              {isDownloading ? (
                <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
              ) : (
                <Download className="w-4 h-4" />
              )}
              <span>{isDownloading ? 'Downloading...' : 'Download'}</span>
            </button>
          </div>
        </div>

        <div className="relative bg-black rounded-lg overflow-hidden">
          <video
            ref={videoRef}
            src={videoUrl.startsWith('http') ? videoUrl : `http://localhost:8080${videoUrl}`}
            className="w-full h-auto"
            onEnded={handleVideoEnded}
            controls
          />
          
          {/* Custom controls overlay */}
          <div className="absolute inset-0 flex items-center justify-center opacity-0 hover:opacity-100 transition-opacity">
            <button
              onClick={handlePlayPause}
              className="bg-black bg-opacity-50 text-white p-4 rounded-full hover:bg-opacity-70 transition-all"
            >
              {isPlaying ? (
                <Pause className="w-8 h-8" />
              ) : (
                <Play className="w-8 h-8" />
              )}
            </button>
          </div>
        </div>

        <div className="mt-4 p-4 bg-gray-50 rounded-lg">
          <h4 className="font-medium text-gray-800 mb-2">Video Details</h4>
          <div className="text-sm text-gray-600 space-y-1">
            <div>• Generated with AI-powered script and images</div>
            <div>• Professional voice-over narration</div>
            <div>• High-quality video output</div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default VideoPlayer;
