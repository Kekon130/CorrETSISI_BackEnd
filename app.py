import os
import shutil
import cv2
from flask import Flask, request, jsonify
from reconoce import borrarDirectorio, corregirExamen, leerRespuestas, escanearArchivo

app = Flask(__name__)


@app.route('/', methods=['POST'])
def corregir():
    try:
        rutaInput = '/tmp/Input'
        rutaOutput = '/tmp/Output'
        examen = request.files.get('examen')
        puntuacionAcertada = float(request.form.get('puntuacionAcertada'))
        puntuacionFallo = float(request.form.get('puntuacionFallo'))
        numPreguntas = int(request.form.get('numpreguntas'))
        os.makedirs(rutaInput)
        shutil.copyfileobj(examen, open((rutaInput + '/examen.jpg'), 'wb'))
        os.makedirs(rutaOutput)
        escanearArchivo(rutaInput, rutaOutput)
        borrarDirectorio(rutaInput)
        examen = leerRespuestas(os.path.join(
            rutaOutput, os.listdir(rutaOutput)[0]), numPreguntas)
        solucion = leerRespuestas(
            'Soluciones/2023-04-11_09-44-04__keys.csv', 75)
        nota = corregirExamen(
            examen, solucion, puntuacionAcertada, puntuacionFallo, numPreguntas)
        borrarDirectorio(rutaOutput)
        return jsonify({'Preguntas acertadas:': nota[0], 'Preguntas incorrectas: ': nota[1], 'Calificacion: ': nota[2]})
    except Exception as ex:
        return ex.__str__()


if __name__ == '__main__':
    app.run()
