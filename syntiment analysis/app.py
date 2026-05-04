from flask import Flask, render_template, request, jsonify
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()

def analyze(text):
    vader = analyzer.polarity_scores(text)
    blob = TextBlob(text)
    tb = blob.sentiment.polarity

    compound = vader['compound'] * 0.7 + tb * 0.3

    if compound >= 0.05:
        sentiment = "Positive"
        emoji = "😊"
    elif compound <= -0.05:
        sentiment = "Negative"
        emoji = "😢"
    else:
        sentiment = "Neutral"
        emoji = "😐"

    pos = round(vader['pos'] * 100, 1)
    neu = round(vader['neu'] * 100, 1)
    neg = round(vader['neg'] * 100, 1)
    confidence = min(round(abs(compound) * 100, 1), 95.0)
    subjectivity = round(blob.sentiment.subjectivity * 100, 1)

    return {
        "sentiment": sentiment,
        "emoji": emoji,
        "positive": pos,
        "neutral": neu,
        "negative": neg,
        "confidence": confidence,
        "subjectivity": subjectivity
    }

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze_route():
    data = request.get_json()
    text = data.get("text", "").strip()
    if not text:
        return jsonify({"error": "Text is empty"}), 400
    result = analyze(text)
    return jsonify(result)

if __name__ == "__main__":
    print("\n✅ Server chal raha hai!")
    print("🌐 Chrome mein kholo: http://127.0.0.1:5000\n")
    app.run(debug=True)
