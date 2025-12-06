import React, { useState } from 'react';
import api from '../services/api';

const TaskForm = ({ onTaskCreated }) => {
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            // ID de usuario "hardcodeado" por ahora (lo arreglaremos al hacer Login)
            const payload = {
                title,
                description,
                user_id: 1,
                priority: 'Medium'
            };

            const response = await api.post('/tasks', payload);

            // Limpiar formulario y avisar al padre que actualice la lista
            setTitle('');
            setDescription('');
            onTaskCreated(response.data);

        } catch (error) {
            console.error('Error creating task:', error);
            alert('Error al crear tarea. ¿Creaste el usuario ID 1 en el sprint pasado?');
        }
    };

    return (
        <form onSubmit={handleSubmit} style={{ marginBottom: '20px', padding: '20px', backgroundColor: '#f8f9fa', borderRadius: '8px' }}>
            <h2 style={{ marginTop: 0 }}>Nueva Tarea</h2>
            <div style={{ marginBottom: '10px' }}>
                <input
                    type="text"
                    placeholder="Título de la tarea"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                    required
                    style={{ width: '100%', padding: '8px', marginBottom: '10px' }}
                />
                <textarea
                    placeholder="Descripción"
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                    style={{ width: '100%', padding: '8px' }}
                />
            </div>
            <button type="submit" style={{ padding: '10px 20px', backgroundColor: '#3b82f6', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer' }}>
                Agregar Tarea
            </button>
        </form>
    );
};

export default TaskForm;