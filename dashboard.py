import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import ast
import os

# ── Page config ───────────────────────────────────────────────
st.set_page_config(
    page_title="Customer Feedback Intelligence",
    page_icon="🧠",
    layout="wide"
)

# ── Load data from CSVs ───────────────────────────────────────
BASE = os.path.dirname(os.path.abspath(__file__))

@st.cache_data
def load_data():
    sentiment_df  = pd.read_csv(os.path.join(BASE, 'reviews_sentiment.csv'))
    analyzed_df   = pd.read_csv(os.path.join(BASE, 'reviews_ai_analyzed.csv'))
    keywords_df   = pd.read_csv(os.path.join(BASE, 'reviews_keywords.csv'))
    return sentiment_df, analyzed_df, keywords_df

sentiment_df, analyzed_df, keywords_df = load_data()

# ── Convert date ──────────────────────────────────────────────
sentiment_df['date'] = pd.to_datetime(sentiment_df['date'])

# ══════════════════════════════════════════════════════════════
# HEADER
# ══════════════════════════════════════════════════════════════
st.title("🧠 Customer Feedback Intelligence System")
st.markdown("**AI-powered analysis of Amazon Fine Food Reviews**")
st.divider()

# ══════════════════════════════════════════════════════════════
# SIDEBAR FILTERS
# ══════════════════════════════════════════════════════════════
st.sidebar.title("🔍 Filters")

sentiment_filter = st.sidebar.multiselect(
    "Sentiment",
    options=['positive', 'negative', 'neutral'],
    default=['positive', 'negative', 'neutral']
)

rating_filter = st.sidebar.multiselect(
    "Star Rating",
    options=[1, 2, 3, 4, 5],
    default=[1, 2, 3, 4, 5]
)

min_confidence = st.sidebar.slider(
    "Min Confidence Score",
    min_value=0.0,
    max_value=1.0,
    value=0.5,
    step=0.05
)

# ── Apply filters ─────────────────────────────────────────────
filtered_df = sentiment_df[
    (sentiment_df['ai_sentiment'].isin(sentiment_filter)) &
    (sentiment_df['rating'].isin(rating_filter)) &
    (sentiment_df['ai_sentiment_score'] >= min_confidence)
]

# ══════════════════════════════════════════════════════════════
# KPI CARDS
# ══════════════════════════════════════════════════════════════
st.subheader("📊 Overview")

total      = len(filtered_df)
positive   = len(filtered_df[filtered_df['ai_sentiment'] == 'positive'])
negative   = len(filtered_df[filtered_df['ai_sentiment'] == 'negative'])
neutral    = len(filtered_df[filtered_df['ai_sentiment'] == 'neutral'])
avg_rating = round(filtered_df['rating'].mean(), 2)
avg_conf   = round(filtered_df['ai_sentiment_score'].mean(), 2)

col1, col2, col3, col4, col5, col6 = st.columns(6)
col1.metric("Total Reviews",   f"{total:,}")
col2.metric("Positive 😊",     f"{positive:,}", f"{round(positive/total*100)}%")
col3.metric("Negative 😞",     f"{negative:,}", f"{round(negative/total*100)}%")
col4.metric("Neutral 😐",      f"{neutral:,}",  f"{round(neutral/total*100)}%")
col5.metric("Avg Star Rating", f"⭐ {avg_rating}")
col6.metric("Avg Confidence",  f"{avg_conf}")

st.divider()

# ══════════════════════════════════════════════════════════════
# ROW 1 — Sentiment + Rating Distribution
# ══════════════════════════════════════════════════════════════
col1, col2 = st.columns(2)

with col1:
    st.subheader("🎯 Sentiment Distribution")
    sent_counts = filtered_df['ai_sentiment'].value_counts().reset_index()
    sent_counts.columns = ['sentiment', 'count']
    colors = {'positive': '#2ecc71', 'negative': '#e74c3c', 'neutral': '#f39c12'}
    fig = px.pie(
        sent_counts, values='count', names='sentiment',
        color='sentiment', color_discrete_map=colors, hole=0.4
    )
    fig.update_layout(margin=dict(t=0, b=0))
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("⭐ Rating Distribution")
    rating_counts = filtered_df['rating'].value_counts().sort_index().reset_index()
    rating_counts.columns = ['rating', 'count']
    fig2 = px.bar(
        rating_counts, x='rating', y='count',
        color='count', color_continuous_scale='Blues',
        labels={'rating': 'Star Rating', 'count': 'Number of Reviews'}
    )
    fig2.update_layout(margin=dict(t=0, b=0), showlegend=False)
    st.plotly_chart(fig2, use_container_width=True)

