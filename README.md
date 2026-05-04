# 🧠 Sentiment Analysis – NLP Project

A customer feedback classifier built with **Flask + Python** that uses **VADER** and **TextBlob** to detect whether text is Positive 😊, Neutral 😐, or Negative 😢.

---

## 🖥️ Live Demo Preview

> Enter any customer review → Get instant sentiment with confidence score, subjectivity meter, and animated score bars.

---

## 📁 Project Structure

```
sentiment-analysis/
│
├── app.py              # Flask backend (VADER + TextBlob analysis)
├── templates/
│   └── index.html      # Frontend UI
└── requirements.txt    # Python dependencies
```

---

## ⚙️ How It Works

The app combines two NLP libraries for more accurate results:

| Library | Role | Weight |
|---|---|---|
| **VADER** | Rule-based sentiment (great for social/review text) | 70% |
| **TextBlob** | ML-based polarity + subjectivity | 30% |

**Combined Score Formula:**
```
compound = (VADER compound × 0.7) + (TextBlob polarity × 0.3)
```

| Score | Label |
|---|---|
| ≥ 0.05 | 😊 Positive |
| ≤ -0.05 | 😢 Negative |
| Between | 😐 Neutral |

---

## 🚀 Installation & Setup

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/sentiment-analysis.git
cd sentiment-analysis
```

### 2. Install dependencies
```bash
pip install flask vaderSentiment textblob
python -m textblob.download_corpora
```

### 3. Set up templates folder
```bash
mkdir templates
mv index.html templates/
```

### 4. Run the app
```bash
python app.py
```

### 5. Open in browser
```
http://127.0.0.1:5000
```

---

## 📦 Requirements

```
flask
vaderSentiment
textblob
```

> Save as `requirements.txt` and install with: `pip install -r requirements.txt`

---

## ✨ Features

- ✅ Real-time sentiment analysis via REST API (`/analyze`)
- ✅ Animated score bars (Positive / Neutral / Negative %)
- ✅ Confidence score & Subjectivity meter
- ✅ Analysis history (last 5 results, clickable)
- ✅ Example buttons for quick testing
- ✅ Ctrl+Enter keyboard shortcut

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| NLP | VADER Sentiment, TextBlob |
| Frontend | HTML, CSS, Vanilla JS |
| API | REST (JSON) |

---

## 📸 Screenshots

> *(Add screenshots here after uploading to GitHub)*

---

## 👨‍💻 Author

Made with ❤️ as an NLP learning project.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
