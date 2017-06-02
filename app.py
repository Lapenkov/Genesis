import json
import wtforms as wt
from wtforms import TextField, Form
from flask import (
    Flask,
    Response,
    render_template,
    request
)
import pymysql

app = Flask(__name__)

db = pymysql.connect(host='78.46.211.29',
                     port=3306,
                     user='science',
                     passwd='sceincekaknerugatsamatom',
                     db='science',
                     charset='utf8')

NAMES = ['abc', 'abcd', 'abcde']


class SearchForm(Form):
    autocomp = TextField('autocomp', id='autocomplete')


@app.route('/autocomplete', methods=['GET', 'POST'])
def autocomplete():
    app.logger.debug(request.args)
    search = request.args.get('autocomplete')
    app.logger.debug(search)
    cursor = db.cursor()
    sql = "SELECT name FROM drug"
    cursor.execute(sql)
    return Response(json.dumps(cursor.fetchall()), mimetype='application/json')


@app.route('/analysis', methods=['GET', 'POST'])
def analysis():
    form = SearchForm(request.form)
    return render_template('analysis.html', form=form)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/')
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
