import { useState, useEffect } from 'react';
import api from './services/api';
import TaskCard from './components/TaskCard';
import TaskForm from './components/TaskForm';
import './App.css'; // Asegúrate de borrar los estilos viejos de este archivo

function App() {
  const [tasks, setTasks] = useState([]);

  // Cargar tareas al iniciar
  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = async () => {
    try {
      const response = await api.get('/tasks');
      setTasks(response.data);
    } catch (error) {
      console.error("Error connecting to API:", error);
    }
  };

  const handleTaskCreated = (newTask) => {
    // Agregamos la nueva tarea a la lista existente
    setTasks([...tasks, newTask]);
  };

  return (
    <div className="container" style={{ maxWidth: '800px', margin: '0 auto', padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <header style={{ textAlign: 'center', marginBottom: '40px' }}>
        <h1 style={{ color: '#333' }}>🚀 TaskMaster</h1>
        <p>Gestión de proyectos escalable</p>
      </header>

      <TaskForm onTaskCreated={handleTaskCreated} />

      <div className="task-list">
        {tasks.length === 0 ? (
          <p style={{ textAlign: 'center', color: '#888' }}>No hay tareas pendientes. ¡Buen trabajo!</p>
        ) : (
          tasks.map(task => (
            <TaskCard key={task.id} task={task} />
          ))
        )}
      </div>
    </div>
  );
}

export default App;