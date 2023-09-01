##Declaramos paqueterías 
##Jsonify tranforma un texto en una respuesta a formato json
from flask import Flask, request, jsonify

import spacy

sp = spacy.load("es_core_news_sm")

app = Flask(__name__)

#Aquí declaramos la ruta que tiene como método post, se llama entidades
@app.route('/entidades', methods=['POST'])
def entidades():
    try:
        data = request.json
        oraciones = data['oraciones']

        results = []
        #Se hace un recorrido de la lista de oraciones
        for oracion in oraciones:
            #Se manda la oración al modelo "es_core_news_sm"
            doc = sp(oracion)
            #Empieza el armado del objeto separando la oración y sus entidades
            enti = {"oración": oracion, "entidades": {ent.text: ent.label_ for ent in doc.ents}}

            results.append(enti)
            #Nos regresa el resultado con un status 200 y en formato json
        return jsonify({'resultado': results})
        #Si existe algún error, nos regresará el error específico en formato json
        #con un estatus 400
    except Exception as e:
        return jsonify({'error': str(e)}),400


if __name__ == 'pruebaflask':
    app.run(debug=True)
