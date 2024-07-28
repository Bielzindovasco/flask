from flask import *
from bd import Playlist

app = Flask(__name__)
pl = Playlist

@app.route('/')
def listar_playlist():
    playlists = pl.listar_playlist()
    return render_template("playlist.html", playlists=playlists)

@app.route("/remover/<int:chave>")
def apagar(chave):
    pl.remove_playlist(chave)
    return redirect('/')

@app.route("/nova", methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        dados = request.form.to_dict()
        pl.nova_playlist(dados.get('nome'), dados.get('tipo'), dados.get('artista'))
        return redirect('/')
    return render_template('playlist_form.html', playlist=None, title='Nova Playlist')

@app.route("/editar/<int:chave>", methods=['GET', 'POST'])
def editar(chave):
    if request.method == 'POST':
        dados = request.form.to_dict()
        pl.atualiza_playlist(chave, dados.get('nome'), dados.get('tipo'), dados.get('artista'))
        return redirect('/')
    playlist = pl.atualiza_playlist(chave)
    return render_template('playlist_form.html', playlist=playlist, title='Editar Playlist')

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
        a.novo_time(ds.get('nome'))
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
