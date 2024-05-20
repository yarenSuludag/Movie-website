from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL bağlantısı
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="film_sorgu"
)

# Ana sayfa
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        film_adi = request.form["film_adi"]
        film_turu = request.form["film_turu"]
        ulke = request.form["ulke"]
        dil = request.form["dil"]
        prod_sirketi = request.form["prod_sirketi"]
        sirala = request.form["sirala"]
        
        cursor = mydb.cursor()

        sql = "SELECT * FROM films WHERE 1=1"

        if film_adi:
            sql += " AND title LIKE '%" + film_adi + "%'"
        if film_turu:
            sql += " AND genre = '" + film_turu + "'"
        if ulke:
            sql += " AND country = '" + ulke + "'"
        if dil:
            sql += " AND language = '" + dil + "'"
        if prod_sirketi:
            sql += " AND production_company = '" + prod_sirketi + "'"
        if sirala:
            if sirala == "imdb_rating" or sirala == "release_year":
                sql += " ORDER BY " + sirala + " DESC"
            else:
                sql += " ORDER BY " + sirala
        cursor.execute(sql)
        films = cursor.fetchall()

        cursor.execute("SELECT DISTINCT genre FROM films")
        film_turleri = [row[0] for row in cursor.fetchall()]
        
        cursor.execute("SELECT DISTINCT country FROM films")
        ulkeler = [row[0] for row in cursor.fetchall()]
        
        cursor.execute("SELECT DISTINCT language FROM films")
        diller = [row[0] for row in cursor.fetchall()]
        
        cursor.execute("SELECT DISTINCT production_company FROM films")
        prod_sirketleri = [row[0] for row in cursor.fetchall()]

        return render_template("index.html", films=films, film_turleri=film_turleri, sirala=sirala, ulkeler=ulkeler, diller=diller, prod_sirketleri=prod_sirketleri)

    else:
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM films")
        films = cursor.fetchall()

        cursor.execute("SELECT DISTINCT genre FROM films")
        film_turleri = [row[0] for row in cursor.fetchall()]
        
        cursor.execute("SELECT DISTINCT country FROM films")
        ulkeler = [row[0] for row in cursor.fetchall()]
        
        cursor.execute("SELECT DISTINCT language FROM films")
        diller = [row[0] for row in cursor.fetchall()]
        
        cursor.execute("SELECT DISTINCT production_company FROM films")
        prod_sirketleri = [row[0] for row in cursor.fetchall()]

        return render_template("index.html", films=films, film_turleri=film_turleri, ulkeler=ulkeler, diller=diller, prod_sirketleri=prod_sirketleri)

# Film ekleme
@app.route("/ekle", methods=["POST"])
def ekle():
    if request.method == "POST":
        film_adi = request.form["film_adi"]
        yonetmen = request.form["yonetmen"]
        tur = request.form["tur"]
        yil = request.form["yil"]
        sure = request.form["sure"]
        imdb_puani = request.form["imdb_puani"]
        ulke = request.form["ulke"]
        dil = request.form["dil"]
        prod_sirketi = request.form["prod_sirketi"]
        
        cursor = mydb.cursor()
        sql = "INSERT INTO films (title, director, genre, release_year, duration_minutes, imdb_rating, country, language, production_company) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (film_adi, yonetmen, tur, yil, sure, imdb_puani, ulke, dil, prod_sirketi)
        cursor.execute(sql, val)
        mydb.commit()

        return redirect("/", code=302)

# Film silme
@app.route("/sil/<int:film_id>")
def sil(film_id):
    cursor = mydb.cursor()
    sql = "DELETE FROM films WHERE id = %s"
    val = (film_id,)
    cursor.execute(sql, val)
    mydb.commit()

    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
