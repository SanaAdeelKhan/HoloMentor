import React from 'react';

const HoloLibrarian = ({ message }) => (
  <div className="text-white p-6 rounded-xl bg-gradient-to-r from-indigo-700 to-purple-800 shadow-2xl border border-white/20">
    <h2 className="text-2xl font-bold">🧠 HoloMentor</h2>
    <p>{message || "Ask me about your contract!"}</p>
  </div>
);

export default HoloLibrarian;
