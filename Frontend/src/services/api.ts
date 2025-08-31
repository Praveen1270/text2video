import axios from 'axios';
import { VideoRequest, ScriptData, VideoGenerationStatus } from '../types';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8080';

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 300000, // 5 minutes timeout for video generation
});

// Voice options for ElevenLabs
export const voiceOptions = [
  { id: '21m00Tcm4TlvDq8ikWAM', name: 'Rachel', description: 'Professional female voice' },
  { id: 'AZnzlk1XvdvUeBnXmlld', name: 'Domi', description: 'Professional male voice' },
  { id: 'EXAVITQu4vr4xnSDxMaL', name: 'Bella', description: 'Friendly female voice' },
  { id: 'ErXwobaYiN019PkySvjV', name: 'Antoni', description: 'Deep male voice' },
  { id: 'MF3mGyEYCl7XYWbV9V6O', name: 'Elli', description: 'Young female voice' },
  { id: 'TxGEqnHWrfWFTfGW9XjX', name: 'Josh', description: 'Young male voice' },
  { id: 'VR6AewLTigWG4xSOukaG', name: 'Arnold', description: 'Strong male voice' },
  { id: 'pNInz6obpgDQGcFmaJgB', name: 'Adam', description: 'Casual male voice' },
  { id: 'yoZ06aMxZJJ28mfd3POQ', name: 'Sam', description: 'Friendly male voice' },
];

export const generateVideo = async (request: VideoRequest): Promise<{ task_id: string; status: string; message: string }> => {
  try {
    const response = await api.post('/api/generate-video', request);
    return response.data;
  } catch (error) {
    console.error('Error generating video:', error);
    throw error;
  }
};

export const getVideoStatus = async (taskId: string): Promise<VideoGenerationStatus> => {
  try {
    const response = await api.get(`/api/status/${taskId}`);
    return response.data;
  } catch (error) {
    console.error('Error getting video status:', error);
    throw error;
  }
};

export const downloadVideo = async (videoUrl: string): Promise<Blob> => {
  try {
    const response = await api.get(videoUrl, { responseType: 'blob' });
    return response.data;
  } catch (error) {
    console.error('Error downloading video:', error);
    throw error;
  }
};

export const generateScript = async (topic: string): Promise<ScriptData> => {
  try {
    const response = await api.post('/api/generate-script', { topic });
    return response.data;
  } catch (error) {
    console.error('Error generating script:', error);
    throw error;
  }
};
