import React, { useState } from 'react';
import CodeUploader from './CodeUploader';
import AgentResponseBox from './AgentResponseBox';
import HoloLibrarian from './HoloLibrarian';

const Dashboard = () => {
  const [response, setResponse] = useState("");

  const handleUpload = (code) => {
    setResponse(`Simulated response for code:\n${code}`);
  };

  return (
    <div className="space-y-6">
      <HoloLibrarian />
      <CodeUploader onUpload={handleUpload} />
      <AgentResponseBox response={response} />
    </div>
  );
};

export default Dashboard;
