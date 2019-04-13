from flask import Flask, render_template
import CarletonCalendarScrape
# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

@app.route('/data')
def data():
    return CarletonCalendarScrape.getAllData()

@app.route('/')
def root():
    return render_template("index.html")

if __name__ == "__main__":
    CarletonCalendarScrape.main()
    app.run(debug = True)
    
