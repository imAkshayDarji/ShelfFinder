# Entry point for ShelfFinder Flask app
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        url = request.form.get("product_url")
        # Placeholder logic until scraper is connected
        result = f"You entered: {url}"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
