import React, { useState } from 'react';

export default function Dashboard() {
  const [taskStatus, setTaskStatus] = useState<string>("IDLE");
  const [uncertainty, setUncertainty] = useState<number>(0.14);

  const runSimulation = () => {
    setTaskStatus("EXECUTING");
    setTimeout(() => {
      setUncertainty(Math.round(Math.random() * 30 + 10) / 100);
      setTaskStatus("COMPLETED");
    }, 1200);
  };

  return (
    <div style={{ padding: '2rem', fontFamily: 'system-ui, sans-serif', backgroundColor: '#0f172a', color: '#f8fafc', minHeight: '100vh' }}>
      <h1>Uncertainty-Guided Adaptive NCM Enterprise</h1>
      <p style={{ color: '#94a3b8' }}>Dynamic Neural Cognitive Model & Multi-Agent Orchestration Controller</p>
      
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '1rem', marginTop: '2rem' }}>
        <div style={{ background: '#1e293b', padding: '1.5rem', borderRadius: '8px', border: '1px solid #334155' }}>
          <h3>Epistemic Uncertainty</h3>
          <p style={{ fontSize: '2rem', fontWeight: 'bold', color: uncertainty > 0.35 ? '#ef4444' : '#10b981' }}>
            {uncertainty.toFixed(3)}
          </p>
        </div>

        <div style={{ background: '#1e293b', padding: '1.5rem', borderRadius: '8px', border: '1px solid #334155' }}>
          <h3>Active Agents</h3>
          <p style={{ fontSize: '2rem', fontWeight: 'bold', color: '#3b82f6' }}>6 Autonomous Agents</p>
        </div>

        <div style={{ background: '#1e293b', padding: '1.5rem', borderRadius: '8px', border: '1px solid #334155' }}>
          <h3>Task Execution Status</h3>
          <p style={{ fontSize: '1.5rem', fontWeight: 'bold', color: '#f59e0b' }}>{taskStatus}</p>
        </div>
      </div>

      <button 
        onClick={runSimulation} 
        style={{ marginTop: '2rem', padding: '0.75rem 1.5rem', backgroundColor: '#3b82f6', color: '#fff', border: 'none', borderRadius: '6px', cursor: 'pointer', fontSize: '1rem', fontWeight: 'bold' }}>
        Trigger Adaptive Enterprise Task Execution
      </button>
    </div>
  );
}
