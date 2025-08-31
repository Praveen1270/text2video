import React, { useState, useEffect } from 'react';
import Header from './components/Header';
import TopicInput from './components/TopicInput';
import VideoSettings from './components/VideoSettings';
import ProgressIndicator from './components/ProgressIndicator';
import VideoPlayer from './components/VideoPlayer';
import ScriptPreview from './components/ScriptPreview';
import { VideoGenerationStatus, VideoSettings as VideoSettingsType } from './types';
import { generateVideo, generateScript, getVideoStatus } from './services/api';

const App: React.FC = () => {
  const [status, setStatus] = useState<VideoGenerationStatus>({ 
    status: 'idle',
    step: undefined,
    progress: 0,
    message: ''
  });
  const [settings, setSettings] = useState<VideoSettingsType>({
    voice_id: '21m00Tcm4TlvDq8ikWAM',
    width: 1920,
    height: 1080,
  });
  const [showSettings, setShowSettings] = useState(false);
  const [showScript, setShowScript] = useState(false);
  const [taskId, setTaskId] = useState<string | null>(null);

  // Poll for status updates when task is running
  useEffect(() => {
    if (!taskId || status.status === 'completed' || status.status === 'error') {
      return;
    }

    const pollStatus = async () => {
      try {
        const statusResponse = await getVideoStatus(taskId);
        setStatus(statusResponse);
        
        if (statusResponse.status === 'completed' || statusResponse.status === 'error') {
          setTaskId(null);
        }
      } catch (error) {
        console.error('Error polling status:', error);
      }
    };

    const interval = setInterval(pollStatus, 2000); // Poll every 2 seconds
    return () => clearInterval(interval);
  }, [taskId, status.status]);

  const progressSteps = [
    {
      id: 'script',
      label: 'Generating Script',
      description: 'Creating engaging content with Gemini AI',
      status: (status.step === 'script' ? 'active' : 
              status.status === 'completed' ? 'completed' : 'pending') as 'pending' | 'active' | 'completed' | 'error'
    },
    {
      id: 'images',
      label: 'Generating Images',
      description: 'Creating visuals with Stable Diffusion',
      status: (status.step === 'images' ? 'active' : 
              ['voice', 'assembly', 'complete'].includes(status.step || '') ? 'completed' : 'pending') as 'pending' | 'active' | 'completed' | 'error'
    },
    {
      id: 'voice',
      label: 'Generating Voice-over',
      description: 'Creating narration with ElevenLabs',
      status: (status.step === 'voice' ? 'active' : 
              ['assembly', 'complete'].includes(status.step || '') ? 'completed' : 'pending') as 'pending' | 'active' | 'completed' | 'error'
    },
    {
      id: 'assembly',
      label: 'Assembling Video',
      description: 'Combining everything into final video',
      status: (status.step === 'assembly' ? 'active' : 
              status.step === 'complete' ? 'completed' : 'pending') as 'pending' | 'active' | 'completed' | 'error'
    }
  ];

  const handleTopicSubmit = async (topic: string) => {
    setStatus({ status: 'generating', step: 'script', message: 'Starting video generation...' });
    
    try {
      // First generate the script
      const scriptData = await generateScript(topic);
      setStatus(prev => ({ ...prev, scriptData }));
      setShowScript(true);

      // Then generate the full video
      const videoRequest = {
        topic,
        voice_id: settings.voice_id,
        width: settings.width,
        height: settings.height,
      };

      const result = await generateVideo(videoRequest);
      setTaskId(result.task_id);
      setStatus({ status: 'generating', step: 'script', message: result.message });
    } catch (error) {
      console.error('Error generating video:', error);
      setStatus({
        status: 'error',
        message: error instanceof Error ? error.message : 'Failed to generate video'
      });
    }
  };

  const handleSettingsChange = (newSettings: VideoSettingsType) => {
    setSettings(newSettings);
  };

  const handleRegenerate = () => {
    if (status.scriptData) {
      setStatus({ status: 'idle' });
      setShowScript(false);
    }
  };

  const isGenerating = (): boolean => {
    return status.status === 'generating' || status.status === 'completed';
  };

  const renderMainContent = () => {
    if (status.status === 'generating') {
      return (
        <div className="space-y-6">
          <ProgressIndicator steps={progressSteps} currentStep={status.step} />
          {status.scriptData && showScript && (
            <ScriptPreview scriptData={status.scriptData} />
          )}
        </div>
      );
    }

    if (status.status === 'completed' && status.videoUrl) {
      return (
        <div className="space-y-6">
          <VideoPlayer 
            videoUrl={status.videoUrl} 
            title={status.scriptData?.title || 'Generated Video'}
            onRegenerate={handleRegenerate}
          />
          {status.scriptData && (
            <ScriptPreview scriptData={status.scriptData} />
          )}
        </div>
      );
    }

    if (status.status === 'error') {
      return (
        <div className="bg-red-50 border border-red-200 rounded-lg p-6">
          <div className="flex items-center space-x-2 mb-4">
            <div className="w-6 h-6 bg-red-500 text-white rounded-full flex items-center justify-center">
              !
            </div>
            <h3 className="text-lg font-semibold text-red-800">Error</h3>
          </div>
          <p className="text-red-700 mb-4">{status.message}</p>
          <button
            onClick={() => setStatus({ status: 'idle' })}
            className="bg-red-600 text-white px-4 py-2 rounded-lg hover:bg-red-700 transition-colors"
          >
            Try Again
          </button>
        </div>
      );
    }

    return (
      <div className="space-y-6">
        <TopicInput onTopicSubmit={handleTopicSubmit} isLoading={isGenerating()} />
        <VideoSettings 
          onSettingsChange={handleSettingsChange}
          isOpen={showSettings}
          onToggle={() => setShowSettings(!showSettings)}
        />
      </div>
    );
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <Header />
      <main className="container mx-auto px-4 py-8">
        <div className="max-w-4xl mx-auto">
          {renderMainContent()}
        </div>
      </main>
    </div>
  );
};

export default App;
