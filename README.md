# The Artifficial Intelligence Free & Open Source Stack (AI FOSS Stack)

The objective of the AI FOSS Stack is to serve as a foundational building block to build apps which can leverage pre-preained large language models (LLMs) which are open source and can run on low specification harware.

This solution is developed in the context of a collaboration between Fordham University and the UN Office of Information and Communications Technology. Read more: http://ideas.unite.un.org/fordham 

The team includes: Hannah, Remi, Peter, Sophie, Robert, and more.

# Installation (For Linux or Mac):

## Language Model
* Install a local LLM. Go to Ollama.ai to install and run your local LLM.
* Download the zephyr model using Ollama. From a terminal window type "$ollama pull zephyr". If your computer becomes slow you can try using a LLM with a smaller footprint such as orca-mini using "$ollama pull orca-mini"

## Obtain the app code
* $git clone http://this_Repo_URL

## Prep the environment
* $cd [path_this repo]
* create virtual env $python -m venv .venv
* activate it $source .venv/bin/activate     
* when you are finished you can deactivate this environment with: $deactivate

## Install required packages (Internet needed)
* $pip install --upgrade pip
* $pip install -r requirements.txt

## Run the app
* $streamlit run proto_aifoss.py --server.port 8504
* Your app will be running at http://localhost:8504


## Current Features
* Retrieval-augmented Generation (RAG) based on data stored in a local folder
* Generate sentence embeddings locally
* Generate text responses using Ollama Local LLM
* The app works offline (after installation with a internet connection)

## Upcoming Features
* Persist a local collection. (The database of embeddigns of the source documents which currently is created at load time)
* Configuration page to set key variables e.g: language model, embedding library,data sources, chat mode, temperature, system prompt, etc.
* Create and manage various collections of indexed source documents. And allow the user to switch between collections.
* Authentication
* User interface to configure new connections to content sources to be ingested (cloud-based storage e.g. google drive, web crawler, etc.)
* ..

# Acknowledgments
This project benefits significantly from opensource code from following entities, and the team extends its sincere appreciation to them:
* the https://ollama.ai/ project @ https://github.com/jmorganca/ollama
* [Streamlit](https://streamlit.io/), [llamaindex](https://www.llamaindex.ai/), and all libraries we are using.
* Caroline Frasca, Krista Muir and Yi Ding, for their app https://blog.streamlit.io/build-a-chatbot-with-custom-data-sources-powered-by-llamaindex/