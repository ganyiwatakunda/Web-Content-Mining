import streamlit as st
import pandas as pd
import pickle
from preprocessing_utils import *

# Set page config
st.set_page_config(page_title="Web Content Mining", layout="centered")

# Landing Image
#st.image("news_landing.jpg", use_column_width=True)
st.image("news_landing.jpg", use_container_width=True)

use_container_width
# Title and Description
st.title("📰 Web Content Mining Platform")
st.markdown("""
Welcome to a web-based platform that clusters and displays related stories based on selected categories from four online newspapers.
Select a category below to explore the clustered articles.
""")

# Load Data
articles = pd.read_csv('clustered_articles.csv')
k_means = pickle.load(open('kmeans_model.pkl', 'rb'))

# Category Selection
selected_category = st.selectbox("📂 Select a news category:", ['Select one', 'politics', 'business', 'culture', 'sports'])

# Proceed only if a real category is selected
if selected_category != 'Select one':
    st.markdown(f"### 🏷️ Displaying Clusters for: **{selected_category.capitalize()}**")

    # Filter articles
    clustered_articles = articles[articles['category'] == selected_category]

    # Sort cluster labels (assuming integer labels)
    sorted_clusters = sorted(clustered_articles['clusters'].unique())

    # Display each cluster in an expandable section
    for cluster in sorted_clusters:
        with st.expander(f"🔹 Cluster {cluster}", expanded=False):
            cluster_articles = clustered_articles[clustered_articles['clusters'] == cluster]
            for _, row in cluster_articles.iterrows():
                st.markdown(f"**{row['article']}**  \n[Read more]({row['url']})")
            st.write("---")
else:
    st.info("Please select a category from the dropdown above to begin.")
