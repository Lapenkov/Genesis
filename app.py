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


@app.route('/analysis', methods=['GET', 'POST'])
def analysis():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM drug")
    entries = cursor.fetchall()
    genes = set([e[1] for e in entries])
    drugs = set([e[2] for e in entries])
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
    cursor = db.cursor()
    cursor.execute(u"SELECT recommendation FROM "
                   u"drug WHERE gene=\"{}\" AND drug=\"{}\"".format(gene, drug))
    recommendations = cursor.fetchall()
    if recommendations:
        result = recommendations[0][0]
    return result


@app.route('/')
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
