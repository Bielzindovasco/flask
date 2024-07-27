import sqlite3

class Playlist:
    def criar():
        conn = sqlite3.connect('playlist.db')
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS playlists(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(255) NOT NULL,
                tipo VARCHAR(255) NOT NULL,
                artista VARCHAR(255) NOT NULL);
        """)

        conn.close()


    def nova_playlist(nome, tipo, artista):
        conn = sqlite3.connect('playlist.db')
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO playlists(nome, tipo, artista)
            VALUES(?, ?, ?);
        """, (nome, tipo, artista))
        conn.commit()
        conn.close()


    def listar_playlist():
        conn = sqlite3.connect('playlist.db')
        cursor = conn.cursor()
        values = cursor.execute("SELECT * FROM playlists")
        resultado = []
        for row in values:
            resultado.append({
                'id': row[0],
                'nome': row[1],
                'tpo': row[2],
                'artista': row[3],
            })
        conn.close()
        return resultado


    def atualiza_playlist(id, nome, tipo, artista):
        conn = sqlite3.connect('playlist.db')
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE playlists
            SET nome=?, posicao=?, altura=?
            WHERE id=?;
            """,
            (nome, tipo, artista, id)
        )
        conn.commit()
        conn.close()


    def remove_playlist(id):
        conn = sqlite3.connect('playlist.db')
        cursor = conn.cursor()
        cursor.execute(
            """
            DELETE FROM playlists
            WHERE id=?;
            """,
            (id,)
        )
        conn.commit()
        conn.close()



if __name__=='__main__':
    Playlist.criar()
