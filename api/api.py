from flask import *
from Teste import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'TESTANDO MINHA API'

@app.route('/login', methods=['POST'])
def login():
    return request.form['user']

@app.route('/test')
def teste():
	t = Teste()
	a = t.show()
	return a

if __name__ == '__main__':
	app.run(debug=True)