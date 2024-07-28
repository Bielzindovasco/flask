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



if __name__ == '__main__':
    app.run()
