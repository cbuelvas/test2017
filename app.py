from flask import Flask, render_template, json, request
from flask.ext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'test2017'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/database')
def showInfo():
    return render_template('database.html')


@app.route('/save',methods=['POST','GET'])
def save():
    try:
        _name = request.form['inputName']
        _color = request.form['inputColor']
        _pet = request.form['inlineRadioOptions']

        print _name, _color, _pet

        # validate the received values
        if _name and _color and _pet:
            print "PROCEDE TO BURN"
            # All Good, let's call MySQL

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_createData',(_name,_color,_pet))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return json.dumps({'message':'Data saved successfully !'})
            else:
                return json.dumps({'error':str(data[0])})
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})

    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    app.run(port=5002)
