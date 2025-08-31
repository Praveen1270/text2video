import React from 'react';
import { Video, Sparkles } from 'lucide-react';

const Header: React.FC = () => {
  return (
    <header className="bg-gradient-to-r from-primary-600 to-primary-700 text-white shadow-lg">
      <div className="container mx-auto px-4 py-6">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <div className="flex items-center justify-center w-10 h-10 bg-white bg-opacity-20 rounded-lg">
              <Video className="w-6 h-6" />
            </div>
            <div>
              <h1 className="text-2xl font-bold">Text2Video</h1>
              <p className="text-primary-100 text-sm">AI-Powered Video Generator</p>
            </div>
          </div>
          <div className="flex items-center space-x-2 text-primary-100">
            <Sparkles className="w-5 h-5" />
            <span className="text-sm font-medium">Powered by AI</span>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;
