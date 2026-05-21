# 🧠 AI-Powered Customer Feedback Intelligence System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.45-red?style=for-the-badge&logo=streamlit)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-yellow?style=for-the-badge&logo=huggingface)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**An end-to-end AI system that transforms raw customer reviews into actionable business intelligence using state-of-the-art NLP models.**

[🌐 Live Demo](https://customer-feedback-intelligence-uefwexmnjwtzntw9nwpoih.streamlit.app/) • [📂 GitHub](https://github.com/vinaybanka/customer-feedback-intelligence) • [📊 Dataset](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews)

</div>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Live Demo](#-live-demo)
- [Key Features](#-key-features)
- [Project Workflow](#-project-workflow)
- [Tech Stack](#-tech-stack)
- [Dataset](#-dataset)
- [Model Performance](#-model-performance)
- [Dashboard Sections](#-dashboard-sections)
- [Project Structure](#-project-structure)
- [How to Run Locally](#-how-to-run-locally)
- [Results & Insights](#-results--insights)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

---

## 📖 Overview

The **AI-Powered Customer Feedback Intelligence System** is a full-stack data science project that processes over **568,000 Amazon Fine Food Reviews** and extracts meaningful patterns using advanced NLP techniques.

The system automatically:
- Detects sentiment (positive, negative, neutral) using a fine-tuned RoBERTa model
- Discovers hidden topics in customer feedback using BERTopic
- Extracts the most relevant keywords using KeyBERT
- Presents everything in an interactive, filterable Streamlit dashboard

This project simulates a real-world business intelligence tool that companies use to monitor customer satisfaction, detect product issues early, and make data-driven decisions.

---

## 🌐 Live Demo

🔗 **[Click here to view the live dashboard](https://customer-feedback-intelligence-uefwexmnjwtzntw9nwpoih.streamlit.app/)**

The dashboard includes:
- Real-time filtering by sentiment, star rating, and confidence score
- Interactive charts built with Plotly
- Keyword word cloud
- Review search and explorer

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🤖 AI Sentiment Analysis | RoBERTa model (97% accuracy) classifies each review as positive, negative, or neutral |
| 🏷️ Topic Modeling | BERTopic auto-discovers 10 hidden themes without any manual labeling |
| 🔑 Keyword Extraction | KeyBERT finds the most relevant phrases from customer feedback |
| 📊 Interactive Dashboard | Streamlit + Plotly dashboard with real-time filters and charts |
| 🗄️ Database Storage | All results stored in SQLite for fast querying |
| ☁️ Cloud Deployment | Fully deployed on Streamlit Cloud — accessible from any device |

---

## 🔄 Project Workflow

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────────┐
│  Phase 1        │     │  Phase 2          │     │  Phase 3            │
│  Data           │────▶│  Data             │────▶│  AI / NLP           │
│  Collection     │     │  Preprocessing    │     │  Analysis           │
│                 │     │                   │     │                     │
│ • Kaggle CSV    │     │ • HTML removal    │     │ • RoBERTa sentiment │
│ • 568K reviews  │     │ • Text cleaning   │     │ • BERTopic modeling │
│ • 10 columns    │     │ • Deduplication   │     │ • KeyBERT keywords  │
└─────────────────┘     │ • Normalization   │     └─────────────────────┘
                        └──────────────────┘                │
                                                            ▼
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────────┐
│  Phase 6        │     │  Phase 5          │     │  Phase 4            │
│  Deployment     │◀────│  Dashboard        │◀────│  Storage            │
│                 │     │                   │     │                     │
│ • GitHub        │     │ • Streamlit app   │     │ • SQLite database   │
│ • Streamlit     │     │ • Plotly charts   │     │ • 7 tables          │
│   Cloud         │     │ • Word cloud      │     │ • Summary tables    │
│ • Public URL    │     │ • Review explorer │     │ • Fast queries      │
└─────────────────┘     └──────────────────┘     └─────────────────────┘
```

---

## 🛠️ Tech Stack

### AI / Machine Learning
| Library | Version | Purpose |
|---|---|---|
| HuggingFace Transformers | 4.x | RoBERTa sentiment analysis model |
| BERTopic | Latest | Unsupervised topic modeling |
| KeyBERT | Latest | Keyword and keyphrase extraction |
| Sentence Transformers | Latest | Text embeddings |
| Scikit-learn | Latest | Vectorization and clustering |

### Data Processing
| Library | Version | Purpose |
|---|---|---|
| Pandas | 2.x | Data manipulation and analysis |
| NumPy | 1.x | Numerical operations |
| BeautifulSoup4 | Latest | HTML tag removal |
| NLTK | Latest | Text tokenization |

### Visualization & Dashboard
| Library | Version | Purpose |
|---|---|---|
| Streamlit | 1.45 | Interactive web dashboard |
| Plotly | 5.x | Interactive charts and graphs |
| WordCloud | Latest | Keyword visualization |
| Matplotlib | 3.x | Static chart generation |

### Storage & Deployment
| Tool | Purpose |
|---|---|
| SQLite | Local database storage |
| GitHub | Version control and code hosting |
| Streamlit Cloud | Free cloud deployment |

---

## 📁 Dataset

**Amazon Fine Food Reviews** from Kaggle

| Property | Value |
|---|---|
| Source | Kaggle — Amazon Fine Food Reviews |
| Total Reviews | 568,454 |
| After Cleaning | 393,115 |
| Time Period | 2000 – 2012 |
| Rating Scale | 1 to 5 stars |
| Language | English |

**Columns Used:**

| Column | Description |
|---|---|
| `ProductId` | Unique product identifier |
| `UserId` | Unique reviewer identifier |
| `Score` | Star rating (1–5) |
| `Time` | Unix timestamp of review |
| `Summary` | Short review headline |
| `Text` | Full review text |
| `HelpfulnessNumerator` | Number of helpful votes |
| `HelpfulnessDenominator` | Total votes received |

---

## 📈 Model Performance

### Sentiment Analysis — RoBERTa

| Metric | Result |
|---|---|
| Model | `cardiffnlp/twitter-roberta-base-sentiment-latest` |
| Accuracy | 97% |
| Reviews Analyzed | 10,000 |
| Processing Time | ~27 minutes on CPU |
| Avg Confidence Score | 0.84 |

**Agreement between Star Rating vs AI Sentiment:**

| Star Rating | AI: Negative | AI: Neutral | AI: Positive |
|---|---|---|---|
| 1–2 ⭐ (Negative) | **78%** | 10% | 13% |
| 3 ⭐ (Neutral) | 42% | **19%** | 39% |
| 4–5 ⭐ (Positive) | 6% | 7% | **87%** |

### Sentiment Distribution

| Sentiment | Count | Percentage |
|---|---|---|
| Positive 😊 | 6,233 | 62% |
| Negative 😞 | 2,747 | 27% |
| Neutral 😐 | 1,020 | 10% |

### Topics Discovered by BERTopic

| Topic | Keywords | Reviews |
|---|---|---|
| Topic 0 | tea, drink, taste, flavor | Most common |
| Topic 1 | chocolate, cookies, good | High volume |
| Topic 2 | sauce, salt, rice, seasoning | Medium |
| Topic 3 | food, dog, dogs, loves | Medium |
| Topic 4 | product, box, price, amazon | Medium |
| Topic 5 | oil, olive, olive oil | Lower |
| Topic 6 | baby, formula, organic, food | Lower |
| Topic 7 | tree, catch, dead, caught | Lower |

---

## 📊 Dashboard Sections

### 1. KPI Overview Cards
- Total reviews count
- Positive / Negative / Neutral counts with percentages
- Average star rating
- Average model confidence score

### 2. Sentiment Distribution
- Donut chart showing positive vs negative vs neutral split
- Interactive hover details

### 3. Rating Distribution
- Bar chart of 1–5 star ratings
- Color-coded by frequency

### 4. Sentiment Trend Over Time
- Line chart showing sentiment changes from 2002–2012
- Tracks how customer satisfaction evolved over time

### 5. Topic Distribution
- Horizontal bar chart of auto-discovered topics
- Shows which product categories get most feedback

### 6. Keyword Word Cloud
- Visual word cloud of most frequently mentioned terms
- Larger words = more frequent

### 7. Sentiment vs Rating Heatmap
- Cross-tabulation of AI sentiment vs star rating
- Shows where AI agrees/disagrees with star ratings

### 8. Review Explorer
- Search reviews by keyword
- Filter by sentiment, rating, confidence
- Browse individual reviews with full text

---

## 📂 Project Structure

```
customer-feedback-intelligence/
│
├── dashboard.py               ← Main Streamlit dashboard app
├── requirements.txt           ← Python dependencies
│
├── reviews_sentiment.csv      ← 10,000 reviews with AI sentiment
├── reviews_ai_analyzed.csv    ← 3,000 reviews with topics
├── reviews_keywords.csv       ← 500 reviews with keywords
│
└── README.md                  ← Project documentation
```

---

## 🚀 How to Run Locally

### Prerequisites
- Python 3.10+
- pip

### Step 1 — Clone the repository
```bash
git clone https://github.com/vinaybanka/customer-feedback-intelligence.git
cd customer-feedback-intelligence
```

### Step 2 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3 — Run the dashboard
```bash
streamlit run dashboard.py
```

### Step 4 — Open in browser
```
http://localhost:8501
```

---

## 💡 Results & Insights

Key findings from analyzing 568,000+ Amazon food reviews:

- **78% of 1-star reviews** were correctly identified as negative by AI — showing strong model performance on clearly unhappy customers
- **Tea and coffee** are the most discussed product categories across all reviews
- **Negative reviews mention specific product names** (Tabasco, K-cups, hot sauce) more than positive ones — suggesting unmet expectations
- **Review volume grew 10x** between 2006 and 2012 — showing Amazon's rapid growth in the food category
- **3-star reviews are genuinely ambiguous** — the AI model classified them as negative 42% of the time, showing that neutral reviews often contain underlying dissatisfaction

---

## 🔮 Future Improvements

- [ ] Add real-time review ingestion via Amazon API
- [ ] Implement aspect-based sentiment analysis (taste, price, packaging separately)
- [ ] Add email alert system when negative sentiment spikes
- [ ] Fine-tune RoBERTa on food-specific reviews for higher accuracy
- [ ] Add multilingual support for non-English reviews
- [ ] Build a REST API endpoint using FastAPI
- [ ] Add user authentication to the dashboard

---

## 👨‍💻 Author

**Vinay Banka**

- GitHub: [@vinaybanka](https://github.com/vinaybanka)
- Project: [customer-feedback-intelligence](https://github.com/vinaybanka/customer-feedback-intelligence)
- Live App: [View Dashboard](https://customer-feedback-intelligence-uefwexmnjwtzntw9nwpoih.streamlit.app/)

---

<div align="center">

⭐ **If you found this project useful, please give it a star on GitHub!** ⭐

</div>
