from flask import *
from bd import Musica, Artista, Estilo, Premio


app = Flask(__name__)
pl = Musica
a = Artista
e = Estilo
p = Premio

@app.route('/')
def listar_musicas():
    musicas = pl.listar_musicas()
    return render_template("musica.html", musicas=musicas)

@app.route("/remover/<int:chave>")
def apagar(chave):
    pl.remove_musica(chave)
    return redirect('/')

@app.route("/nova_musica", methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        ds = request.form.to_dict()
        pl.nova_musica(dados.get('nome'), ds.get('tipo'), dados.get('artista'))
        return redirect('/')
    return render_template('musica_form.html', musica=None, title='Nova Musica')

@app.route("/editar/<int:chave>", methods=['GET', 'POST'])
def editar(chave):
    if request.method == 'POST':
        ds = request.form.to_dict()
        pl.atualiza_musica(chave, ds.get('nome'), dados.get('tipo'), dados.get('artista'))
        return redirect('/')
    musica = pl.atualiza_musica(chave)
    return render_template('musica_form.html', musica=musica, title='Editar Musica')

@app.route('/artista')
def listar_artista():
    artistas = a.listar_artistas()
    return render_template("artistas.html", artistas=artistas)

@app.route("/artista/remover/<int:id_time>")
def apagar_artista(id_artista):
    a.remove_artista(id_artista)
    return redirect('/artista')

@app.route("/artista/novo", methods=['GET', 'POST'])
def cadastro_artista():
    if request.method == 'POST':
        ds = request.form.to_dict()
        a.novo_artista(dados.get('nome'), ds.get('estilo_musica'), dados.get('sexo'))
        return redirect('/artista')
    return render_template('artista_form.html', artista=None, title='Novo(a) artista')

@app.route("/artista/editar/<int:id_artista>", methods=['GET', 'POST'])
def editar_artista(id_artista):
    if request.method == 'POST':
        ds = request.form.to_dict()
        a.atualiza_artista(id_artista, ds.get('nome'))
        return redirect('/artista')
    artista = a.detalha_artista(id_artista)
    return render_template('artista_form.html', artista=artista, title='Editar Artista')

@app.route('/estilo')
def listar_estilo():
    artistas = a.listar_estilos()
    return render_template("estilos.html", estilos=estilos)

@app.route("/estilo/remover/<int:id_estilo>")
def apagar_estilo(id_estilo):
    e.remove_estilo(id_estilo)
    return redirect('/estilo')

@app.route("/estilo/novo", methods=['GET', 'POST'])
def cadastro_estilo():
    if request.method == 'POST':
        ds = request.form.to_dict()
        e.novo_estilo(dados.get('nome_estilo'))
        return redirect('/estilo')
    return render_template('estilo_form.html', estilo=None, title='Novo estilo')

@app.route("/estilo/editar/<int:id_estilo>", methods=['GET', 'POST'])
def editar_estilo(id_estilo):
    if request.method == 'POST':
        ds = request.form.to_dict()
        e.atualiza_estilo(id_estilo, ds.get('nome_estilo'))
        return redirect('/estilo')
    estilo = e.atualiza_artista(id_estilo)
    return render_template('estilo_form.html', estilo=estilo, title='Editar Estilo')

@app.route('/premio')
def listar_premio():
    premio = p.listar_premio()
    return render_template("premio.html", premio=premio)

@app.route("/artista/remover/<int:id_time>")
def apagar_premio(id_premios):
    p.remove_premio(id_premio)
    return redirect('/premio')

@app.route("/premio/novo", methods=['GET', 'POST'])
def cadastro_premio():
    if request.method == 'POST':
        ds = request.form.to_dict()
        p.novo_premio(dados.get('artista'), ds.get('premio'))
        return redirect('/premio')
    return render_template('premio_form.html', premio=None, title='Novo premio')

@app.route("/premio/editar/<int:id_premio>", methods=['GET', 'POST'])
def editar_premio(id_premio):
    if request.method == 'POST':
        ds = request.form.to_dict()
        p.atualiza_premio(id_premio, ds.get('artista') ds.get('premio'))
        return redirect('/premio')
    artista = p.editar_premio(id_premio)
    return render_template('premio_form.html', premio=premio, title='Editar Premio')



if __name__ == '__main__':
    app.run()
