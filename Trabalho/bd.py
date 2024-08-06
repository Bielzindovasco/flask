import sqlite3

class Musica:
    def criar():
        conn = sqlite3.connect('spotify.db')
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS musicas(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(255) NOT NULL,
                tipo VARCHAR(255) NOT NULL,
                artista VARCHAR(255) NOT NULL);
        """)

        conn.close()


    def nova_musica(nome, tipo, artista):
        conn = sqlite3.connect('spotify.db')
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO musicas(nome, tipo, artista)
            VALUES(?, ?, ?);
        """, (nome, tipo, artista))
        conn.commit()
        conn.close()


    def listar_musicas():
        conn = sqlite3.connect('spotify.db')
        cursor = conn.cursor()
        values = cursor.execute("SELECT * FROM musicas")
        resultado = []
        for row in values:
            resultado.append({
                'id': row[0],
                'nome': row[1],
                'tipo': row[2],
                'artista': row[3],
            })
        conn.close()
        return resultado


    def atualiza_musica(id, nome, tipo, artista):
        conn = sqlite3.connect('spotify.db')
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE musicas
            SET nome=?, tipo=?, artista=?
            WHERE id=?;
            """,
            (nome, tipo, artista, id)
        )
        conn.commit()
        conn.close()


    def remove_musica(id):
        conn = sqlite3.connect('spotify.db')
        cursor = conn.cursor()
        cursor.execute(
            """
            DELETE FROM musicas
            WHERE id=?;
            """,
            (id,)
        )
        conn.commit()
        conn.close()

class Artista:
    def criar():
        conn = sqlite3.connect('spotify.db')
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS artistas(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(255) NOT NULL,
                estilo_musica VARCHAR(255) NOT NULL,
                sexo VARCHAR(10) NOT NULL)
        """)

        conn.close()


    def novo_artista(nome, estilo_musica, sexo):
        conn = sqlite3.connect('spotify.db')
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO artistas(nome, estilo_musica, sexo)
            VALUES(?, ?, ?);
        """, (nome, estilo_musica, sexo))
        conn.commit()
        conn.close()


    def listar_artistas():
        conn = sqlite3.connect('spotify.db')
        cursor = conn.cursor()
        values = cursor.execute("SELECT * FROM artistas")
        resultado = []
        for row in values:
            resultado.append({
                'id': row[0],
                'nome': row[1],
                'estilo_musica': row[2],
                'artista': row[3],
            })
        conn.close()
        return resultado


    def atualiza_artista(id, nome, estilo_musica, sexo):
        conn = sqlite3.connect('spotify.db')
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE artistas
            SET nome=?, estilo_musica=?, sexo=?
            WHERE id=?;
            """,
            (nome, estilo_musica, sexo, id)
        )
        conn.commit()
        conn.close()


    def remove_artista(id):
        conn = sqlite3.connect('spotify.db')
        cursor = conn.cursor()
        cursor.execute(
            """
            DELETE FROM artistas
            WHERE id=?;
            """,
            (id,)
        )
        conn.commit()
        conn.close()

class Estilo:
    def criar():
        conn = sqlite3.connect('spotify.db')
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS estilos(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome_estilo VARCHAR(255) NOT NULL
            )
        """)

        conn.close()


    def novo_estilo(nome_estilo):
        conn = sqlite3.connect('spotify.db')
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO estilos(nome_estilos)
            VALUES(?, ?, ?);
        """, (nome_estilo))
        conn.commit()
        conn.close()


    def listar_estilos():
        conn = sqlite3.connect('spotify.db')
        cursor = conn.cursor()
        values = cursor.execute("SELECT * FROM estilos")
        resultado = []
        for row in values:
            resultado.append({
                'id': row[0],
                'nome_estilos': row[1],
            })
        conn.close()
        return resultado


    def atualiza_estilo(id, nome_estilo):
        conn = sqlite3.connect('spotify.db')
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE estilos
            SET nome=?, posicao=?, altura=?
            WHERE id=?;
            """,
            (nome_estilo, id)
        )
        conn.commit()
        conn.close()


    def remove_estilo(id):
        conn = sqlite3.connect('spotify.db')
        cursor = conn.cursor()
        cursor.execute(
            """
            DELETE FROM estilos
            WHERE id=?;
            """,
            (id,)
        )
        conn.commit()
        conn.close()

class Premio:
    def criar():
        conn = sqlite3.connect('spotify.db')
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS premios(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                artista VARCHAR(255) NOT NULL,
                premio VARCHAR(255) NOT NULL
                )
        """)

        conn.close()


    def novo_premio(artista,premio):
        conn = sqlite3.connect('spotify.db')
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO premios(artista, premio)
            VALUES(?, ?, ?);
        """, (artista, premio))
        conn.commit()
        conn.close()


    def listar_premio():
        conn = sqlite3.connect('spotify.db')
        cursor = conn.cursor()
        values = cursor.execute("SELECT * FROM premio")
        resultado = []
        for row in values:
            resultado.append({
                'id': row[0],
                'artista': row[1],
                'premio': row[2],
            })
        conn.close()
        return resultado


    def atualiza_premio(id, artista, premio):
        conn = sqlite3.connect('spotify.db')
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE premios
            SET artista=?, premio=?,
            WHERE id=?;
            """,
            (artista, premio, id)
        )
        conn.commit()
        conn.close()


    def remove_premio(id):
        conn = sqlite3.connect('spotify.db')
        cursor = conn.cursor()
        cursor.execute(
            """
            DELETE FROM premios
            WHERE id=?;
            """,
            (id,)
        )
        conn.commit()
        conn.close()


if __name__=='__main__':
    Musica.criar()
    Artista.criar()
    Estilo.criar()
    Premio.criar()
