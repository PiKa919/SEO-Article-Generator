import streamlit as st
import openai

#Initialize OpenAI
api_key = "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"
model_id = "gpt-3.5-turbo"

st.title("SEO - Article Generator")
st.subheader("Generate SEO articles in a jiffy!")

#Defining the function to generate the article
def generate_article(keywords, writing_style, words):
    respond_to_prompt = openai.Completion.create(
        model_id="gpt-3.5-turbo",
        message = [
            {"role": "user", "content": "Write an SEO optimized article which has these keywords" + keywords + "\nWriting style: " + writing_style + "\nNumber of words: " + str(words) + "\n\nArticle:"},
        ]
    )
    result = ''
    for choice in respond_to_prompt.choices:
        result += choice.message.content
        
    print(result)
    return result
    
    # return "This is a test article generated"

#Defining the app
keyword = st.text_input("Enter keywords")
writing_style = st.selectbox("Select writing style", ["Formal", "Casual", "Friendly", "Humorous", "Poetic"])  
words = st.slider("Number of words", min_value=100, max_value=1000, value=300)

#Generate article
submit = st.button("Generate")

#Display article
if submit:
    message = st.empty()
    message.text("Generating article...")
    article = (generate_article(keyword, writing_style, words))
    message.text("Article generated!")
    st.write(article)
    
    #Download article
    st.download_button(label="Download article", data=article, file_name="article.txt", mime="text/txt")