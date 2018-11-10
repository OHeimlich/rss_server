from flask import Flask, request, jsonify
from rss_manager import RSSManager

app = Flask(__name__)
rss_mng = RSSManager()

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/add', methods=['GET', 'POST'])
def add():
    data = request.json
    try:
        rss_mng.add_new_address(data.get('rss_address'))
        resp = jsonify(success=True)
        return resp
    except NameError as err:
        return jsonify(str(err))


@app.route('/search_by_dates', methods=['POST'])
def search_by_dates():
    data = request.json
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    try:
        res = rss_mng.get_feeds_by_dates(start_date, end_date)
        titles = [(doc.get('title'), doc.get('published')) for doc in res]
        return jsonify(str(titles))
    except NameError as err:
        return jsonify(str(err))


@app.route('/search', methods=['POST'])
def search():
    data = request.json
    try:
        res = rss_mng.search_content(data.get('keywords'))
        titles = [(doc.get('title'), doc.get('summary_detail')['base']) for doc in res]
        return jsonify(str(titles))
    except NameError as err:
        return jsonify(str(err))


if __name__ == '__main__':
    app.run()
