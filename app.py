from flask import Flask, render_template, jsonify

app = Flask(__name__)

vagas = [{
    'id': 1,
    'titulo': 'Desenvolvedor Python',
    'localidade': 'RJ, Brasil',
    'salario': 'R$ 5.000,00'
}, {
    'id': 2,
    'titulo': 'Analista de dados',
    'localidade': 'PR, Brasil',
    'salario': 'R$ 3.000,00'
}, {
    'id': 3,
    'titulo': 'Cientista de dados',
    'localidade': 'SP, Brasil',
    'salario': 'R$ 4.000,00'
}, {
    'id': 4,
    'titulo': 'Desenvolvedor Backend',
    'localidade': 'SC, Brasil',
    'salario': 'R$ 4.500,00'
}, {
    'id': 5,
    'titulo': 'Desenvolvedor Frontend',
    'localidade': 'SP, Brasil',
    'salario': 'R$ 3.500,00'
}]


@app.route('/')
def page_home():
    return render_template('home.html', vagas=vagas)

@app.route("/vagas")
def list_vagas():
    return jsonify(vagas)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
