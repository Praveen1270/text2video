import React from 'react';
import { FileText, Image, Volume2 } from 'lucide-react';
import { ScriptData } from '../types';

interface ScriptPreviewProps {
  scriptData: ScriptData;
}

const ScriptPreview: React.FC<ScriptPreviewProps> = ({ scriptData }) => {
  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      <div className="flex items-center space-x-2 mb-6">
        <FileText className="w-5 h-5 text-primary-600" />
        <h3 className="text-xl font-semibold text-gray-800">Generated Script</h3>
      </div>

      {/* Title */}
      <div className="mb-6">
        <h4 className="text-lg font-medium text-gray-800 mb-2">Title</h4>
        <div className="p-4 bg-gray-50 rounded-lg">
          <p className="text-gray-700">{scriptData.title}</p>
        </div>
      </div>

      {/* Full Script */}
      <div className="mb-6">
        <h4 className="text-lg font-medium text-gray-800 mb-2">Full Script</h4>
        <div className="p-4 bg-gray-50 rounded-lg">
          <p className="text-gray-700 leading-relaxed">{scriptData.script}</p>
        </div>
      </div>

      {/* Scenes */}
      <div>
        <h4 className="text-lg font-medium text-gray-800 mb-4">Scenes Breakdown</h4>
        <div className="space-y-4">
          {scriptData.scenes.map((scene, index) => (
            <div key={index} className="border border-gray-200 rounded-lg p-4">
              <div className="flex items-center space-x-2 mb-3">
                <div className="w-6 h-6 bg-primary-600 text-white rounded-full flex items-center justify-center text-sm font-medium">
                  {index + 1}
                </div>
                <h5 className="font-medium text-gray-800">Scene {index + 1}</h5>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                {/* Caption */}
                <div>
                  <div className="flex items-center space-x-2 mb-2">
                    <FileText className="w-4 h-4 text-gray-500" />
                    <span className="text-sm font-medium text-gray-600">Caption</span>
                  </div>
                  <div className="p-3 bg-blue-50 rounded border border-blue-200">
                    <p className="text-sm text-blue-800">{scene.caption}</p>
                  </div>
                </div>

                {/* Image Prompt */}
                <div>
                  <div className="flex items-center space-x-2 mb-2">
                    <Image className="w-4 h-4 text-gray-500" />
                    <span className="text-sm font-medium text-gray-600">Image Prompt</span>
                  </div>
                  <div className="p-3 bg-green-50 rounded border border-green-200">
                    <p className="text-sm text-green-800">{scene.image_prompt}</p>
                  </div>
                </div>

                {/* Voice Text */}
                <div>
                  <div className="flex items-center space-x-2 mb-2">
                    <Volume2 className="w-4 h-4 text-gray-500" />
                    <span className="text-sm font-medium text-gray-600">Voice Text</span>
                  </div>
                  <div className="p-3 bg-purple-50 rounded border border-purple-200">
                    <p className="text-sm text-purple-800">{scene.voice}</p>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>

      <div className="mt-6 p-4 bg-primary-50 rounded-lg">
        <div className="flex items-center space-x-2">
          <div className="w-2 h-2 bg-primary-600 rounded-full"></div>
          <span className="text-sm text-primary-700">
            This script will be used to generate {scriptData.scenes.length} scenes with AI-generated images and voice-over narration.
          </span>
        </div>
      </div>
    </div>
  );
};

export default ScriptPreview;
