from flask import Flask, render_template_string, request, send_file
from scraper import scrape_google_maps

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
  <title>Zubdata Scraper</title>
</head>
<body style="font-family: Arial; text-align:center; padding-top:50px;">
  <h2>🗺️ Zubdata - Google Maps Scraper</h2>
  <form method="POST">
    <input type="text" name="query" placeholder="Enter keyword or category" style="width:300px; padding:8px;">
    <br><br>
    <button type="submit">Start Scraping</button>
  </form>
  {% if file_ready %}
  <p>✅ Done! <a href="/download">Download CSV</a></p>
  {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        query = request.form["query"]
        scrape_google_maps(query)
        return render_template_string(HTML, file_ready=True)
    return render_template_string(HTML, file_ready=False)

@app.route("/download")
def download():
    return send_file("results.csv", as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

