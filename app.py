# coding: utf-8
import json
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


@app.route('/analysis', methods=['GET', 'POST'])
def analysis():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM drug")
    drugs = cursor.fetchall()
    cursor.execute("SELECT * FROM polymorphism")
    genes = cursor.fetchall()
    return render_template('analysis.html', drugs=drugs, genes=genes)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/result', methods=['POST'])
def result():
    result = u"Коррекция не требуется"
    args = request.form
    gene = args['gene']
    drug = args['drug']
    return result


@app.route('/')
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
