import streamlit as st

st.set_page_config(
    page_title="Check content with SLM",
    page_icon="🤖",
    # layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar
st.sidebar.markdown("## Select :green[**Models**] and :orange[**Categories**]")

models = st.sidebar.selectbox(
    "**Choose your Models:**",
    ("GPT-4", "TinyLlamda", "Phi-2"))

categories = st.sidebar.selectbox(
    "**Choose your Categories:**",
    ("DBI", "PFP", "SSL"))

# Main page
st.title("Checking the content of question")
st.write("""
- This tool will check the input content
- Returns the match rate between the sentence and the meaning
- Now it can check match rate of DBi, PFP, SSL
""")

st.subheader("🤖 Checker")
with st.form("my_form"):
    st.write("Tool for check content ⬇️")

    question = st.text_area("**Input for question**", height=500)
    answer = st.text_area("**Enter true answer of your question**")

    # st.write(f"You wrote {len(question)} characters.")

    submitted = st.form_submit_button("Submit")
    if submitted:
        pass
