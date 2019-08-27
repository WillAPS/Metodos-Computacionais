from flask import Flask, request
import Intervalo_Confiança
import Coeficiente_Correlação
import Reamostragem


app = Flask(__name__)


@app.route('/mediaConhecida', methods=['POST'])
def json_mediaConhecida():
	media = request.json['media']
	tamanhoAmostra = request.json['tamanhoAmostra']
	desvioPadrao = request.json['desvioPadrao']
	nivelConfianca = request.json['nivelConfianca']
	result = Intervalo_Confiança.MediaConhecida(float(media), int(tamanhoAmostra), float(desvioPadrao), float(nivelConfianca))
	return str(result)


@app.route('/mediaPopulacional', methods=['POST'])
def json_mediaPopulacional():
	tamanhoAmostra = request.json['tamanhoAmostra']
	tamanhoAmostra_Sucesso = request.json['tamanhoAmostra_Sucesso']
	nivelConfianca = request.json['nivelConfianca']
	result = Intervalo_Confiança.MediaPopulacional(int(tamanhoAmostra), int(tamanhoAmostra_Sucesso), float(nivelConfianca))
	return str(result)


@app.route('/mediaAmostral', methods=['POST'])
def json_mediaAmostral():
	media = request.json['media']
	tamanhoAmostra = request.json['tamanhoAmostra']
	desvioPadrao = request.json['desvioPadrao']
	nivelConfianca = request.json['nivelConfianca']
	result = Intervalo_Confiança.mediaAmostral(float(media), int(tamanhoAmostra), float(desvioPadrao), float(nivelConfianca))
	return str(result)


@app.route('/correlacaoPearson', methods=['POST'])
def json_correlacaoPearson():
	n = request.json['n']
	Vx = request.json['Vx']
	Vy = request.json['Vy']
	result = Coeficiente_Correlação.Correlacao_Pearson(Vx, Vy, int(n))
	return str(result)


@app.route('/correlacaoKendall', methods=['POST'])
def json_correlacaoKendall():
	n = request.json['n']
	Vx = request.json['Vx']
	Vy = request.json['Vy']
	result = Coeficiente_Correlação.Correlacao_Kendall(Vx, Vy, int(n))
	return str(result)


@app.route('/correlacaoSpearman', methods=['POST'])
def json_correlacaoSpearman():
	n = request.json['n']
	Vx = request.json['Vx']
	Vy = request.json['Vy']
	result = Coeficiente_Correlação.Correlacao_Spearman(Vx, Vy, int(n))
	return str(result)


@app.route('/bootstrap', methods=['POST'])
def json_bootstrap():
	n = request.json['n']
	repeticoes = request.json['repeticoes']
	v = request.json['v']
	result = Reamostragem.bootstrap(v, int(repeticoes), int(n))
	return str(result)


@app.route('/jackknife', methods=['POST'])
def json_jackknife():
	n = request.json['n']
	v = request.json['v']
	result = Reamostragem.jackknife(v, int(n))
	return str(result)


if __name__ == '__main__':
	app.run()
