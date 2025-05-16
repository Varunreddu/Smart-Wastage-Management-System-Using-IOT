from flask import Flask, jsonify, render_template
import requests
import re

app = Flask(__name__)

# Adafruit IO credentials
AIO_USERNAME = "rapole"
AIO_KEY = "give your AIO KEY"
HEADERS = {"X-AIO-Key": AIO_KEY}

def extract_fill_level(msg):
    """Extracts the full 'Bin Fill Level: XX%' text."""
    match = re.search(r'Bin Fill Level: \d+%', msg)
    return match.group(0) if match else "N/A"

def extract_numeric_level(msg):
    """Extracts just the number from 'Bin Fill Level: XX%'."""
    match = re.search(r'Bin Fill Level: (\d+)%', msg)
    return int(match.group(1)) if match else None

def fetch_latest_value(feed):
    """Gets the latest full message and extracts 'Bin Fill Level: XX%'."""
    url = f"https://io.adafruit.com/api/v2/{AIO_USERNAME}/feeds/{feed}/data?limit=1"
    r = requests.get(url, headers=HEADERS)
    if r.status_code == 200 and r.json():
        return extract_fill_level(r.json()[0]['value'])
    return "No data"

def fetch_average(feed):
    """Gets average of last 15 numeric percentages from feed."""
    url = f"https://io.adafruit.com/api/v2/{AIO_USERNAME}/feeds/{feed}/data?limit=15"
    r = requests.get(url, headers=HEADERS)
    if r.status_code == 200:
        values = []
        for entry in r.json():
            num = extract_numeric_level(entry['value'])
            if num is not None:
                values.append(num)
        if values:
            return f"{round(sum(values) / len(values), 2)}%"
    return "N/A"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/bin1/latest")
def bin1_latest():
    return jsonify(value=fetch_latest_value("bin1"))

@app.route("/bin2/latest")
def bin2_latest():
    return jsonify(value=fetch_latest_value("bin2"))

@app.route("/bin1/average")
def bin1_average():
    return jsonify(average=fetch_average("bin1"))

@app.route("/bin2/average")
def bin2_average():
    return jsonify(average=fetch_average("bin2"))

if __name__ == "__main__":
    app.run(debug=True)
