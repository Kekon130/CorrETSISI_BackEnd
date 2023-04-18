import os
import csv
import shutil


def escanearArchivo(ubicacionArchivo, ubicacionArchivoEscaneado):
    archivo = os.listdir(ubicacionArchivo)[0]
    rutaArchivo = os.path.join(ubicacionArchivo, archivo)
    if (os.path.isfile(rutaArchivo) and archivo.endswith('.jpg')):
        os.system(
            f'python src/main.py -e {ubicacionArchivo} {ubicacionArchivoEscaneado}')


def corregirExamen(examen, solucion, puntuacionAcertada, puntuacionFallo, numPreguntas):
    preguntasCorrectas = 0
    preguntasIncorrectas = 0
    for pregunta in range(numPreguntas):
        if (examen[pregunta] != 'G'):
            if (examen[pregunta] == solucion[pregunta]):
                preguntasCorrectas += 1
            else:
                preguntasIncorrectas += 1
    resultado = (preguntasCorrectas * puntuacionAcertada) - \
        (preguntasIncorrectas * puntuacionFallo)
    return [preguntasCorrectas, preguntasIncorrectas, resultado]


def leerRespuestas(ubicacionExamen, numPreguntas):
    respuestas = []
    with open(ubicacionExamen, 'r') as examen:
        lector = csv.DictReader(examen)
        for fila in lector:
            for pregunta in range(1, numPreguntas + 1):
                respuestas.append(fila['Q' + str(pregunta)])
    return respuestas


def borrarDirectorio(rutaDirectorio):
    archivos = os.listdir(rutaDirectorio)
    for archivo in archivos:
        os.remove(os.path.join(rutaDirectorio, archivo))
    os.rmdir(rutaDirectorio)
