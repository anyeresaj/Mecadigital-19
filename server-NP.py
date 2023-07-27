# server-NP.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np


app = Flask(__name__)
CORS(app)  # Aquí es donde permites a Flask aceptar solicitudes de cualquier origen.


@app.route('/Evaluar', methods=['POST'])
def evaluar():
    try:
        data = request.get_json()

        # Extrae las respuestas de la petición.
        respuestas = data.get('respuestas', [])
        porcentajes = data.get('porcentajes', [])


       # Convertir las respuestas a floats y validar.
        calificaciones_float = []
        porcentajes_float = []
        suma_porcentajes = 0

        for respuesta, porcentaje in zip(respuestas, porcentajes):
            respuesta = round(float(respuesta), 2)
            porcentaje = round(float(porcentaje)/100, 2)

            
            if respuesta < 0 or respuesta > 5:
                return jsonify({'error': 'Los valores deben estar entre 0 y 5'})
            if porcentaje < 0 or porcentaje > 1:
                return jsonify({'error': 'Los porcentajes deben estar entre 0 y 100'})
            calificaciones_float.append(respuesta)
            porcentajes_float.append(porcentaje)

            suma_porcentajes += porcentaje
        
        epsilon = 0.1
        if round(suma_porcentajes, 2) > 1.0 + epsilon :
            return jsonify({'error': 'Los porcentajes deben sumar menos de 100%'}) 

        if round(suma_porcentajes, 2) < 1.0 - epsilon :
            return jsonify({'La suma de los porcentajes es': suma_porcentajes}) 

        # Aquí puedes hacer tus cálculos con NumPy y converte resultado antes de enviarlo
        calificaciones = np.array(calificaciones_float)
        porcentajes = np.array(porcentajes_float)
        promedionota = np.sum(calificaciones * porcentajes)
        promedionota = round(float(promedionota),2)

        # Devuelve el resultado como una respuesta JSON.
        return jsonify({'resultado': promedionota})

    except Exception as e:
        return jsonify({'error': str(e)}) # Aquí manejamos el error.

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)