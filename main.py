import streamlit as st
import openai

#Initialize OpenAI
api_key = "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"
openai.api_key = api_key

st.title("SEO - Article Generator")
st.subheader("Generate SEO articles in a jiffy!")

#Defining the function to generate the article
import openai

def generate_article(keywords, writing_style, words):
    """
    Generates an SEO optimized article based on the given keywords, writing style, and desired number of words.

    Args:
        keywords (str): The keywords to be included in the article.
        writing_style (str): The desired writing style of the article.
        words (int): The desired number of words in the article.

    Returns:
        str: The generated article.
    """
    respond_to_prompt = openai.Completion.create(
        engine="text-davinci-002",
        prompt = "Write an SEO optimized article which has these keywords " + keywords + "\nWriting style: " + writing_style + "\nNumber of words: " + str(words) + "\n\nArticle:",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    result = ''
    for choice in respond_to_prompt.choices:
        result += choice.text
        
    print(result)
    return result

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