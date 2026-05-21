🧠 AI-Powered Customer Feedback Intelligence System
<div align="center">
Show Image
Show Image
Show Image
Show Image
An end-to-end AI system that transforms raw customer reviews into actionable business intelligence using state-of-the-art NLP models.
🌐 Live Demo • 📂 GitHub • 📊 Dataset
</div>

📌 Table of Contents

Overview
Live Demo
Key Features
Project Workflow
Tech Stack
Dataset
Model Performance
Dashboard Sections
Project Structure
How to Run Locally
Results & Insights
Future Improvements
Author


📖 Overview
The AI-Powered Customer Feedback Intelligence System is a full-stack data science project that processes over 568,000 Amazon Fine Food Reviews and extracts meaningful patterns using advanced NLP techniques.
The system automatically:

Detects sentiment (positive, negative, neutral) using a fine-tuned RoBERTa model
Discovers hidden topics in customer feedback using BERTopic
Extracts the most relevant keywords using KeyBERT
Presents everything in an interactive, filterable Streamlit dashboard

This project simulates a real-world business intelligence tool that companies use to monitor customer satisfaction, detect product issues early, and make data-driven decisions.

🌐 Live Demo
🔗 Click here to view the live dashboard
The dashboard includes:

Real-time filtering by sentiment, star rating, and confidence score
Interactive charts built with Plotly
Keyword word cloud
Review search and explorer


✨ Key Features
FeatureDescription🤖 AI Sentiment AnalysisRoBERTa model (97% accuracy) classifies each review as positive, negative, or neutral🏷️ Topic ModelingBERTopic auto-discovers 10 hidden themes without any manual labeling🔑 Keyword ExtractionKeyBERT finds the most relevant phrases from customer feedback📊 Interactive DashboardStreamlit + Plotly dashboard with real-time filters and charts🗄️ Database StorageAll results stored in SQLite for fast querying☁️ Cloud DeploymentFully deployed on Streamlit Cloud — accessible from any device

🔄 Project Workflow
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

🛠️ Tech Stack
AI / Machine Learning
LibraryVersionPurposeHuggingFace Transformers4.xRoBERTa sentiment analysis modelBERTopicLatestUnsupervised topic modelingKeyBERTLatestKeyword and keyphrase extractionSentence TransformersLatestText embeddingsScikit-learnLatestVectorization and clustering
Data Processing
LibraryVersionPurposePandas2.xData manipulation and analysisNumPy1.xNumerical operationsBeautifulSoup4LatestHTML tag removalNLTKLatestText tokenization
Visualization & Dashboard
LibraryVersionPurposeStreamlit1.45Interactive web dashboardPlotly5.xInteractive charts and graphsWordCloudLatestKeyword visualizationMatplotlib3.xStatic chart generation
Storage & Deployment
ToolPurposeSQLiteLocal database storageGitHubVersion control and code hostingStreamlit CloudFree cloud deployment

📁 Dataset
Amazon Fine Food Reviews from Kaggle
PropertyValueSourceKaggle — Amazon Fine Food ReviewsTotal Reviews568,454After Cleaning393,115Time Period2000 – 2012Rating Scale1 to 5 starsLanguageEnglish
Columns Used:
ColumnDescriptionProductIdUnique product identifierUserIdUnique reviewer identifierScoreStar rating (1–5)TimeUnix timestamp of reviewSummaryShort review headlineTextFull review textHelpfulnessNumeratorNumber of helpful votesHelpfulnessDenominatorTotal votes received

📈 Model Performance
Sentiment Analysis — RoBERTa
MetricResultModelcardiffnlp/twitter-roberta-base-sentiment-latestAccuracy97%Reviews Analyzed10,000Processing Time~27 minutes on CPUAvg Confidence Score0.84
Agreement between Star Rating vs AI Sentiment:
Star RatingAI: NegativeAI: NeutralAI: Positive1–2 ⭐ (Negative)78%10%13%3 ⭐ (Neutral)42%19%39%4–5 ⭐ (Positive)6%7%87%
Sentiment Distribution
SentimentCountPercentagePositive 😊6,23362%Negative 😞2,74727%Neutral 😐1,02010%
Topics Discovered by BERTopic
TopicKeywordsReviewsTopic 0tea, drink, taste, flavorMost commonTopic 1chocolate, cookies, goodHigh volumeTopic 2sauce, salt, rice, seasoningMediumTopic 3food, dog, dogs, lovesMediumTopic 4product, box, price, amazonMediumTopic 5oil, olive, olive oilLowerTopic 6baby, formula, organic, foodLowerTopic 7tree, catch, dead, caughtLower

📊 Dashboard Sections
1. KPI Overview Cards

Total reviews count
Positive / Negative / Neutral counts with percentages
Average star rating
Average model confidence score

2. Sentiment Distribution

Donut chart showing positive vs negative vs neutral split
Interactive hover details

3. Rating Distribution

Bar chart of 1–5 star ratings
Color-coded by frequency

4. Sentiment Trend Over Time

Line chart showing sentiment changes from 2002–2012
Tracks how customer satisfaction evolved over time

5. Topic Distribution

Horizontal bar chart of auto-discovered topics
Shows which product categories get most feedback

6. Keyword Word Cloud

Visual word cloud of most frequently mentioned terms
Larger words = more frequent

7. Sentiment vs Rating Heatmap

Cross-tabulation of AI sentiment vs star rating
Shows where AI agrees/disagrees with star ratings

8. Review Explorer

Search reviews by keyword
Filter by sentiment, rating, confidence
Browse individual reviews with full text


📂 Project Structure
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

🚀 How to Run Locally
Prerequisites

Python 3.10+
pip

Step 1 — Clone the repository
bashgit clone https://github.com/vinaybanka/customer-feedback-intelligence.git
cd customer-feedback-intelligence
Step 2 — Install dependencies
bashpip install -r requirements.txt
Step 3 — Run the dashboard
bashstreamlit run dashboard.py
Step 4 — Open in browser
http://localhost:8501

💡 Results & Insights
Key findings from analyzing 568,000+ Amazon food reviews:

78% of 1-star reviews were correctly identified as negative by AI — showing strong model performance on clearly unhappy customers
Tea and coffee are the most discussed product categories across all reviews
Negative reviews mention specific product names (Tabasco, K-cups, hot sauce) more than positive ones — suggesting unmet expectations
Review volume grew 10x between 2006 and 2012 — showing Amazon's rapid growth in the food category
3-star reviews are genuinely ambiguous — the AI model classified them as negative 42% of the time, showing that neutral reviews often contain underlying dissatisfaction


🔮 Future Improvements

 Add real-time review ingestion via Amazon API
 Implement aspect-based sentiment analysis (taste, price, packaging separately)
 Add email alert system when negative sentiment spikes
 Fine-tune RoBERTa on food-specific reviews for higher accuracy
 Add multilingual support for non-English reviews
 Build a REST API endpoint using FastAPI
 Add user authentication to the dashboard


👨‍💻 Author
Vinay Banka

GitHub: @vinaybanka
Project: customer-feedback-intelligence
Live App: View Dashboard
