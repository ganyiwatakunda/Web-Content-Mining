
import streamlit as st
import pandas as pd
import pickle
from preprocessing_utils import *

# Set Streamlit page settings
st.set_page_config(page_title="Web Content Mining", layout="centered")

# Landing image (replace with your image path or URL)
#st.image("news_landing.jpg", use_container_width=True)
st.image("news_landing.jpg", width=400)

#width=600

# Page title and description
st.title("📰 Web Content Mining Platform")
st.markdown("""
Welcome! This platform displays clusters of related news stories based on selected categories from four online newspapers.
""")

# Load data
articles = pd.read_csv('clustered_articles.csv')
k_means = pickle.load(open('kmeans_model.pkl', 'rb'))

# Category selection
selected_category = st.selectbox("📂 Select a news category:", ['Select one', 'politics', 'business', 'culture', 'sports'])

if selected_category != 'Select one':
    st.markdown(f"### 🏷️ Clusters for category: **{selected_category.capitalize()}**")

    # Filter articles by selected category
    clustered_articles = articles[articles['category'] == selected_category]

    # Sort cluster numbers (assumes numeric cluster labels)
    sorted_clusters = sorted(clustered_articles['clusters'].unique())

    # Show results
    for cluster in sorted_clusters:
        cluster_articles = clustered_articles[clustered_articles['clusters'] == cluster]
        with st.expander(f"🔹 Cluster {cluster}"):
            st.write("Related Articles:")
            st.write(cluster_articles[['article', 'url']])
            st.markdown("---")
else:
    st.info("Please select a category to see the related clusters and articles.")

