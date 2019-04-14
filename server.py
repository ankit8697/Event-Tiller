from flask import Flask, render_template
import CarletonCalendarScrape
import json_parser
# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

@app.route('/')
def root():
    return render_template("index.html")

@app.route('/data')
def data():
    return CarletonCalendarScrape.getAllData()

@app.route('/graph')
def graph():
    return render_template("graph.html")

@app.route('/index.html')
def index():
    return render_template("index.html")

@app.route('/graph.html')
def graph():
    return render_template("graph.html")

@app.route('/graph')
def graphServer():
    return render_template("graph.html")

@app.route('/stylesheet.css')
def style():
    return render_template("stylesheet.css")

if __name__ == "__main__":
    CarletonCalendarScrape.main()
    json_parser.parse_categories('event_data.json')
    app.run(debug = True)
    
