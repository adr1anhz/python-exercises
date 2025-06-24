from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")



@app.route("/api/v1/<word>")
def get_definition(word):
    info = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    f = requests.get(info)
    f2 = f.json()
    definition = f2[0]['meanings'][0]['definitions'][0]['definition']
    return {"definition": definition,
            "word": word}

if __name__ == "__main__":
    app.run(debug=True, port=5000)