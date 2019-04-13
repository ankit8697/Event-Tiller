from flask import Flask, render_template
import CarletonCalendarScrape
# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

 
@app.route('/')
def root():
    CarletonCalendarScrape.main()
    return render_template("index.html")

@app.route('/data')
def data():
    return CarletonCalendarScrape.getAllData() 

if __name__ == "__main__":
    app.run(debug = True)