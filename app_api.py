from flask import Flask, jsonify
import csv

app = Flask(__name__)

datos = []

def cargar_csv():
    with open('datos.csv', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            datos.append(fila)

@app.route('/api/datos', methods=['GET'])
def obtener_datos():
    return jsonify(datos)

@app.route('/api/datos/<id>', methods=['GET'])
def obtener_dato_por_id(id):
    for d in datos:
        if d['id'] == id:
            return jsonify(d)
    return jsonify({'error': 'Registro no encontrado'}), 404

if __name__ == '__main__':
    cargar_csv()
    app.run(debug=True)
