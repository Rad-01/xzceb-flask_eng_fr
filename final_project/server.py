from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def translateToFrench():
    textToTranslate = request.args.get('textToTranslate')
    Translation = translator.english_to_french(textToTranslate)

    return Translation

@app.route("/frenchToEnglish")
def translateToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    Translation = translator.french_to_english(textToTranslate)

    return Translation

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
