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


"""os.makedirs('Input')
shutil.copy(
    "C:/Users/sergi/OneDrive/Escritorio/Ejemplo/Ejemplo_1/Input/1190_003.jpg", './Input')
os.makedirs('Output')
escanearArchivo('./Input', './Output')
borrarDirectorio('./Input')
examen = leerRespuestas(os.path.join(
    './Output', os.listdir('./Output')[0]), 75)
solucion = leerRespuestas('Soluciones/2023-04-11_09-44-04__keys.csv', 75)
nota = corregirExamen(examen, solucion, 1, 0.5, 75)
borrarDirectorio('./Output')"""
