export interface VideoRequest {
  topic: string;
  voice_id?: string;
  width?: number;
  height?: number;
}

export interface Scene {
  caption: string;
  image_prompt: string;
  voice: string;
}

export interface ScriptData {
  title: string;
  script: string;
  scenes: Scene[];
}

export interface VideoGenerationStatus {
  status: 'idle' | 'generating' | 'completed' | 'error';
  step?: 'script' | 'images' | 'voice' | 'assembly' | 'complete';
  progress?: number;
  message?: string;
  videoUrl?: string;
  scriptData?: ScriptData;
}

export interface VoiceOption {
  id: string;
  name: string;
  description: string;
}

export interface VideoSettings {
  width: number;
  height: number;
  voice_id: string;
}
