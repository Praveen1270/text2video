import React, { useState } from 'react';
import { Settings, Volume2, Monitor } from 'lucide-react';
import { voiceOptions } from '../services/api';

interface VideoSettingsProps {
  onSettingsChange: (settings: { voice_id: string; width: number; height: number }) => void;
  isOpen: boolean;
  onToggle: () => void;
}

const resolutionOptions = [
  { width: 1920, height: 1080, label: 'Full HD (1920x1080)', aspect: '16:9' },
  { width: 1280, height: 720, label: 'HD (1280x720)', aspect: '16:9' },
  { width: 854, height: 480, label: 'SD (854x480)', aspect: '16:9' },
  { width: 1080, height: 1920, label: 'Vertical (1080x1920)', aspect: '9:16' },
];

const VideoSettings: React.FC<VideoSettingsProps> = ({ onSettingsChange, isOpen, onToggle }) => {
  const [selectedVoice, setSelectedVoice] = useState(voiceOptions[0].id);
  const [selectedResolution, setSelectedResolution] = useState(resolutionOptions[0]);

  const handleVoiceChange = (voiceId: string) => {
    setSelectedVoice(voiceId);
    onSettingsChange({
      voice_id: voiceId,
      width: selectedResolution.width,
      height: selectedResolution.height,
    });
  };

  const handleResolutionChange = (resolution: typeof resolutionOptions[0]) => {
    setSelectedResolution(resolution);
    onSettingsChange({
      voice_id: selectedVoice,
      width: resolution.width,
      height: resolution.height,
    });
  };

  return (
    <div className="bg-white rounded-lg shadow-md">
      <button
        onClick={onToggle}
        className="w-full p-4 flex items-center justify-between text-left hover:bg-gray-50 transition-colors rounded-lg"
      >
        <div className="flex items-center space-x-2">
          <Settings className="w-5 h-5 text-primary-600" />
          <span className="font-medium text-gray-800">Video Settings</span>
        </div>
        <div className={`transform transition-transform ${isOpen ? 'rotate-180' : ''}`}>
          <svg className="w-5 h-5 text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
          </svg>
        </div>
      </button>

      {isOpen && (
        <div className="px-4 pb-4 space-y-6">
          {/* Voice Selection */}
          <div>
            <div className="flex items-center space-x-2 mb-3">
              <Volume2 className="w-4 h-4 text-primary-600" />
              <h3 className="font-medium text-gray-800">Voice Selection</h3>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
              {voiceOptions.map((voice) => (
                <button
                  key={voice.id}
                  onClick={() => handleVoiceChange(voice.id)}
                  className={`p-3 text-left rounded-lg border transition-all ${
                    selectedVoice === voice.id
                      ? 'border-primary-500 bg-primary-50 text-primary-700'
                      : 'border-gray-200 hover:border-gray-300 hover:bg-gray-50'
                  }`}
                >
                  <div className="font-medium text-sm">{voice.name}</div>
                  <div className="text-xs text-gray-500">{voice.description}</div>
                </button>
              ))}
            </div>
          </div>

          {/* Resolution Selection */}
          <div>
            <div className="flex items-center space-x-2 mb-3">
              <Monitor className="w-4 h-4 text-primary-600" />
              <h3 className="font-medium text-gray-800">Video Resolution</h3>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
              {resolutionOptions.map((resolution) => (
                <button
                  key={`${resolution.width}x${resolution.height}`}
                  onClick={() => handleResolutionChange(resolution)}
                  className={`p-3 text-left rounded-lg border transition-all ${
                    selectedResolution.width === resolution.width && selectedResolution.height === resolution.height
                      ? 'border-primary-500 bg-primary-50 text-primary-700'
                      : 'border-gray-200 hover:border-gray-300 hover:bg-gray-50'
                  }`}
                >
                  <div className="font-medium text-sm">{resolution.label}</div>
                  <div className="text-xs text-gray-500">Aspect ratio: {resolution.aspect}</div>
                </button>
              ))}
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default VideoSettings;
