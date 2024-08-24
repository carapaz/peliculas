from flask import Flask,render_template
import pymysql  # Importar el conector PyMySQL


app = Flask(__name__)

# Configuración de la conexión a la base de datos
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = 'tatiana2006'
DB_NAME = 'peliculas'

def get_db_connection():
    conn = pymysql.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASS, db=DB_NAME)
    return conn


def get_peliculas():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id,titulo,imagen FROM datos_peliculas')
    peliculas = cursor.fetchall()
    cursor.close()
    conn.close()
    return peliculas


def get_pelicula(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query =(""" SELECT titulo,titulo_original,imagen,genero,anio,sinopsis,enlace FROM datos_peliculas
    WHERE id = %s """)
    cursor.execute(query, (id,))
    pelicula = cursor.fetchone()
    cursor.close()
    conn.close()
    return pelicula
print(get_pelicula(2))

@app.route('/')
def home():
    peliculas = get_peliculas()
    return render_template('index.html', peliculas=peliculas)

@app.route('/pelicula/<int:id>')
def pelicula(id):
    pelicula = get_pelicula(id)
    return render_template('detalle_pelicula.html', pelicula=pelicula)

if __name__ == "__main__":
    app.run(debug=True)