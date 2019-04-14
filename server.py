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
    return render_template("graph.html", all_data = all_data)

@app.route('/index.html')
def index():
    return render_template("index.html")

@app.route('/graph.html')
def graph2():
    return render_template("graph.html")

@app.route('/graph')
def graphServer():
    return render_template("graph.html")

@app.route('/stylesheet.css')
def style():
    return render_template("stylesheet.css")

if __name__ == "__main__":
    all_data = CarletonCalendarScrape.getAllDataPython()
    #CarletonCalendarScrape.main()
    app.run(debug = True)
    
