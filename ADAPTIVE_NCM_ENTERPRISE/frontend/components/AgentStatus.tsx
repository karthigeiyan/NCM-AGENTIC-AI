import React from 'react';

export const AgentStatus = ({ name, role, active }: { name: string, role: string, active: boolean }) => (
  <div style={{ border: '1px solid #ccc', padding: '10px', margin: '5px', borderRadius: '5px' }}>
    <h4>{name} {active ? '🟢' : '⚪'}</h4>
    <p>{role}</p>
  </div>
);
