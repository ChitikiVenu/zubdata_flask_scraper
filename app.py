from flask import Flask, render_template_string, request
from scraper import scrape_google_maps

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
  <title>Google Maps Scraper</title>
</head>
<body>
  <h1>Google Maps Scraper</h1>
  <form method="POST">
    <input type="text" name="query" placeholder="Enter keyword..." required>
    <button type="submit">Scrape</button>
  </form>
  {% if result %}
    <h3>Scraped Data:</h3>
    <div style="white-space: pre-wrap;">{{ result }}</div>
  {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        query = request.form["query"]
        result = scrape_google_maps(query)
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
