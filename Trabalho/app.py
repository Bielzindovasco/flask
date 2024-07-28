from flask import *
from bd import musica
from bd import artista

app = Flask(__name__)
pl = Musica
a = Artista

@app.route('/')
def listar_musica():
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
def listar_artistas():
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



if __name__ == '__main__':
    app.run()
