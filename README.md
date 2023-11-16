## The Artifficial Intelligence Free & Open Source Stack (AI FOSS Stack)

This solution was developed in the context of a collaboration between Fordham University and the UN office of Information and Communications Technology. Read more: http://ideas.unite.un.org/fordham 

The objective of the AI FOSS Stack is to serve as a foundational building block to build apps which can leverage pre-preained large language models (LLMs) which are open source and can run on low specification harware.

This projects thanks the entities below from their great work:
* the https://ollama.ai/ project @ https://github.com/jmorganca/ollama
* Streamlit, llamaindex, and all libraries we are using.
* Caroline Frasca, Krista Muir and Yi Ding, for their app https://blog.streamlit.io/build-a-chatbot-with-custom-data-sources-powered-by-llamaindex/ @ https://github.com/carolinedlu/llamaindex-chat-with-streamlit-docs

## Installation:

# Language Model
* Install a local LLM using Ollama.ai
* Download the orca-mini model using $ollama pull orca-mini

# Obtain the app code
* $git clone [this repo]

# Prep the environment
* $cd [this repo]
* create virtual env $python -m venv .venv
* activate it $source .venv/bin/activate     
* when you are finished you can deactivate this environment with: $deactivate

# Install required packages (Internet needed)
* $pip install --upgrade pip
* $pip install -r requirements.txt

# Run the app
* $streamlit run proto_aifoss.py --server.port 8504
* Your app wil be running at http://localhost:8504


# Current Features
* Retrieval-augmented Generation (RAG) based on data stored in a local folder
* Generate sentence embeddings locally
* Generate text responses using Ollama Local LLM
* The app works offline (after installation with a internet connection)

# Upcoming Features
* Persist local embedding database (to avoid indexing source documents everytime)
* Configuration page to set key variables e.g: language model, embedding library,data sources, chat mode, temperature, system prompt, etc.
* 