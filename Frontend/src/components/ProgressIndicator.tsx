import React from 'react';
import { CheckCircle, Circle, Loader } from 'lucide-react';

interface ProgressStep {
  id: string;
  label: string;
  description: string;
  status: 'pending' | 'active' | 'completed' | 'error';
}

interface ProgressIndicatorProps {
  steps: ProgressStep[];
  currentStep?: string;
}

const ProgressIndicator: React.FC<ProgressIndicatorProps> = ({ steps, currentStep }) => {
  const getStepIcon = (step: ProgressStep) => {
    switch (step.status) {
      case 'completed':
        return <CheckCircle className="w-6 h-6 text-green-500" />;
      case 'active':
        return <Loader className="w-6 h-6 text-primary-600 animate-spin" />;
      case 'error':
        return <Circle className="w-6 h-6 text-red-500" />;
      default:
        return <Circle className="w-6 h-6 text-gray-300" />;
    }
  };

  const getStepClasses = (step: ProgressStep) => {
    switch (step.status) {
      case 'completed':
        return 'text-green-600';
      case 'active':
        return 'text-primary-600';
      case 'error':
        return 'text-red-600';
      default:
        return 'text-gray-400';
    }
  };

  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      <h3 className="text-lg font-semibold text-gray-800 mb-6">Generating Your Video</h3>
      
      <div className="space-y-4">
        {steps.map((step, index) => (
          <div key={step.id} className="flex items-start space-x-4">
            <div className="flex-shrink-0 mt-1">
              {getStepIcon(step)}
            </div>
            
            <div className="flex-1 min-w-0">
              <div className={`font-medium ${getStepClasses(step)}`}>
                {step.label}
              </div>
              <div className="text-sm text-gray-500 mt-1">
                {step.description}
              </div>
              
              {step.status === 'active' && (
                <div className="mt-2">
                  <div className="w-full bg-gray-200 rounded-full h-2">
                    <div className="bg-primary-600 h-2 rounded-full animate-pulse" style={{ width: '60%' }}></div>
                  </div>
                </div>
              )}
            </div>
          </div>
        ))}
      </div>
      
      <div className="mt-6 p-4 bg-primary-50 rounded-lg">
        <div className="flex items-center space-x-2">
          <div className="w-2 h-2 bg-primary-600 rounded-full animate-pulse"></div>
          <span className="text-sm text-primary-700">
            This process typically takes 2-3 minutes. Please don't close this page.
          </span>
        </div>
      </div>
    </div>
  );
};

export default ProgressIndicator;
