import streamlit as st
import openai

api_key = "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"
model_id = "gpt-3.5-turbo"

def generate_article(keywords, writing_style, words):
    return "This is a test article generated"

keyword = st.text_input("Enter keywords")
writing_style = st.selectbox("Select writing style", ["Formal", "Casual", "Friendly", "Humorous", "Poetic"])  
words = st.slider("Number of words", min_value=100, max_value=1000, value=300)

submit = st.button("Generate")

if submit:
    message = st.empty()
    message.text("Generating article...")
    article = (generate_article(keyword, writing_style, words))
    message.text("Article generated!")
    st.write(article)
    
    st.download_button(label="Download article", data=article, file_name="article.txt", mime="text/txt")