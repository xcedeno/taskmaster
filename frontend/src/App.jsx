import { useState, useEffect } from 'react';
import api from './services/api';
import TaskCard from './components/TaskCard';
import TaskForm from './components/TaskForm';
import LoginPage from './components/LoginPage';
import { AuthProvider, useAuth } from './context/AuthContext'; // Importamos Provider y Hook
import './App.css';

// Creamos un componente interno para manejar la lógica de vista
const Dashboard = () => {
  const [tasks, setTasks] = useState([]);
  const { user, logout } = useAuth(); // Datos del usuario logueado

  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = async () => {
    try {
      const response = await api.get('/tasks');
      setTasks(response.data);
    } catch (error) {
      console.error("Error connecting to API:", error);
      // Si el token expiró, podríamos hacer logout automático aquí
    }
  };

  const handleTaskCreated = (newTask) => {
    setTasks([...tasks, newTask]);
  };

  return (
    <div className="container" style={{ maxWidth: '800px', margin: '0 auto', padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <header style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '40px' }}>
        <div>
          <h1 style={{ margin: 0, color: '#333' }}>🚀 TaskMaster</h1>
          <small>Hola, {user?.username}</small>
        </div>
        <button onClick={logout} style={{ padding: '5px 10px', backgroundColor: '#ef4444', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer' }}>
          Cerrar Sesión
        </button>
      </header>

      <TaskForm onTaskCreated={handleTaskCreated} />

      <div className="task-list">
        {tasks.length === 0 ? (
          <p style={{ textAlign: 'center', color: '#888' }}>No tienes tareas. ¡Eres libre!</p>
        ) : (
          tasks.map(task => (
            <TaskCard key={task.id} task={task} />
          ))
        )}
      </div>
    </div>
  );
};

// Componente Principal
function App() {
  return (
    <AuthProvider>
      <MainContent />
    </AuthProvider>
  );
}

// Sub-componente para decidir qué renderizar basado en el contexto
const MainContent = () => {
  const { user } = useAuth();
  // Si hay usuario, mostramos Dashboard. Si no, Login.
  return user ? <Dashboard /> : <LoginPage />;
};

export default App;