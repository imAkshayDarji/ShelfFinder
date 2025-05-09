# Entry point for ShelfFinder Flask app
from flask import Flask, render_template, request
from scrapers.amazon import scrape_amazon

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        url = request.form.get("product_url")
        if "amazon" in url:
            result = scrape_amazon(url)
        else:
            result = {"title": "Not an Amazon URL", "availability": "N/A"}
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
