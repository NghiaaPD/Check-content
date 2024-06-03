import google.generativeai as genai
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.set_page_config(
    page_title="Check content with SLM",
    page_icon="🤖",
    initial_sidebar_state="expanded"
)

# Sidebar
st.sidebar.markdown("## Select :green[**Models**] and :orange[**Categories**]")

models = st.sidebar.selectbox(
    "**Choose your Models:**",
    ("Gemini", "TinyLlamda", "Phi-2")
)

st.title("Checking the content of question")
st.write("""
- This tool will check the input content
- Returns the match rate between the sentence and the meaning
- Now it can check match rate of DBI, PFP, SSL
""")

st.subheader("🤖 Checker")

with st.form("form_1"):
    st.write("**Enter your question need check** ⬇️")
    question_check = st.text_area("**Input for question**", height=200)
    answer_check = st.text_area("**Enter true answer of your question**")

    st.write("")

    st.write("**Enter your question in db** ⬇️")
    question_inside = st.text_area("**Input for question from database**", height=200)
    answer_inside = st.text_area("**Enter true answer of question from database**")
    submitted = st.form_submit_button("Check !")

if submitted:
    if not question_check or not answer_check or not question_inside or not answer_inside:
        st.error("All fields are required")
    else:
        google_api_key = os.getenv('GEMINI_API_KEY')
        genai.configure(api_key=google_api_key)
        model = genai.GenerativeModel('gemini-1.0-pro')

        prompt = f"""
        Please compare for me the overlap between the structure and meaning of that question:
        "{question_check}" and the answer "{answer_check}" with the following question and answer:
        "{question_inside}" and "{answer_inside}". 
        Then JUST RETURN to me the:
        - percentage of similarity
        - structural similarity ratio
        - semantic overlap ratio and
        - the most duplicated words
        between the two pairs of question and answer with EXAMPLE of the output format as below:
        
        FORMAT EXAMPLE NEED TO RETURN:
        Overlap ratio: 0%
        Structural similarity ratio: 0%
        Semantic overlap ratio: 0%
        Most duplicated words: None
        """

        try:
            response = model.generate_content(prompt)

            text = ""
            for chunk in response:
                text += chunk.text
            textsplit = text.split("\n")

            st.write("**Comparison Result**")
            for line in textsplit:
                st.write(line)
        except Exception as e:
            st.error(str(e))
