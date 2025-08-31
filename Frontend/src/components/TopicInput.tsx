import React, { useState } from 'react';
import { Search, Lightbulb, Video } from 'lucide-react';

interface TopicInputProps {
  onTopicSubmit: (topic: string) => void;
  isLoading: boolean;
}

const topicSuggestions = [
  'How do electric circuits work?',
  'The water cycle explained',
  'Photosynthesis process',
  'How do airplanes fly?',
  'The human digestive system',
  'How do solar panels work?',
  'The life cycle of a butterfly',
  'How do computers work?',
  'The process of photosynthesis',
  'How do magnets work?',
  'The water cycle',
  'How do volcanoes erupt?',
  'The human heart and circulation',
  'How do plants grow?',
  'The solar system planets'
];

const TopicInput: React.FC<TopicInputProps> = ({ onTopicSubmit, isLoading }) => {
  const [topic, setTopic] = useState('');
  const [showSuggestions, setShowSuggestions] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (topic.trim() && !isLoading) {
      onTopicSubmit(topic.trim());
    }
  };

  const handleSuggestionClick = (suggestion: string) => {
    setTopic(suggestion);
    setShowSuggestions(false);
    onTopicSubmit(suggestion);
  };

  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      <div className="flex items-center space-x-2 mb-4">
        <Search className="w-5 h-5 text-primary-600" />
        <h2 className="text-xl font-semibold text-gray-800">What would you like to create a video about?</h2>
      </div>
      
      <form onSubmit={handleSubmit} className="space-y-4">
        <div className="relative">
          <input
            type="text"
            value={topic}
            onChange={(e) => setTopic(e.target.value)}
            onFocus={() => setShowSuggestions(true)}
            placeholder="Enter a topic (e.g., 'How do electric circuits work?')"
            className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent outline-none transition-all"
            disabled={isLoading}
          />
        </div>

        {showSuggestions && topicSuggestions.length > 0 && (
          <div className="bg-gray-50 rounded-lg p-4 border border-gray-200">
            <div className="flex items-center space-x-2 mb-3">
              <Lightbulb className="w-4 h-4 text-yellow-500" />
              <span className="text-sm font-medium text-gray-700">Popular topics:</span>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-2">
              {topicSuggestions.map((suggestion, index) => (
                <button
                  key={index}
                  type="button"
                  onClick={() => handleSuggestionClick(suggestion)}
                  className="text-left p-2 text-sm text-gray-600 hover:bg-primary-50 hover:text-primary-700 rounded transition-colors"
                >
                  {suggestion}
                </button>
              ))}
            </div>
          </div>
        )}

        <button
          type="submit"
          disabled={!topic.trim() || isLoading}
          className="w-full bg-primary-600 text-white py-3 px-6 rounded-lg font-medium hover:bg-primary-700 disabled:bg-gray-300 disabled:cursor-not-allowed transition-colors flex items-center justify-center space-x-2"
        >
          {isLoading ? (
            <>
              <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
              <span>Generating...</span>
            </>
          ) : (
            <>
              <Video className="w-4 h-4" />
              <span>Generate Video</span>
            </>
          )}
        </button>
      </form>
    </div>
  );
};

export default TopicInput;
