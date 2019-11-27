from flask import Flask, render_template, request
from flaskext.mysql import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test'

mysql = MySQL(app)


@app.route('/', methods=['GET'])
@
def index():
    if request.method == "GET":
        firstName = "palathip"
        lastName = "wu"
        cur = mysql.connection.cursor()
        cur.execute("""INSERT INTO bbb(bbb, ccc) VALUES (%s, %s)""", (firstName, lastName))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')


if __name__ == '__main__':
    app.run()