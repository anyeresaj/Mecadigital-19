#-----------
#Flask es un microframework de Python usado para construir aplicaciones web
#Lo usaré p´ crear un servidor de back-end que se comunicará con la  aplicación React
#en el front-end.
#Un servidor web es UN PROGRAMA que sirve contenido a través de la web. 
#----------------

# Importamos la clase Flask del módulo flask. Flask es la clase principal que usaremos para crear nuestra aplicación.
from flask import Flask, request
# Importamos CORS del módulo flask_cors. CORS nos permitirá manejar las solicitudes de diferentes orígenes.
from flask_cors import CORS
# sqrt de math para calcular sqrt
from math import sqrt
import cmath


# Creamos una instancia de la clase Flask. 
# La variable __name__ se utiliza para determinar la raíz de la aplicación.
app = Flask(__name__)
# Habilitamos CORS para nuestra aplicación. 
# Esto nos permitirá recibir solicitudes de nuestra aplicación React.
CORS(app)

# Definimos una ruta para nuestra aplicación. Una ruta es una URL que el usuario puede visitar.
# Cuando un usuario visita la URL "/", nuestra aplicación responderá con "¡Hola, mundo!".
@app.route('/')
def hello_world():
    return '¡Hola, mundo! Soy el servidor Flask para el React de Neider'

# Definimos otra ruta: '/resolver', ésta ruta (endpoint) escuchará peticiones POST.
# Al acceder a esta ruta, se llama la función "resolver_ecuacion".
@app.route('/resolver', methods=['POST'])
def resolver_ecuacion():
    # Obtenemos los datos enviados en el cuerpo de la petición como JSON.
    data = request.json
    # Extraemos los valores de 'a', 'b' y 'c' de los datos.
    a = float(data['a'])
    b = float(data['b'])
    c = float(data['c'])

    
    # Calculamos el discriminante de la ecuación cuadrática.
    discriminante = b**2 - 4*a*c

    # Ahora permitiremos soluciones complejas.
    # Calculamos las dos soluciones de la ecuación.
    solucion1 = (-b + cmath.sqrt(discriminante)) / (2*a)
    solucion2 = (-b - cmath.sqrt(discriminante)) / (2*a)
    
    # Si las soluciones son complejas (parte imaginaria diferente de 0), se formatean correctamente como strings.
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
