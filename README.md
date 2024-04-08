# Document-QnA-ChatBot

Customize LLM Model Using llama.index - Document Q/A ChatBot

This project showcases the customization of the LLM (Large Language Model) using llama.index, a powerful tool for building Document Q/A (Question-Answering) ChatBots. By harnessing advanced natural language processing techniques and leveraging large language models, the project aims to create an intuitive and efficient system for interacting with documents.

For this purpose, it uses:

- [Streamlit](https://streamlit.io/): to build a data science web app
- [Hugging Face](https://huggingface.co/): Hugging Face's models are incorporated for various NLP tasks within the web app. This includes tasks such as text classification, sentiment analysis, etc.
- [Llama-index](https://docs.llamaindex.ai/): LLama index is used for semantic search and similarity matching in the web app. It provides tools for building semantic search engines and performing similarity search on large-scale text data.

## Dataset

- LLM Project requires upload of pdf or txt file.

## Run the project

If you don't have a Python environment available, you can use the [conda package manager](https://docs.conda.io/projects/conda/en/latest/index.html) which comes with the [Anaconda distribution](https://www.anaconda.com/download) to manage a clean Python environment.

Create a new environment and activate it:

```sh
conda create -n streamlit python=3.9
```

Install Python dependencies in the activate Python environment:

```sh
pip install -r requirements.txt
```

Create a [new API key](https://platform.openai.com/account/api-keys) and set it to the `OPENAI_API_KEY` environment variable beforehand.

On Windows:

```bash
set OPENAI_API_KEY="sk-..."
```

On Unix:

```sh
export OPENAI_API_KEY="sk-..."
```

Run the Streamlit project:

```sh
streamlit run streamlit_app.py
```
