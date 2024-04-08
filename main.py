import streamlit as st
from PIL import Image
from utils import *


# Importing llama-index and its dependencies
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, ServiceContext


st.set_page_config(page_title="Gen AI Projects", layout="wide")

image = Image.open('./images/profile_pix.jpg')


# Use local CSS to manipulate Streamlit default styles
st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
        font-weight: 550;
    }
    .info-text {
        font-size:20px !important;
        margin-bottom: 0.5em;
    }
    .python-code {
        background: #000;
        color: #eee;
        padding: 10px;
        border-radius: 10px;
        overflow-x: auto;
    }
    .button {
            border-radius: 10px;
            border: 1px solid #fff;
            padding: 0.5em;
            font: inherit;
            cursor: pointer;
            text-decoration: underline;
            color: black;
            width: 100%;
            text-decoration: none;

    }
    a {
            text-decoration: none;
    }
    img {
        border-radius: 50%;
    }
    .description {
            font-size: 20px;
        }
    </style>
    """, unsafe_allow_html=True)

# st.write('----')
# Custom layout with columns
col1, col2 = st.columns(2)

# First column for profile image and quick links
with col1:
    st.image(image, width=280)  # replace with the path to the image
    st.markdown('### Hi, I’m Princewill', unsafe_allow_html=True)
    st.markdown('<div class="info-text">Data Scientist | Process Engineer </div>',
                unsafe_allow_html=True)

    col4, col5, col6 = st.columns(3)
    col4.markdown(
        '<a href="mailto:princewill.egbujor@gmail.com"><button class="button">Email</button></a>', unsafe_allow_html=True)

    col5.markdown(
        '<a href="https://www.linkedin.com/in/princewillegbujor/"><button class="button">LinkedIn</button></a>', unsafe_allow_html=True)
    col6.markdown(
        '<a href="https://elprinz1.github.io/portfolio-website/"><button class="button">Portfolio</button></a>', unsafe_allow_html=True)

# Second column for python code display
with col2:
    st.markdown("""
    ```python
    class AboutPrincewill:
        def __init__(self):
            self.occupation = 'Data Scientist | Process Engineer'
            self.skills = (
                'Python',
                'Machine Learning',
                'A/B testing',
                'Generative AI',
                'Project Management'
            )
            self.hobbies = (
                '⚽️ Playing Soccer',
                '🛫 Travelling'
            )
            self.current_favorite_music_artists = (
                'Dierk Bentley',
                'Eric Church',
                'Maroon 5',
            )
            self.fun_fact = 'Arsenal FC Fan'
    ```
    """, unsafe_allow_html=True)

    # Add more Streamlit components or custom HTML/CSS as needed for your content

st.write('---')

# SECTION 2

# RAG LLAMA Document Q/A ChatBot

row3_1, row3_2, row3_3 = st.columns([1, 4, 1])

with row3_2:
    st.title("Customize LLM Model Using llama.index - Document Q/A ChatBot")

    documents = []
    uploaded_files = st.file_uploader("Upload files (text or PDF)", type=[
        'txt', 'pdf'], accept_multiple_files=True)

    if uploaded_files is not None:
        # Creating a folder named "data" to store the uploaded files
        create_folder_if_not_exists("data")

        # Iterating through uploaded files and saving them
        for file_num, file in enumerate(uploaded_files):
            # Saving each uploaded file in the "data" folder with its original name
            with open(os.path.join("data", file.name), "wb") as f:
                f.write(file.getbuffer())
            st.success(
                f"File '{file.name}' uploaded successfully and stored in the 'data' folder.")

    try:
        # Trying to load files assuming this is where you're trying to load them
        documents = SimpleDirectoryReader(
            'data').load_data(show_progress=True)
    except ValueError as e:
        # Displaying error message if loading fails
        st.error(str(e))

    # Configuring service context
    embed_model_bge = HuggingFaceEmbedding(model_name="bert-base-uncased")

    # Configuring service context with default settings
    service_context = ServiceContext.from_defaults(embed_model=embed_model_bge,
                                                   chunk_size=5000,
                                                   chunk_overlap=100)

    # Creating index from documents
    index = VectorStoreIndex.from_documents(
        documents, service_context=service_context)

    # Creating query engine
    query_engine = index.as_query_engine()

    # Subheader for querying the uploaded files
    st.subheader(f"🔎 Let's Query the Document")

    # Text area for user to input query
    query = st.text_area("🗣️ Chat with the Document",
                         placeholder="Ask something about the document uploaded")

    # Processing user query if provided
    if query:
        response = query_engine.query(query)
        st.markdown(response.response.strip(), unsafe_allow_html=True)
