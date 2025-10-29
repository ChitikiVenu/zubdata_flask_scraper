# app.py
from flask import Flask, render_template_string, request
from scraper import scrape_google_maps

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head><title>Zubdata Google Maps Scraper</title></head>
<body style="font-family: Arial; text-align:center; margin-top:50px;">
    <h1>Zubdata Google Maps Scraper</h1>
    <form method="post">
        <input name="query" placeholder="Enter keywords..." size="40" required>
        <button type="submit">Scrape</button>
    </form>
    {% if message %}
        <p style="margin-top:30px;">{{ message }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        query = request.form.get("query")
        message = scrape_google_maps(query)
    return render_template_string(HTML_PAGE, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
