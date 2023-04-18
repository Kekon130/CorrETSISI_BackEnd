import os
import shutil
from flask import Flask, request, jsonify
from reconoce import borrarDirectorio, corregirExamen, leerRespuestas, escanearArchivo

app = Flask(__name__)


@app.route('/', methods=['POST'])
def corregir():
    try:
        print('Holi')
        rutaInput = '/tmp/Input'
        rutaOutput = '/tmp/Output'
        examen = request.files.get('examen')
        puntuacionAcertada = float(request.form.get('puntuacionAcertada'))
        puntuacionFallo = float(request.form.get('puntuacionFallo'))
        numPreguntas = int(request.form.get('numpreguntas'))
        print('variables extraidas')
        os.makedirs(rutaInput)
        shutil.copyfileobj(examen, open((rutaInput + '/examen.jpg'), 'wb'))
        print('Imagen copiada')
        os.makedirs(rutaOutput)
        escanearArchivo(rutaInput, rutaOutput)
        print('Examen escaneado')
        borrarDirectorio(rutaInput)
        print('Input borrado')
        examen = leerRespuestas(os.path.join(
            rutaOutput, os.listdir(rutaOutput)[0]), numPreguntas)
        print('Respuestas del examen leidas')
        solucion = leerRespuestas(
            'Soluciones/2023-04-11_09-44-04__keys.csv', 75)
        print('Solucion leida')
        nota = corregirExamen(
            examen, solucion, puntuacionAcertada, puntuacionFallo, numPreguntas)
        print('Examen corregido')
        borrarDirectorio(rutaOutput)
        return jsonify({'Preguntas acertadas:': nota[0], 'Preguntas incorrectas: ': nota[1], 'Calificacion: ': nota[2]})
    except Exception as ex:
        return ex.__str__()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=4000)
