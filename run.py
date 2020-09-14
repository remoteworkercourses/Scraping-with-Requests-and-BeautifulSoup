import bs4
import requests
import flask

app = flask.Flask(__name__)


@app.route('/')
def home():
    return flask.render_template('base.html')


@app.route('/detik-scraper')
def detik_scraper():
    html_doc = requests.get("https://www.detik.com/terpopuler", params={"tag_from": "wp_cb_mostPopular_more"})

    soup = bs4.BeautifulSoup(html_doc.text, "html.parser")

    popular_area = soup.find(attrs={"class": "grid-row list-content"})

    titles = popular_area.findAll(attrs={"class": "media__title"})
    images = popular_area.findAll(attrs={"class": "media__image"})
    return flask.render_template('detik-scraper.html', images=images)


@app.route('/idr-rates')
def idr_rates():
    source = requests.get('http://www.floatrates.com/daily/idr.json')
    json_data = source.json()
    return flask.render_template('idr-rates-scraper.html', datas=json_data.values())


if __name__ == '__main__':
    app.run(debug=True)
