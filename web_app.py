import streamlit as st
import pandas as pd
import pickle

from preprocessing_utils import *

st.write(""" 
    # Cluster News Articles
""")

articles = pd.read_csv('clustered_articles.csv')

# Get user input
news_article = st.text_input("Paste a news article: ")
news_category = st.text_input("Enter the category of the news article: Allowed categories are [politics, business, culture, sports]")
news_url = st.text_input("Enter link to news article: ")

if news_article and news_category and news_url:
    st.write("**News Article **: " , news_article)
    st.write("**Category **:" , news_category)
    st.write("**Link to Article **:" , news_url)

    k_means = pickle.load(open('kmeans_model.pkl', 'rb'))
    tfidf_vectorizer = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))
    tfidf_pca = pickle.load(open('tfidf_pca.pkl', 'rb'))

    preprocessed_news_article = preprocess_article(news_article) 
    tfidf_article = tfidf_vectorizer.transform(np.array([preprocessed_news_article]))

    tfidf_pca_comp = tfidf_pca.transform(tfidf_article.toarray())

    st.write('NEWS CLUSTERS')

    #Articles in cluster 0
    cluster_0 = articles[articles['clusters'] == 0][['category', 'article', 'clusters', 'url']]
    st.write('Cluster 0')
    st.write(cluster_0)

    #Articles in cluster 1
    cluster_1 = articles[articles['clusters'] == 1][['category', 'article', 'clusters', 'url']]
    st.write('Cluster 1')
    st.write(cluster_1)

    #Articles in cluster 2
    cluster_2 = articles[articles['clusters'] == 2][['category', 'article', 'clusters', 'url']]
    st.write('Cluster 2')
    st.write(cluster_2)

    #Articles in cluster 3
    cluster_3 = articles[articles['clusters'] == 3][['category', 'article', 'clusters', 'url']]
    st.write('Cluster 3')
    st.write(cluster_3)

    #Articles in cluster 4
    cluster_4 = articles[articles['clusters'] == 4][['category', 'article', 'clusters', 'url']]
    st.write('Cluster 4')
    st.write(cluster_4)

    #Articles in cluster 5
    cluster_5 = articles[articles['clusters'] == 5][['category', 'article', 'clusters', 'url']]
    st.write('Cluster 5')
    st.write(cluster_5)

    #Articles in cluster 6
    cluster_6 = articles[articles['clusters'] == 6][['category', 'article', 'clusters', 'url']]
    st.write('Cluster 6')
    st.write(cluster_6)

if st.button("Cluster Article"):
    cluster = k_means.predict(tfidf_pca_comp)

    if cluster == 0:
        st.write('Your article belongs to cluster: ', str(cluster))
        st.write(cluster_0)

    elif cluster == 1:
        st.write('Your article belongs to cluster: ', str(cluster))
        st.write(cluster_1)

    elif cluster == 2:
        st.write('Your article belongs to cluster: ', str(cluster))
        st.write(cluster_2)

    elif cluster == 3:
        st.write('Your article belongs to cluster: ', str(cluster))
        st.write(cluster_3)

    elif cluster == 4:
        st.write('Your article belongs to cluster: ', str(cluster))
        st.write(cluster_4)

    elif cluster == 5:
        st.write('Your article belongs to cluster: ', str(cluster))
        st.write(cluster_5)
    
    elif cluster == 6:
        st.write('Your article belongs to cluster: ', str(cluster))
        st.write(cluster_6)
