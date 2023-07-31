
from flask import Flask, request
from flask_cors import CORS

from math import sqrt
import cmath


app = Flask(__name__)
CORS(app)

@app.route('/resolver', methods=['POST'])
def resolver_ecuacion():
    data = request.json
    a = float(data['a'])
    b = float(data['b'])
    c = float(data['c'])

    
    discriminante = b**2 - 4*a*c

    solucion1 = (-b + cmath.sqrt(discriminante)) / (2*a)
    solucion2 = (-b - cmath.sqrt(discriminante)) / (2*a)
    
    if solucion1.imag != 0:
        solucion1 = str(solucion1.real) + ' + ' + str(solucion1.imag) + 'i'
    else:
        solucion1 = solucion1.real  # Si no es complejo, guardamos solo la parte real

    if solucion2.imag != 0:
        solucion2 = str(solucion2.real) + ' + ' + str(solucion2.imag) + 'i'
    else:
        solucion2 = solucion2.real  # Si no es complejo, guardamos solo la parte real
       
        
    # Devolvemos las soluciones en formato JSON.
    return {"solucion1": solucion1, "solucion2": solucion2}


# Si este archivo se ejecuta directamente (en lugar de ser importado),
# entonces la aplicación se iniciará en el puerto 5000.
#if __name__ == "__main__":
#    app.run(port=5000)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
