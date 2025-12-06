import React from 'react';

// Estilos simples para una tarjeta limpia (puedes pasarlo a CSS luego)
const styles = {
    card: {
        backgroundColor: 'white',
        borderRadius: '8px',
        padding: '16px',
        margin: '10px 0',
        boxShadow: '0 2px 4px rgba(0,0,0,0.1)',
        borderLeft: '5px solid #3b82f6' // Azul bonito
    },
    title: { margin: '0 0 8px 0', fontSize: '1.2rem' },
    status: {
        fontSize: '0.8rem',
        padding: '4px 8px',
        borderRadius: '12px',
        backgroundColor: '#e0f2fe',
        color: '#0369a1'
    }
};

const TaskCard = ({ task }) => {
    return (
        <div style={styles.card}>
            <h3 style={styles.title}>{task.title}</h3>
            <p style={{ color: '#666' }}>{task.description}</p>
            <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: '10px' }}>
                <span style={styles.status}>{task.status}</span>
                <span style={{ fontSize: '0.8rem', color: '#999' }}>Prioridad: {task.priority}</span>
            </div>
        </div>
    );
};

export default TaskCard;