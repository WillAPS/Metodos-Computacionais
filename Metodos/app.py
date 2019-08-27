import json, request
from flask import Flask

app = Flask(__name__)

'''
Inputs Esperados
{
	"Media" : "5",
	"tamanhoAmostra" : "30",
	"desvioPadrao" : "2.56

}
'''


@app.route('/mediaConhecida', methods=['POST'])
def j_mediaConhecida():
	Media = request.json['Media']
	tamanhoAmostra = request.json['tamanhoAmostra']
	desvioPadrao = request.json['desvioPadrao']
	nivelConfiança = request.json['nivelConfiança']
	return Intervalo_Confiança.MediaConhecida(float(Media), int(tamanhoAmostra), float(desvioPadrao), float(nivelConfiança))



if __name__ == '__main__':
	app.run()
