import React from 'react';

const AgentResponseBox = ({ response }) => (
  <div className="p-4 bg-black/80 rounded-lg border border-green-400 text-green-300 whitespace-pre-wrap">
    {response || "Awaiting agent response..."}
  </div>
);

export default AgentResponseBox;
