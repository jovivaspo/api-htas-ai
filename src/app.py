from flask import Flask, jsonify, request, abort
from models.translate import get_translation
from models.extract_keywords import keywords
from models.paraphrase import paraphrase_control
from models.summarize import summarize
from models.sentiment import analyze

app = Flask(__name__)

@app.route('/api')
def api():
    message = "Welcome to this API-REST. You will found some tools made of transformers"
    return jsonify({"message":message})

@app.errorhandler(500)
def error(e):
    return jsonify(error=str(e)), 500

@app.route('/api/translate', methods=['POST'])

def translate():
    try:
        leng_dest = request.json['destino']
        text = request.json['text']

        text = text.split(".")
        text.pop()
        text_translated = ""

        for sentence in text:
            translate = get_translation(sentence, leng_dest)
            text_translated = text_translated + '. ' + translate

        text_translated = text_translated.replace('. ', '') + '.'
        print(text_translated)

        return text_translated

    except:
        abort(500, description="Error al traducir")

@app.route('/api/extract-keywords', methods=['POST'])
def extract_keywords():
    try:
        text = request.json['text']
        list_keywords = keywords(text)
        return list_keywords
    except:
        abort(500, description="Error al encontrar keywords")
  
@app.route('/api/paraphrase', methods=['POST'])
def paraphrase():
    try:
        text = request.json['text']
        phrase = paraphrase_control(text)
        print(phrase)
        return phrase['phrase']
    except:
          abort(500, description="Error al intentar parafrasear")

@app.route('/api/summarize', methods=['POST']) 
def summarize_text():
    try:
        text = request.json['text']
        sum = summarize(text)
        return sum
    except:
        abort(500, description="Error al intentar resumir"  )
   
@app.route('/api/sentiment', methods=['POST'])
def sentiment():
    try:
        text = request.json['text']
        result = analyze(text)
        return jsonify({"sentiment":result})

    except:
        abort(500,description="Error al analizar")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=4000)

