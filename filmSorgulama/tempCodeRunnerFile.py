from flask import Flask, render_template, request
import mysql.connector
import os

app = Flask(__name__)
proje_dizini = os.path.dirname(os.path.abspath(__file__))

# MySQL veritabanı bağlantısı
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="fb123456",
    database="film_sorgu"
)

# Film türleri
film_turleri = [
    "Aksiyon",
    "Macera",
    "Komedi",
    "Drama",
    "Gerilim",
    "Bilim Kurgu",
    "Korku",
    "Romantik",
    "Belgesel",
    "Animasyon",
    "Fantastik"
]

# Ana sayfa
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        film_adi = request.form['film_adi']
        film_turu = request.form['film_turu']
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM films WHERE title LIKE %s AND genre LIKE %s", (f"%{film_adi}%", film_turu))
        films = cursor.fetchall()
        if films:
            return render_template('index.html', films=films, film_turleri=film_turleri)
    return render_template('index.html', films=[], film_turleri=film_turleri, not_found=True)

if __name__ == '__main__':
    app.run(debug=True)