# ══════════════════════════════════════════════════════════════
# ROW 2 — Sentiment Over Time
# ══════════════════════════════════════════════════════════════
st.subheader("📈 Sentiment Trend Over Time")

time_df = filtered_df.copy()
time_df['year_month'] = time_df['date'].dt.to_period('M').astype(str)
trend = time_df.groupby(['year_month', 'ai_sentiment']).size().reset_index(name='count')

fig3 = px.line(
    trend, x='year_month', y='count',
    color='ai_sentiment',
    color_discrete_map={'positive':'#2ecc71','negative':'#e74c3c','neutral':'#f39c12'},
    labels={'year_month': 'Month', 'count': 'Reviews', 'ai_sentiment': 'Sentiment'}
)
fig3.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig3, use_container_width=True)

# ══════════════════════════════════════════════════════════════
# ROW 3 — Topic Distribution + Word Cloud
# ══════════════════════════════════════════════════════════════
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏷️ Topic Distribution")
    topic_counts = analyzed_df['topic_name'].value_counts().reset_index()
    topic_counts.columns = ['topic', 'count']
    topic_counts = topic_counts[~topic_counts['topic'].str.startswith('-1')]
    fig4 = px.bar(
        topic_counts.head(8), x='count', y='topic',
        orientation='h', color='count',
        color_continuous_scale='Blues',
        labels={'topic': 'Topic', 'count': 'Reviews'}
    )
    fig4.update_layout(margin=dict(t=0, b=0), yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig4, use_container_width=True)

with col2:
    st.subheader("☁️ Keyword Word Cloud")
    try:
        all_keywords = []
        for kws in keywords_df['keywords']:
            try:
                parsed = ast.literal_eval(str(kws))
                all_keywords.extend(parsed)
            except:
                pass
        if all_keywords:
            text = ' '.join(all_keywords)
            wc = WordCloud(
                width=800, height=400,
                background_color='white',
                colormap='Blues', max_words=100
            ).generate(text)
            fig5, ax = plt.subplots(figsize=(10, 5))
            ax.imshow(wc, interpolation='bilinear')
            ax.axis('off')
            st.pyplot(fig5)
    except Exception as e:
        st.error(f"Word cloud error: {e}")

# ══════════════════════════════════════════════════════════════
# ROW 4 — Heatmap
# ══════════════════════════════════════════════════════════════
st.subheader("🔥 Sentiment vs Star Rating Heatmap")

heatmap_data = filtered_df.groupby(
    ['rating', 'ai_sentiment']
).size().reset_index(name='count')

heatmap_pivot = heatmap_data.pivot(
    index='rating', columns='ai_sentiment', values='count'
).fillna(0)

fig6 = px.imshow(
    heatmap_pivot, color_continuous_scale='Blues',
    labels=dict(x='AI Sentiment', y='Star Rating', color='Count'),
    text_auto=True
)
fig6.update_layout(margin=dict(t=0, b=0))
st.plotly_chart(fig6, use_container_width=True)

# ══════════════════════════════════════════════════════════════
# ROW 5 — Review Explorer
# ══════════════════════════════════════════════════════════════
st.subheader("🔍 Review Explorer")

search_term = st.text_input(
    "Search reviews by keyword",
    placeholder="e.g. tea, coffee, dog food..."
)

explore_df = filtered_df.copy()
if search_term:
    explore_df = explore_df[
        explore_df['text'].str.contains(search_term, case=False, na=False)
    ]

st.dataframe(
    explore_df[['date','rating','ai_sentiment','ai_sentiment_score','text','summary']]
    .sort_values('date', ascending=False)
    .head(50),
    use_container_width=True,
    height=400
)
st.caption(f"Showing {min(50, len(explore_df))} of {len(explore_df):,} filtered reviews")

# ══════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════
st.divider()
st.markdown("🧠 **Customer Feedback Intelligence System** — Built with Python, HuggingFace, BERTopic & Streamlit")