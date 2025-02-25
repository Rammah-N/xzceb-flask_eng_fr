from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get("textToTranslate")
    translatedText = translator.english_to_french(textToTranslate)
    return "{} translated to French is: {}".format(textToTranslate, translatedText)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get("textToTranslate")
    translatedText = translator.french_to_english(textToTranslate)
    return "{} translated to English is: {}".format(textToTranslate, translatedText)


@app.route("/")
def renderIndexPage():
    # Write the code to render template
    result = render_template("index.html")
    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
