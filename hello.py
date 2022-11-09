from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    # return "<p>Hello, World!</p>"
    return render_template('home.html')

@app.route("/hola/<name>")
def hello(name):
    return render_template('hola.html', name=name)
    
@app.route("/rick/<page>")
def rick_and_morty(page=1):

    url = f'https://rickandmortyapi.com/api/character/?page={page}'

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    respuesta_json = response.json()
    info = respuesta_json['info']
    personajes = respuesta_json['results']

    next = int(page) + 1
    prev = int(page) -1

    return render_template('rick.html', personajes=personajes, prev=prev, next=next)
    
@app.route("/search", methods=['GET', 'POST'])
def search():
    print(requests)
    return "Busqueda"

if __name__ == '__main__':
    app.run(debug=True)