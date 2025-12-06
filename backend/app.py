from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app) # Permite peticiones desde React

@app.route('/api/health')
def health_check():
    return jsonify({
        "status": "success",
        "message": "TaskMaster Backend is running inside Docker!",
        "system": "administrative"
    })

if __name__ == '__main__':
    # host='0.0.0.0' es OBLIGATORIO para que Docker exponga el puerto
    app.run(debug=True, host='0.0.0.0', port=5000)