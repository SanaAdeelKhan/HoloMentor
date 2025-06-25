import React, { useState } from 'react';

const CodeUploader = ({ onUpload }) => {
  const [code, setCode] = useState("");

  return (
    <div className="mb-4">
      <textarea
        rows="8"
        value={code}
        onChange={(e) => setCode(e.target.value)}
        placeholder="Paste your C++ smart contract here"
        className="w-full p-3 rounded-lg bg-gray-900 text-white"
      />
      <button
        onClick={() => onUpload(code)}
        className="mt-2 px-4 py-2 bg-green-600 text-white rounded-lg"
      >
        Upload Code
      </button>
    </div>
  );
};

export default CodeUploader;
