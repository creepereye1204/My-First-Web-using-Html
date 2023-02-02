from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello():

  return render_template('Log_In.html')


########################################
@app.route('/Article/<index>')
def Article(index):
  print('ㅇ난영')

  conn = sqlite3.connect("Lists.db")
  cur = conn.cursor()
  cur.execute("SELECT Main FROM Lists where Indexs=" + index)
  rows = cur.fetchall()
  conn.commit()
  conn.close()
  return jsonify(rows)


##########################################


@app.route("/Home", methods=['POST'])
def Home():
  Id = request.form['Id']
  Pw = request.form['Pw']
  conn = sqlite3.connect("User.db")
  cur = conn.cursor()
  cur.execute("SELECT * FROM User")

  rows = cur.fetchall()

  for row in rows:
    if row[0] == Id and row[1] == Pw:
      return render_template('Home.html')
      break

  conn.close()

  return render_template('Failed_Log_In.html')


@app.route("/Write")
def Write():

  return render_template('Write.html')


@app.route("/List", methods=['POST'])
def List():
  Title = request.form['Title']
  Main = request.form['Main']
  conn = sqlite3.connect("Lists.db")
  cur = conn.cursor()
  cur.execute("SELECT * FROM Lists")
  rows = cur.fetchall()
  cur.execute("INSERT INTO Lists VALUES(?,?,?)", (len(rows) + 1, Title, Main))
  conn.commit()
  conn.close()
  return render_template('Home.html')


@app.route("/Lists")
def Lists():
  conn = sqlite3.connect("Lists.db")
  cur = conn.cursor()
  cur.execute("SELECT * FROM Lists")
  rows = cur.fetchall()
  conn.commit()
  conn.close()
  return jsonify(rows)


#booard_views.py 추가내용


@app.route('/Content/<index>')
def Content(index):
  # conn = sqlite3.connect("Lists.db")
  # cur = conn.cursor()
  # cur.execute("SELECT Main FROM Lists where Indexs=" + index)#############추가!!!!!!!
  # rows = cur.fetchall()
  # print(rows)
  # conn.commit()
  # conn.close()
  return render_template('Content.html', value=index)


if __name__ == '__main__':
  #conn = sqlite3.connect("User.db")
  #cur = conn.cursor()
  #cur.execute("INSERT INTO User VALUES(?,?,?)",('1','2','3'))
  #conn.commit()
  #conn.close()
  #https://lcs1245.tistory.com/entry/Python-Sqlite3-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0-%EB%A1%9C%EC%BB%AC-DB
  #https://hermeslog.tistory.com/181
  # conn = sqlite3.connect("Lists.db")
  # cur = conn.cursor()
  # cur.execute("CREATE TABLE IF NOT EXISTS Lists (Indexs integer PRIMARY KEY, Title text, Main text)")

  # conn.commit()
  # conn.close()

  # conn = sqlite3.connect("Lists.db")
  # cur = conn.cursor()
  # cur.execute("DELETE FROM Lists WHERE Indexs>1")
  # conn.commit()
  # conn.close()
  
  # https://lcs1245.tistory.com/entry/Python-Sqlite3-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0-%EB%A1%9C%EC%BB%AC-DB
  # https://hermeslog.tistory.com/181
  # conn = sqlite3.connect("Lists.db")
  # cur = conn.cursor()
  # cur.execute("CREATE TABLE IF NOT EXISTS Lists (Indexs integer PRIMARY KEY, Title text, Main text)")

  # conn.commit()
  # conn.close()

  app.run(host='0.0.0.0', debug=True)
